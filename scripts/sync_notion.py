#!/usr/bin/env python3
"""
Kunpengzhi Podcast -> Notion Auto Sync Script
Supports CI/CD workflow and local execution with incremental update support.
"""

import os
import sys
import time
import json
import urllib.request
import urllib.error

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "NOTION_TOKEN_FROM_VAULT")
PARENT_PAGE_ID = os.environ.get("NOTION_PARENT_PAGE_ID", "300c1384-f34d-8098-bbc4-d0902ac81d54")

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

EPISODES = [
    {"num": "S00", "title": "第零期 · 缘起 · 借你一双慧眼", "filename": "三更道场_第零期_缘起_正稿_普通话版.md", "volume": "总序幕", "theme": "创世纪·审查样带·人物谱系"},
    {"num": "S01", "title": "第一期 · 丹 · 辰砂之血与神权做账", "filename": "三更道场_第一期_丹_正稿_普通话版.md", "volume": "石头记", "theme": "辰砂·汞毒·巴寡妇清·神权财政"},
    {"num": "S02", "title": "第二期 · 哗 · 汉家制度与黄河大工", "filename": "三更道场_第二期_哗_正稿_普通话版.md", "volume": "石头记", "theme": "汉家制度·河工血酬·霸道王道"},
    {"num": "S03", "title": "第三期 · 瑟 · 绿松石与石国悬案", "filename": "三更道场_第三期_瑟_正稿_普通话版.md", "volume": "石头记", "theme": "高仙芝·石国·绿松石·中亚大崩盘"},
    {"num": "S04", "title": "第四期 · 玺 · 传国玉玺与受命之账", "filename": "三更道场_第四期_玺_正稿_普通话版.md", "volume": "石头记", "theme": "传国玉玺·受命于天·法统神话审计"},
    {"num": "S05", "title": "第五期 · 陨 · 天降星石与大灭绝纪元", "filename": "三更道场_第五期_陨_正稿_普通话版.md", "volume": "天权记", "theme": "新仙女木·陨石撞击·白令海峡·大洪水"},
    {"num": "S06", "title": "第六期 · 翡 · 昆仑玉路与西王母国", "filename": "三更道场_第六期_翡_正稿_普通话版.md", "volume": "石头记", "theme": "玉石之路·阿尔金山·青玉·早期全球化"},
    {"num": "S07", "title": "第七期 · 血酬 · 岁币对冲与澶渊之盟", "filename": "三更道场_第七期_血酬_正稿_普通话版.md", "volume": "双约记", "theme": "澶渊之盟·岁币博弈·宋辽地缘金融"},
    {"num": "S08", "title": "第八期 · 铁幕 · 雅尔塔与第一岛链", "filename": "三更道场_第八期_铁幕_正稿_普通话版.md", "volume": "双约记", "theme": "雅尔塔·旧金山和约·第一岛链·冷战条约法医"},
    {"num": "S08.5", "title": "第八期半 · 天权 · 深空第一因与引力弹弓", "filename": "三更道场_第八期半_天权_正稿_普通话版.md", "volume": "天权记", "theme": "木星引力·拉格朗日点·开普勒偏心率·深空第一因"},
    {"num": "S09", "title": "第九期 · 回音 · 莫高窟与藏经洞大账", "filename": "三更道场_第九期_回音_正稿_普通话版.md", "volume": "天权记", "theme": "敦煌文书·90万年大同古湖·瓦罕走廊大洪水"},
    {"num": "S10", "title": "第十期 · 割席 · 儒法之辨与道统重构", "filename": "三更道场_第十期_割席_正稿_普通话版.md", "volume": "道名记", "theme": "徐复观·熊十力·儒道分流·认识论断裂"},
    {"num": "S11", "title": "第十一期 · 筑基 · 印欧语东进与华夏发生学", "filename": "三更道场_第十一期_筑基_正稿_普通话版.md", "volume": "筑基篇", "theme": "吐火罗语·PIE构拟·白-沙上古音·大空间语言流形"},
    {"num": "S12", "title": "第十二期 · 黄道 · 二十八宿与华夏星图", "filename": "三更道场_第十二期_黄道_正稿_普通话版.md", "volume": "天权记", "theme": "天球四层星空·岁差·北斗秤学·华夏星空坐标"},
]

