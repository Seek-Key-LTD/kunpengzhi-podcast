#!/usr/bin/env python3
"""把仓库文字稿同步到飞书知识库（repo → Feishu wiki）。

- 目标：公开知识库 space_id=7692783315471846383。
- 结构：容器「三更道场 · 文字稿」
            ├─ 主线正稿（15 篇）
            └─「番外」
                 └─「<系列>」
                       └─ 该系列文稿
- 手段：调用本机 lark-cli 的用户身份（公开知识库应用 tenant 写不进去）。
- 幂等：按标题对账；sha256 未变则跳过；已存在则 `docs +update --command overwrite`，否则 `docs +create` + `wiki +move`。
- 状态：scripts/feishu_wiki_state.json（rel_path -> {title,node_token,obj_token,sha256}）。

用法：
    python3 scripts/sync_feishu_wiki.py                    # 主线
    python3 scripts/sync_feishu_wiki.py --include-spinoff  # 主线 + 番外
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


def children(parent_token):
    """parent 下子节点：title -> node_token（分页，page_size 上限 50）。"""
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
    """确保 parent 下存在名为 title 的容器节点，返回其 node_token。"""
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


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def collect(include_spinoff):
    """返回 [(rel_path, title, parent_resolver)]；parent_resolver 只有番外需要。"""
    items = []
    for f in sorted(glob.glob(os.path.join(ROOT, "docs", "三更道场_*正稿_普通话版.md"))):
        stem = os.path.splitext(os.path.basename(f))[0]
        if "前传" in stem:      # 与「第零期」字节相同，只保留第零期
            continue
        key = stem[:-len("_正稿_普通话版")] if stem.endswith("_正稿_普通话版") else stem
        items.append((os.path.relpath(f, ROOT), MAINLINE_TITLES.get(key, stem), None))
    if include_spinoff:
        for f in sorted(glob.glob(os.path.join(ROOT, "docs", "spinoff_*", "**", "*.md"), recursive=True)):
            series = os.path.basename(os.path.dirname(f))
            stem = os.path.splitext(os.path.basename(f))[0]
            rel = os.path.relpath(f, ROOT)
            items.append((rel, f"{series}｜{stem}", series))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-spinoff", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state = json.load(open(STATE_PATH, encoding="utf-8")) if os.path.exists(STATE_PATH) else {}
    dir_cache = {}
    spinoff_root = None
    if args.include_spinoff and not args.dry_run:
        spinoff_root = ensure_dir_node(CONTAINER, SPINOFF_TITLE, dir_cache)

    seen_sha, created, updated, skipped = {}, 0, 0, 0
    for rel, title, series in collect(args.include_spinoff):
        digest = sha256(os.path.join(ROOT, rel))
        if digest in seen_sha:
            skipped += 1
            continue
        seen_sha[digest] = rel

        entry = state.get(rel, {})
        node = entry.get("node_token")

        if entry.get("sha256") == digest and node:
            skipped += 1
            continue

        if args.dry_run:
            print(f"[plan] {'update' if node else 'create'} {title}")
            continue

        if node:  # 已存在：整篇覆盖
            lark(["docs", "+update", "--doc", node, "--command", "overwrite",
                  "--doc-format", "markdown", "--content", f"@{rel}"])
            obj = entry.get("obj_token")
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

        state[rel] = {"title": title, "node_token": node, "obj_token": obj, "sha256": digest}
        json.dump(state, open(STATE_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"\n完成：新增 {created} / 更新 {updated} / 跳过 {skipped}")


if __name__ == "__main__":
    sys.exit(main())
