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

def process_file(src_path, dest_path, section_name):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract Title from first H1 or filename
    title = os.path.splitext(os.path.basename(src_path))[0]
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()

    title_safe = title.replace('"', '\\"')

    # If frontmatter doesn't exist, add it
    if not content.startswith("---"):
        frontmatter = f"""---
title: "{title_safe}"
date: 2026-09-13
draft: false
section: "{section_name}"
---

"""
        content = frontmatter + content

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    clean_and_make_dir()
    print("🚀 Preparing Hugo content (Publishing Official Final Scripts only)...")

    # 1. Main canon docs (Only official finalized manuscripts: *正稿*.md)
    published_count = 0
    for fname in sorted(os.listdir(DOCS_DIR)):
        fpath = os.path.join(DOCS_DIR, fname)
        if os.path.isfile(fpath) and fname.endswith(".md"):
            if "正稿" in fname:
                dest = os.path.join(CONTENT_DIR, "canon", fname)
                process_file(fpath, dest, "canon")
                published_count += 1
            else:
                # Non-finalized or internal notes remain draft
                print(f"  [Skip Draft/Internal] {fname}")

    print(f"✔ Hugo content prepared: {published_count} official canon manuscripts published.")

if __name__ == "__main__":
    main()