def notion_request(endpoint, method="POST", data=None):
    url = f"https://api.notion.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    
    for retry in range(5):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8")
            if e.code == 429:
                sleep_t = 2 ** retry
                print(f"[Notion Rate Limit 429] Backing off for {sleep_t}s...")
                time.sleep(sleep_t)
                continue
            print(f"[HTTP Error {e.code}] {endpoint}: {err_msg}")
            raise
        except Exception as e:
            print(f"[Network Error] {e}, retrying...")
            time.sleep(2)
    raise RuntimeError(f"Failed Notion request to {endpoint}")

def md_to_blocks(md_text):
    lines = md_text.split("\n")
    blocks = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Heading 1
        if line.startswith("# "):
            text = line[2:].strip()
            if text:
                blocks.append({
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
                })
        # Heading 2
        elif line.startswith("## "):
            text = line[3:].strip()
            if text:
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
                })
        # Heading 3 / 4 / 5
        elif line.startswith("### ") or line.startswith("#### ") or line.startswith("##### "):
            text = line.lstrip("#").strip()
            if text:
                blocks.append({
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
                })
        # Callout / Quote
        elif line.startswith("> "):
            text = line[2:].strip()
            if text:
                blocks.append({
                    "object": "block",
                    "type": "quote",
                    "quote": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
                })
        # Divider
        elif line.strip() in ["---", "***", "___"]:
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        # Bullet list
        elif line.startswith("- ") or line.startswith("* "):
            text = line[2:].strip()
            if text:
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
                })
        # Numbered list
        elif len(line) > 2 and line[0].isdigit() and line[1:3] in [". ", ") "]:
            text = line[3:].strip()
            if text:
                blocks.append({
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
                })
        # Code block
        elif line.startswith("```"):
            lang = line[3:].strip() or "plain text"
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code_content = "\n".join(code_lines)[:2000]
            blocks.append({
                "object": "block",
                "type": "code",
                "code": {
                    "language": "markdown" if "md" in lang else "plain text",
                    "rich_text": [{"type": "text", "text": {"content": code_content}}]
                }
            })
        # Paragraph
        else:
            text = line.strip()
            if text:
                for chunk in [text[j:j+1900] for j in range(0, len(text), 1900)]:
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": [{"type": "text", "text": {"content": chunk}}]}
                    })
        i += 1
    return blocks

def append_blocks_chunked(block_id, blocks, chunk_size=80):
    for idx in range(0, len(blocks), chunk_size):
        chunk = blocks[idx:idx+chunk_size]
        notion_request(f"blocks/{block_id}/children", method="PATCH", data={"children": chunk})
        time.sleep(0.35)

def clear_block_children(block_id):
    """Delete existing children blocks before re-uploading updated content."""
    res = notion_request(f"blocks/{block_id}/children?page_size=100", method="GET")
    for b in res.get("results", []):
        try:
            notion_request(f"blocks/{b['id']}", method="DELETE")
            time.sleep(0.1)
        except Exception:
            pass

def find_existing_database(parent_page_id, title_keyword="《三更道场》正稿全集数据库"):
    res = notion_request(f"blocks/{parent_page_id}/children?page_size=100", method="GET")
    for item in res.get("results", []):
        if item.get("type") == "child_database":
            db_title = item.get("child_database", {}).get("title", "")
            if title_keyword in db_title:
                return item["id"]
    return None

def find_existing_page(parent_page_id, title_keyword):
    res = notion_request(f"blocks/{parent_page_id}/children?page_size=100", method="GET")
    for item in res.get("results", []):
        if item.get("type") == "child_page":
            page_title = item.get("child_page", {}).get("title", "")
            if title_keyword in page_title:
                return item["id"]
    return None

def query_db_pages(db_id):
    pages = {}
    res = notion_request(f"databases/{db_id}/query", method="POST", data={"page_size": 100})
    for page in res.get("results", []):
        title_prop = page.get("properties", {}).get("期次", {}).get("title", [])
        if title_prop:
            full_title = title_prop[0].get("text", {}).get("content", "")
            pages[full_title] = page["id"]
    return pages

