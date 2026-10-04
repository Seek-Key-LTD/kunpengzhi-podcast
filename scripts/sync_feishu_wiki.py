#!/usr/bin/env python3
"""仓库文字稿 <-> 飞书知识库 双向同步。

方向：
  push（默认）：仓库 main 的文稿 → 飞书知识库
  pull：       飞书知识库的改动 → 仓库工作区（供 CI 开 PR）

幂等与防抖：
  每条文档在 state 里记 {node_token, obj_token, sha256, revision_id}。
  - 仓库文件 sha256 != state.sha256            → 仓库改了 → 推
  - 飞书 doc revision_id != state.revision_id  → 飞书改了 → 拉
  推/拉之后都会把新的 sha 与 revision 写回 state，所以自己造成的 revision 变化
  不会被下一轮当成"别人改的"（防来回抖动）。

冲突策略：两边都改 → **飞书优先**（pull 覆盖仓库；push 侧看到 revision 变过就不推）。
代价：飞书导出的 markdown 与仓库原文有系统性格式差异（行尾硬换行、引用块层级等），
      被拉回过的文档格式会变成"飞书风格"。

用法：
  python3 scripts/sync_feishu_wiki.py                 # 推送（主线）
  python3 scripts/sync_feishu_wiki.py --include-spinoff
  python3 scripts/sync_feishu_wiki.py --pull          # 拉回（写入工作区）
  python3 scripts/sync_feishu_wiki.py --pull --changed-list /tmp/changed.txt
  python3 scripts/sync_feishu_wiki.py --dry-run

环境变量：LARK_BIN / LARK_PROFILE / FEISHU_SPACE_ID / FEISHU_CONTAINER
"""
import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPACE_ID = os.environ.get("FEISHU_SPACE_ID", "7692783315471846383")
CONTAINER = os.environ.get("FEISHU_CONTAINER", "XBgZw3UvBiH8AOkXpH9cQYVjnkf")
SPINOFF_TITLE = "番外"
LARK = os.environ.get("LARK_BIN", "lark-cli")
PROFILE = os.environ.get("LARK_PROFILE", "n8n-cli")
STATE_PATH = os.path.join(ROOT, "scripts", "feishu_wiki_state.json")

MAINLINE_TITLES = {
    "三更道场_第零期_缘起":   "第零期 · 缘起 · 借你一双慧眼",
    "三更道场_第一期_丹":     "第一期 · 道名 · 丹 ♈",
    "三更道场_第二期_哗":     "第二期 · 道名 · 哗 ♉",
    "三更道场_第三期_瑟":     "第三期 · 道名 · 瑟 ♊",
    "三更道场_第四期_玺":     "第四期 · 石头 · 玺 ♋",
    "三更道场_第五期_陨":     "第五期 · 石头 · 陨 ♌",
    "三更道场_第六期_翡":     "第六期 · 石头 · 翡 ♍",
    "三更道场_第七期_血酬":   "第七期 · 双约 · 血酬 ♎",
    "三更道场_第八期_铁幕":   "第八期 · 双约 · 铁幕 ♏",
    "三更道场_第八期半_天权": "第八期半 · 天权 · 银道 ⛎",
    "三更道场_第九期_回音":   "第九期 · 双约 · 回音 ♐",
    "三更道场_第十期_割席":   "第十期 · 列王 · 割席 ♑",
    "三更道场_第十一期_筑基": "第十一期 · 列王 · 筑基 ♒",
    "三更道场_第十二期_黄道": "第十二期 · 列王 · 黄道 ♓",
    "三更道场_尾声":         "尾声 · 闭门复盘 ⭕",
}


def lark(args):
    p = subprocess.run([LARK, "--profile", PROFILE, *args, "--as", "user", "--format", "json"],
                       cwd=ROOT, capture_output=True, text=True)
    try:
        d = json.loads(p.stdout.strip())
    except Exception:
        raise RuntimeError(f"lark-cli 非 JSON 输出: {p.stdout[:200]} {p.stderr[:200]}")
    if not d.get("ok"):
        raise RuntimeError(f"lark-cli 失败: {json.dumps(d.get('error', {}), ensure_ascii=False)[:300]}")
    return d.get("data") if isinstance(d.get("data"), dict) else d


