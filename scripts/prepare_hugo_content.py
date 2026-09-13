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
    print("🚀 Preparing Hugo content from docs and tasks...")

    # 1. Main canon docs
    for fname in sorted(os.listdir(DOCS_DIR)):
        fpath = os.path.join(DOCS_DIR, fname)
        if os.path.isfile(fpath) and fname.endswith(".md"):
            dest = os.path.join(CONTENT_DIR, "canon", fname)
            process_file(fpath, dest, "canon")
        elif os.path.isdir(fpath) and fname.startswith("spinoff_"):
            for sub_fname in sorted(os.listdir(fpath)):
                if sub_fname.endswith(".md"):
                    sub_fpath = os.path.join(fpath, sub_fname)
                    dest_fname = f"{fname}_{sub_fname}"
                    dest = os.path.join(CONTENT_DIR, "spinoff", dest_fname)
                    process_file(sub_fpath, dest, "spinoff")

    # 2. Tasks / Forensics
    if os.path.exists(TASKS_DIR):
        for fname in sorted(os.listdir(TASKS_DIR)):
            fpath = os.path.join(TASKS_DIR, fname)
            if os.path.isfile(fpath) and fname.endswith(".md"):
                dest = os.path.join(CONTENT_DIR, "tasks", fname)
                process_file(fpath, dest, "tasks")

    print("✔ Hugo content prepared successfully.")

if __name__ == "__main__":
    main()