def sync_all():
    print(f"[*] Starting Notion Sync for Kunpengzhi Podcast...")
    print(f"[*] Parent Page ID: {PARENT_PAGE_ID}")
    
    db_id = find_existing_database(PARENT_PAGE_ID)
    if not db_id:
        print("[+] Creating new Episodes Database...")
        db_payload = {
            "parent": {"type": "page_id", "page_id": PARENT_PAGE_ID},
            "title": [{"type": "text", "text": {"content": "📚《三更道场》正稿全集数据库（14卷）"}}],
            "icon": {"type": "emoji", "emoji": "🎙️"},
            "properties": {
                "期次": {"title": {}},
                "卷次": {
                    "select": {
                        "options": [
                            {"name": "总序幕", "color": "purple"},
                            {"name": "石头记", "color": "blue"},
                            {"name": "天权记", "color": "orange"},
                            {"name": "双约记", "color": "red"},
                            {"name": "道名记", "color": "green"},
                            {"name": "筑基篇", "color": "pink"}
                        ]
                    }
                },
                "核心主题": {"rich_text": {}},
                "状态": {
                    "select": {
                        "options": [
                            {"name": "定稿完全版", "color": "green"},
                            {"name": "审查样带", "color": "yellow"}
                        ]
                    }
                },
                "字数/规模": {"number": {}}
            }
        }
        db_res = notion_request("databases", method="POST", data=db_payload)
        db_id = db_res["id"]
        print(f"[+] Created Database: {db_id}")
    else:
        print(f"[*] Found existing Episodes Database: {db_id}")

    existing_pages = query_db_pages(db_id)

    # Sync Episodes
    for item in EPISODES:
        file_path = os.path.join(DOCS_DIR, item["filename"])
        if not os.path.exists(file_path):
            print(f"[-] File missing: {file_path}")
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        char_count = len(content)
        title_key = f"[{item['num']}] {item['title']}"
        print(f"--> Syncing {title_key} ({char_count} chars)...")
        
        if title_key in existing_pages:
            page_id = existing_pages[title_key]
            # Update metadata
            notion_request(f"pages/{page_id}", method="PATCH", data={
                "properties": {
                    "字数/规模": {"number": char_count},
                    "核心主题": {"rich_text": [{"type": "text", "text": {"content": item["theme"]}}]}
                }
            })
            # Refresh content
            clear_block_children(page_id)
        else:
            page_payload = {
                "parent": {"database_id": db_id},
                "icon": {"type": "emoji", "emoji": "📜"},
                "properties": {
                    "期次": {"title": [{"type": "text", "text": {"content": title_key}}]},
                    "卷次": {"select": {"name": item["volume"]}},
                    "核心主题": {"rich_text": [{"type": "text", "text": {"content": item["theme"]}}]},
                    "状态": {"select": {"name": "定稿完全版"}},
                    "字数/规模": {"number": char_count}
                }
            }
            page_res = notion_request("pages", method="POST", data=page_payload)
            page_id = page_res["id"]
        
        blocks = md_to_blocks(content)
        append_blocks_chunked(page_id, blocks, chunk_size=80)
        print(f"    [OK] {item['num']} Synced!")

    # Sync Character Assets
    char_file = os.path.join(DOCS_DIR, "五卷人物资产_v1.md")
    if os.path.exists(char_file):
        print("\n--> Syncing Character Assets...")
        with open(char_file, "r", encoding="utf-8") as f:
            char_content = f.read()
        
        char_page_id = find_existing_page(PARENT_PAGE_ID, "《三更道场》人物资产与学者全谱系")
        if char_page_id:
            clear_block_children(char_page_id)
        else:
            char_page_payload = {
                "parent": {"type": "page_id", "page_id": PARENT_PAGE_ID},
                "icon": {"type": "emoji", "emoji": "👥"},
                "properties": {
                    "title": [{"type": "text", "text": {"content": "👥《三更道场》人物资产与学者全谱系（定稿资产库）"}}]
                }
            }
            char_res = notion_request("pages", method="POST", data=char_page_payload)
            char_page_id = char_res["id"]
        
        char_blocks = md_to_blocks(char_content)
        append_blocks_chunked(char_page_id, char_blocks, chunk_size=80)
        print("    [OK] Character Assets Synced!")

    print("\n[SUCCESS] Notion synchronization complete!")

if __name__ == "__main__":
    sync_all()