def doc_revision(obj_token):
    """取飞书文档当前 revision_id（轻量，不拉正文）。"""
    if not obj_token:
        return None
    try:
        d = lark(["api", "GET", f"/open-apis/docx/v1/documents/{obj_token}"])
        doc = (d.get("document") if isinstance(d, dict) else None) or \
              ((d.get("data") or {}).get("document") if isinstance(d, dict) else None) or {}
        return doc.get("revision_id")
    except Exception as e:
        print(f"  [warn] revision 取失败 {obj_token}: {e}")
        return None


def fetch_markdown(node_token):
    d = lark(["docs", "+fetch", "--doc", node_token, "--doc-format", "markdown"])
    doc = (d.get("document") if isinstance(d, dict) else None) or {}
    return doc.get("content", ""), doc.get("revision_id")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    return sha256_bytes(open(path, "rb").read())


def children(parent_token):
    out, token = {}, None
    while True:
        params = {"parent_node_token": parent_token, "page_size": 50}
        if token:
            params["page_token"] = token
        data = lark(["api", "GET", f"/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes",
                     "--params", json.dumps(params)])
        items = (data.get("items") if isinstance(data, dict) else None) \
            or (data.get("data", {}) or {}).get("items") or []
        for it in items:
            out[it.get("title")] = it.get("node_token")
        if not data.get("has_more"):
            break
        token = data.get("page_token")
        if not token:
            break
    return out


def ensure_dir_node(parent_token, title, cache):
    key = (parent_token, title)
    if key in cache:
        return cache[key]
    kids = children(parent_token)
    node = kids.get(title)
    if not node:
        data = lark(["wiki", "+node-create", "--space-id", SPACE_ID,
                     "--parent-node-token", parent_token, "--title", title])
        node = data.get("node_token")
        print(f"[dir ] + {title} -> {node}")
    cache[key] = node
    return node


def collect(include_spinoff):
    items = []
    for f in sorted(glob.glob(os.path.join(ROOT, "docs", "三更道场_*正稿_普通话版.md"))):
        stem = os.path.splitext(os.path.basename(f))[0]
        if "前传" in stem:
            continue
        key = stem[:-len("_正稿_普通话版")] if stem.endswith("_正稿_普通话版") else stem
        items.append((os.path.relpath(f, ROOT), MAINLINE_TITLES.get(key, stem), None))
    if include_spinoff:
        for f in sorted(glob.glob(os.path.join(ROOT, "docs", "spinoff_*", "**", "*.md"), recursive=True)):
            series = os.path.basename(os.path.dirname(f))
            stem = os.path.splitext(os.path.basename(f))[0]
            items.append((os.path.relpath(f, ROOT), f"{series}｜{stem}", series))
    return items


def load_state():
    return json.load(open(STATE_PATH, encoding="utf-8")) if os.path.exists(STATE_PATH) else {}


