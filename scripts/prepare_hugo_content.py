#!/usr/bin/env python3
import os
import shutil
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
TASKS_DIR = os.path.join(ROOT_DIR, "tasks_第二季工单池")
CONTENT_DIR = os.path.join(ROOT_DIR, "content")

def clean_and_make_dir():
    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
    os.makedirs(os.path.join(CONTENT_DIR, "canon"), exist_ok=True)
    os.makedirs(os.path.join(CONTENT_DIR, "special"), exist_ok=True)

CANON_MAP = {
    "第零期": {"weight": 1, "title": "第零期 · 缘起 · 借你一双慧眼"},
    "第一期": {"weight": 2, "title": "第一期 · 道名 · 丹 ♈"},
    "第二期": {"weight": 3, "title": "第二期 · 道名 · 哗 ♉"},
    "第三期": {"weight": 4, "title": "第三期 · 道名 · 瑟 ♊"},
    "第四期": {"weight": 5, "title": "第四期 · 石头 · 玺 ♋"},
    "第五期": {"weight": 6, "title": "第五期 · 石头 · 陨 ♌"},
    "第六期": {"weight": 7, "title": "第六期 · 石头 · 翡 ♍"},
    "第七期": {"weight": 8, "title": "第七期 · 双约 · 血酬 ♎"},
    "第八期_": {"weight": 9, "title": "第八期 · 双约 · 铁幕 ♏"},
    "第八期半": {"weight": 10, "title": "第八期半 · 天权 · 银道 ⛎"},
    "第九期": {"weight": 11, "title": "第九期 · 双约 · 回音 ♐"},
    "第十期": {"weight": 12, "title": "第十期 · 列王 · 割席 ♑"},
    "第十一期": {"weight": 13, "title": "第十一期 · 列王 · 筑基 ♒"},
    "第十二期": {"weight": 14, "title": "第十二期 · 列王 · 黄道 ♓"},
    "尾声": {"weight": 99, "title": "尾声 · 闭门复盘 ⭕"},
}

def get_canon_meta(fname):
    for key, meta in CANON_MAP.items():
        if key in fname:
            return meta["weight"], meta["title"]
    return 50, fname

def process_file(src_path, dest_path, section_name, weight=None, custom_title=None):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    if custom_title:
        title = custom_title
    else:
        # Extract Title from first H1 or filename
        raw_title = os.path.splitext(os.path.basename(src_path))[0]
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if h1_match:
            raw_title = h1_match.group(1).strip()
        title = clean_canon_title(raw_title)

    title_safe = title.replace('"', '\\"')
    weight_str = f"weight: {weight}\n" if weight is not None else ""

    # If frontmatter doesn't exist, add it
    if not content.startswith("---"):
        frontmatter = f"""---
title: "{title_safe}"
date: 2026-09-13
draft: false
section: "{section_name}"
{weight_str}---

"""
        content = frontmatter + content

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    clean_and_make_dir()
    print("🚀 Preparing Hugo content (Canon Scripts + Special Popout Assets)...")

    # 1. Main canon docs (Only official finalized manuscripts: *正稿*.md)
    published_count = 0
    files_to_process = []
    for fname in os.listdir(DOCS_DIR):
        fpath = os.path.join(DOCS_DIR, fname)
        if os.path.isfile(fpath) and fname.endswith(".md"):
            # Skip duplicate 前传 (which is byte-for-byte identical to 第零期)
            if "前传" in fname and any("第零期" in f for f in os.listdir(DOCS_DIR)):
                print(f"  [Skip Duplicate 前传] {fname}")
                continue
            if "正稿" in fname:
                weight, title = get_canon_meta(fname)
                files_to_process.append((weight, title, fname, fpath))
            else:
                print(f"  [Skip Draft/Internal] {fname}")

    # Sort numerically by weight ascending
    files_to_process.sort(key=lambda x: x[0])

    for weight, title, fname, fpath in files_to_process:
        dest = os.path.join(CONTENT_DIR, "canon", fname)
        process_file(fpath, dest, "canon", weight=weight, custom_title=title)
        published_count += 1
        print(f"  [{weight:02d}] Published Canon: {title}")

    # 2. Special Popout Assets: 人物资产图 & 诗词集
    persona_src = os.path.join(TASKS_DIR, "五卷人物资产_v1.md")
    if os.path.exists(persona_src):
        persona_dest = os.path.join(CONTENT_DIR, "special", "五卷人物资产总册.md")
        process_file(persona_src, persona_dest, "special", weight=1, custom_title="五卷人物资产总册 · 智者图谱与声纹档案")
        print("  [Special Popout] Published: 五卷人物资产总册 · 智者图谱与声纹档案")

    poem_src = os.path.join(ROOT_DIR, "三更书场", "第一场_第一季诗词歌赋集锦_普通话定稿.md")
    if os.path.exists(poem_src):
        poem_dest = os.path.join(CONTENT_DIR, "special", "第一季诗词歌赋集锦.md")
        process_file(poem_src, poem_dest, "special", weight=2, custom_title="第一季诗词歌赋集锦 · 定场散场全集与茶史五绝赋")
        print("  [Special Popout] Published: 第一季诗词歌赋集锦 · 定场散场全集与茶史五绝赋")

    print(f"✔ Hugo content prepared: {published_count} canon manuscripts + 2 special popout assets published.")

if __name__ == "__main__":
    main()
