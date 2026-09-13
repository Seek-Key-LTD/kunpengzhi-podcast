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
    os.makedirs(os.path.join(CONTENT_DIR, "spinoff"), exist_ok=True)
    os.makedirs(os.path.join(CONTENT_DIR, "tasks"), exist_ok=True)

def get_canon_weight(fname):
    if "第零期" in fname or "第0期" in fname:
        return 0
    if "第一期" in fname or "第1期" in fname:
        return 1
    if "第二期" in fname or "第2期" in fname:
        return 2
    if "第三期" in fname or "第3期" in fname:
        return 3
    if "第四期" in fname or "第4期" in fname:
        return 4
    if "第五期" in fname or "第5期" in fname:
        return 5
    if "第六期" in fname or "第6期" in fname:
        return 6
    if "第七期" in fname or "第7期" in fname:
        return 7
    if "第八期半" in fname:
        return 9
    if "第八期" in fname or "第8期" in fname:
        return 8
    if "第九期" in fname or "第9期" in fname:
        return 10
    if "第十期" in fname or "第10期" in fname:
        return 11
    if "第十一期" in fname or "第11期" in fname:
        return 12
    if "第十二期" in fname or "第12期" in fname:
        return 13
    if "尾声" in fname:
        return 99
    return 50

def clean_canon_title(raw_title):
    # Remove leading markdown #
    title = re.sub(r"^#+\s*", "", raw_title)
    # Remove 《三更道场》 or 三更道场 prefixes
    title = re.sub(r"^《?三更道场》?[\s·:：]*", "", title)
    # Clean up redundant positive text notes
    title = re.sub(r"（正稿.*?）", "", title)
    title = re.sub(r"正稿（.*?）", "", title)
    title = re.sub(r"\s*·\s*正稿.*$", "", title)
    title = re.sub(r"\s*正稿.*$", "", title)
    return title.strip(" ·:：-—")

def process_file(src_path, dest_path, section_name, weight=None):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

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
    print("🚀 Preparing Hugo content (Publishing Official Final Scripts with Name/Weight Alignment)...")

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
                weight = get_canon_weight(fname)
                files_to_process.append((weight, fname, fpath))
            else:
                print(f"  [Skip Draft/Internal] {fname}")

    # Sort numerically by weight ascending
    files_to_process.sort(key=lambda x: x[0])

    for weight, fname, fpath in files_to_process:
        dest = os.path.join(CONTENT_DIR, "canon", fname)
        process_file(fpath, dest, "canon", weight=weight)
        published_count += 1
        print(f"  [{weight:02d}] Published: {fname}")

    print(f"✔ Hugo content prepared: {published_count} official canon manuscripts published.")

if __name__ == "__main__":
    main()