def save_state(state):
    json.dump(state, open(STATE_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def do_push(args):
    state = load_state()
    dir_cache = {}
    spinoff_root = None
    if args.include_spinoff and not args.dry_run:
        spinoff_root = ensure_dir_node(CONTAINER, SPINOFF_TITLE, dir_cache)

    seen_sha, created, updated, skipped = {}, 0, 0, 0
    for rel, title, series in collect(args.include_spinoff):
        digest = sha256_file(os.path.join(ROOT, rel))
        if digest in seen_sha:
            skipped += 1
            continue
        seen_sha[digest] = rel
        entry = state.get(rel, {})
        node, obj = entry.get("node_token"), entry.get("obj_token")

        if entry.get("sha256") == digest and node:
            skipped += 1
            continue
        if entry.get("revision_id") and doc_revision(obj) != entry.get("revision_id"):
            # 飞书端也变了 → 飞书优先，本轮不推（交给 pull）
            print(f"[hold] {title}（飞书已改，飞书优先，等 pull）")
            skipped += 1
            continue
        if args.dry_run:
            print(f"[plan] {'update' if node else 'create'} {title}")
            continue

        if node:
            lark(["docs", "+update", "--doc", node, "--command", "overwrite",
                  "--doc-format", "markdown", "--content", f"@{rel}"])
            updated += 1
        else:
            parent = ensure_dir_node(spinoff_root, series, dir_cache) if series else CONTAINER
            data = lark(["docs", "+create", "--doc-format", "markdown",
                         "--title", title, "--content", f"@{rel}"])
            obj = (data.get("document") or {}).get("document_id")
            mv = lark(["wiki", "+move", "--obj-type", "docx", "--obj-token", obj,
                       "--target-space-id", SPACE_ID, "--target-parent-token", parent])
            node = mv.get("node_token")
            created += 1
        print(f"[{'upd ' if entry else 'new '}] {title}")
        state[rel] = {"title": title, "node_token": node, "obj_token": obj,
                      "sha256": digest, "revision_id": doc_revision(obj)}
        save_state(state)
    print(f"\npush 完成：新增 {created} / 更新 {updated} / 跳过 {skipped}")


def do_pull(args):
    state = load_state()
    changed = []
    for rel, entry in sorted(state.items()):
        node, obj = entry.get("node_token"), entry.get("obj_token")
        if not node:
            continue
        rev = doc_revision(obj)
        if rev is None or rev == entry.get("revision_id"):
            continue
        md, new_rev = fetch_markdown(node)
        if not md.strip():
            print(f"[warn] {rel} 拉回为空，跳过")
            continue
        path = os.path.join(ROOT, rel)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if md == old:
            entry["revision_id"] = new_rev or rev
            save_state(state)
            continue
        changed.append(rel)
        print(f"[pull] {rel}  (rev {entry.get('revision_id')} -> {new_rev or rev})")
        if not args.dry_run:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(md)
            entry["sha256"] = sha256_bytes(md.encode("utf-8"))
            entry["revision_id"] = new_rev or rev
            save_state(state)
    if args.changed_list:
        open(args.changed_list, "w", encoding="utf-8").write("\n".join(changed) + ("\n" if changed else ""))
    print(f"\npull 完成：仓库侧改动 {len(changed)} 篇")
    return 0


def do_baseline(args):
    """只记录当前飞书 revision 作为基线，不拉正文。
    用途：首次启用 pull 时，避免把"我们自己刚推上去的内容"当成外部改动全量拉回。"""
    state = load_state()
    n = 0
    for rel, entry in sorted(state.items()):
        obj = entry.get("obj_token")
        if not obj and entry.get("node_token"):
            # 早期手工导入的条目没记 obj_token，从 wiki 节点补回来
            try:
                d = lark(["wiki", "+node-get", "--node-token", entry["node_token"]])
                obj = d.get("obj_token")
                if obj and not args.dry_run:
                    entry["obj_token"] = obj
            except Exception as e:
                print(f"[warn] {rel} 取 obj_token 失败: {e}")
        if not obj:
            continue
        rev = doc_revision(obj)
        if rev is not None and rev != entry.get("revision_id"):
            print(f"[base] {rel}: revision -> {rev}")
            if not args.dry_run:
                entry["revision_id"] = rev
                save_state(state)
            n += 1
    print(f"\nbaseline 完成：{n} 条更新 revision")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-spinoff", action="store_true")
    ap.add_argument("--pull", action="store_true", help="飞书 → 仓库")
    ap.add_argument("--baseline", action="store_true", help="只记 revision 基线，不拉正文")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--changed-list", default=None, help="把拉回改动的文件清单写到此路径")
    args = ap.parse_args()
    if args.baseline:
        return do_baseline(args)
    if args.pull:
        return do_pull(args)
    return do_push(args)


if __name__ == "__main__":
    sys.exit(main())
