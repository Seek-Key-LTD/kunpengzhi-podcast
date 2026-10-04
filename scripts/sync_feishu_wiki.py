#!/usr/bin/env python3
"""把仓库文字稿同步到飞书知识库（repo → Feishu wiki）。

- 目标：公开知识库 space_id=7692783315471846383 下的容器节点「三更道场 · 文字稿」。
- 手段：调用本机 lark-cli（用户身份；公开知识库应用 tenant 写不进去）。
- 幂等：按标题对账；内容 sha256 未变则跳过；已存在则 `docs +update --command overwrite`，否则 `docs +create` + `wiki +move`。
- 状态：scripts/feishu_wiki_state.json（path -> {node_token,obj_token,sha256,title}）。

用法：
    python3 scripts/sync_feishu_wiki.py                 # 主线
    python3 scripts/sync_feishu_wiki.py --include-spinoff  # 主线 + 番外
    python3 scripts/sync_feishu_wiki.py --dry-run

环境变量：
    LARK_BIN       默认 lark-cli
    LARK_PROFILE   默认 n8n-cli（设备码授权拿到的用户 token）
    FEISHU_SPACE_ID / FEISHU_CONTAINER  覆盖默认空间/容器
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
CONTAINER_TITLE = "三更道场 · 文字稿"
LARK = os.environ.get("LARK_BIN", "lark-cli")
PROFILE = os.environ.get("LARK_PROFILE", "n8n-cli")
STATE_PATH = os.path.join(ROOT, "scripts", "feishu_wiki_state.json")

# 主线：文件名 stem -> 标题（与已入库的标题一致，保证按标题对账能命中）
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
    """调用 lark-cli，返回 data（失败抛异常）。"""
    p = subprocess.run(
        [LARK, "--profile", PROFILE, *args, "--as", "user", "--format", "json"],
        cwd=ROOT, capture_output=True, text=True)
    try:
        d = json.loads(p.stdout.strip())
    except Exception:
        raise RuntimeError(f"lark-cli 非 JSON 输出: {p.stdout[:200]} {p.stderr[:200]}")
    if not d.get("ok"):
        raise RuntimeError(f"lark-cli 失败: {json.dumps(d.get('error', {}), ensure_ascii=False)[:300]}")
    # 部分 shortcut 把结果放在顶层（无 data 包装）
    return d.get("data") if isinstance(d.get("data"), dict) else d


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def container_children():
    """列出容器下已有子节点：title -> node_token（分页，page_size 上限 50）。"""
    out, token = {}, None
    while True:
        params = {"parent_node_token": CONTAINER, "page_size": 50}
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


def collect_sources(include_spinoff):
    files = sorted(glob.glob(os.path.join(ROOT, "docs", "三更道场_*正稿_普通话版.md")))
    if include_spinoff:
        files += sorted(glob.glob(os.path.join(ROOT, "docs", "spinoff_*", "**", "*.md"), recursive=True))
    out = []
    for f in files:
        rel = os.path.relpath(f, ROOT)
        stem = os.path.splitext(os.path.basename(f))[0]
        # 「前传」与「第零期」字节相同，只保留第零期（与 prepare_hugo_content.py 一致）
        if "前传" in stem and os.path.basename(os.path.dirname(f)) == "docs":
            continue
        key = stem[:-len("_正稿_普通话版")] if stem.endswith("_正稿_普通话版") else stem
        if key in MAINLINE_TITLES:
            title = MAINLINE_TITLES[key]
        elif os.sep + "spinoff_" in f:
            series = os.path.basename(os.path.dirname(f))
            title = f"{series}｜{stem}"
        else:
            title = stem
        out.append((rel, title, f))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-spinoff", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state = {}
    if os.path.exists(STATE_PATH):
        state = json.load(open(STATE_PATH, encoding="utf-8"))

    by_title = container_children()
    print(f"容器已有 {len(by_title)} 个子节点")

    seen_sha = {}
    created = updated = skipped = 0
    for rel, title, path in collect_sources(args.include_spinoff):
        digest = sha256(path)
        if digest in seen_sha:
            print(f"[dup ] {title}（与 {seen_sha[digest]} 内容相同，跳过）")
            skipped += 1
            continue
        seen_sha[digest] = rel

        node = by_title.get(title) or (state.get(rel, {}) or {}).get("node_token")
        if state.get(rel, {}).get("sha256") == digest and node:
            print(f"[skip] {title}")
            skipped += 1
            continue

        if args.dry_run:
            print(f"[plan] {'update' if node else 'create'} {title}")
            continue

        if node:
            lark(["docs", "+update", "--doc", node, "--command", "overwrite",
                  "--doc-format", "markdown", "--content", f"@{rel}"])
            obj = state.get(rel, {}).get("obj_token")
            updated += 1
            print(f"[upd ] {title}")
        else:
            data = lark(["docs", "+create", "--doc-format", "markdown",
                         "--title", title, "--content", f"@{rel}"])
            doc_id = (data.get("document") or {}).get("document_id")
            mv = lark(["wiki", "+move", "--obj-type", "docx", "--obj-token", doc_id,
                       "--target-space-id", SPACE_ID, "--target-parent-token", CONTAINER])
            node = mv.get("node_token")
            obj = doc_id
            created += 1
            print(f"[new ] {title} node={node}")

        state[rel] = {"title": title, "node_token": node, "obj_token": obj, "sha256": digest}
        json.dump(state, open(STATE_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"\n完成：新增 {created} / 更新 {updated} / 跳过 {skipped}")


if __name__ == "__main__":
    sys.exit(main())
