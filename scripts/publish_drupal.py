#!/usr/bin/env python3
"""
ASN 智者专栏 ➔ Drupal CMS 自动化发布引擎
通过通配符映射匹配专栏目录、从 Vault 读取 Agent 凭据、以对应 Agent 身份获取 OAuth2 Token 并推入 Drupal。
"""

import os
import sys
import json
import re
import argparse
import subprocess
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

VAULT_ADDR = os.environ.get("VAULT_ADDR", "https://vault.capitaltrain.cn")
DRUPAL_BASE_URL = os.environ.get("DRUPAL_BASE_URL", "https://drupal.seekkey.eu.org")

# 专栏目录通配符映射表 (100% 对齐 docs/spinoff_* 与 Authentik/Drupal SSOT)
SPINOFF_TO_AGENT = {
    "spinoff_华严蒲牢": "carbonado",
    "spinoff_廊桥疑梦": "ruby",
    "spinoff_桃源格竹": "zhuyu",
    "spinoff_鱼尾狮吼": "violet",
    "spinoff_雁栖唱晚": "diamond",
    "spinoff_踹忑一角": "leopard",
    "spinoff_辛河酉阵": "tumi",
    "spinoff_青城刀客": "argentite",
    "spinoff_古蜀账房": "obsidian",
    "spinoff_红岩花媒": "murex",
    "spinoff_雨花道情": "azure",
    "spinoff_酒色财气": "agate",
    "spinoff_越秀风云": "topaz",
    "spinoff_龟蛇锁江": "quartz",
    "spinoff_湖海知否": "amber",
    "spinoff_灵隐行在": "luna",
    "spinoff_凉州丝玉": "topaz",
    "spinoff_关山出月": "moli",
    "spinoff_卢浮半夏": "muxu",
    "spinoff_天守藏经": "qiangwei",
}


def get_vault_token():
    """获取 Vault Token"""
    # 1. 环境变量
    if os.environ.get("VAULT_TOKEN"):
        return os.environ.get("VAULT_TOKEN")
    # 2. 系统 vault-agent 路径
    for path in ["/etc/vault-agent/token", os.path.expanduser("~/.vault-token")]:
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    tok = f.read().strip()
                    if tok:
                        return tok
            except Exception:
                pass
    return None


def get_agent_drupal_credentials(agent_name):
    """从 Vault 通配符路径 secret/data/dev/drupal/{agent_name} 获取凭据"""
    vault_token = get_vault_token()
    if not vault_token:
        raise RuntimeError("Vault Token not found in VAULT_TOKEN env or /etc/vault-agent/token")

    url = f"{VAULT_ADDR}/v1/secret/data/dev/drupal/{agent_name}"
    headers = {"X-Vault-Token": vault_token}
    resp = requests.get(url, headers=headers, verify=False, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to fetch Vault secret for {agent_name}: HTTP {resp.status_code} - {resp.text}")

    data = resp.json().get("data", {}).get("data", {})
    client_id = data.get("client_id")
    client_secret = data.get("client_secret")

    if not client_id or not client_secret:
        raise ValueError(f"client_id or client_secret missing in Vault for agent {agent_name}")

    return client_id, client_secret


def get_drupal_oauth_token(client_id, client_secret):
    """请求 Drupal 获取 OAuth2 Bearer Token (scope=columnist)"""
    url = f"{DRUPAL_BASE_URL}/oauth/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "columnist"
    }
    resp = requests.post(url, data=payload, verify=False, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to obtain Drupal OAuth token: HTTP {resp.status_code} - {resp.text}")

    token_data = resp.json()
    access_token = token_data.get("access_token")
    if not access_token:
        raise RuntimeError(f"access_token missing in response: {token_data}")

    return access_token


def parse_markdown_file(file_path):
    """解析 Markdown 文件，提取首行一级标题与正文"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    title = os.path.basename(file_path).replace(".md", "")
    body = content

    # 寻找首个一级标题
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            # 可以选择保留全部正文，也可以把首行剔除
            break

    return title, body


def publish_article_to_drupal(access_token, title, body_content):
    """通过 Drupal JSON:API 发布文章"""
    url = f"{DRUPAL_BASE_URL}/jsonapi/node/article"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/vnd.api+json",
        "Accept": "application/vnd.api+json"
    }

    # Drupal 文章发布 payload (采用 basic_html 或 full_html 格式，直接支持 Markdown 渲染)
    payload = {
        "data": {
            "type": "node--article",
            "attributes": {
                "title": title,
                "body": {
                    "value": body_content,
                    "format": "basic_html"
                }
            }
        }
    }

    resp = requests.post(url, headers=headers, json=payload, verify=False, timeout=20)
    if resp.status_code not in (200, 201):
        raise RuntimeError(f"Failed to publish article: HTTP {resp.status_code} - {resp.text}")

    resp_data = resp.json()
    article_id = resp_data.get("data", {}).get("id")
    nid = resp_data.get("data", {}).get("attributes", {}).get("drupal_internal__nid")
    return article_id, nid


def process_file(file_path):
    """处理单个 Markdown 文件的发布流程"""
    norm_path = os.path.normpath(file_path)
    parts = norm_path.split(os.sep)

    spinoff_dir = None
    for p in parts:
        if p.startswith("spinoff_"):
            spinoff_dir = p
            break

    if not spinoff_dir:
        print(f"[-] Skipping {file_path}: Not located in a spinoff_* directory.")
        return False

    agent = SPINOFF_TO_AGENT.get(spinoff_dir)
    if not agent:
        print(f"[-] Warning: No agent mapped for directory '{spinoff_dir}'. Skipping.")
        return False

    print(f"\n========================================================")
    print(f"[*] Dispatching: {file_path}")
    print(f"[*] Spinoff Dir: {spinoff_dir}")
    print(f"[*] Bound Agent: {agent}")
    print(f"========================================================")

    # 1. 读文件
    title, body = parse_markdown_file(file_path)
    print(f"[+] Title: {title}")

    # 2. 取凭据
    print(f"[+] Reading Vault credentials for '{agent}'...")
    client_id, client_secret = get_agent_drupal_credentials(agent)

    # 3. 换取 Token
    print(f"[+] Authenticating as '{client_id}' on Drupal OAuth2...")
    token = get_drupal_oauth_token(client_id, client_secret)

    # 4. 发布文章
    print(f"[+] Publishing article via Drupal JSON:API...")
    article_uuid, nid = publish_article_to_drupal(token, title, body)

    print(f"[✓] Successfully published!")
    print(f"    - UUID: {article_uuid}")
    print(f"    - Node ID: {nid}")
    print(f"    - Drupal URL: {DRUPAL_BASE_URL}/node/{nid}")
    return True


def get_git_diff_files():
    """获取本次 commit 变动的 markdown 文件"""
    try:
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
        output = subprocess.check_output(cmd, text=True)
        files = [line.strip() for line in output.splitlines() if line.strip().endswith(".md")]
        return files
    except Exception as e:
        print(f"[-] Warning: git diff failed ({e}), checking unstaged/staged files...")
        cmd = ["git", "status", "--porcelain"]
        output = subprocess.check_output(cmd, text=True)
        files = [line[3:].strip() for line in output.splitlines() if line[3:].strip().endswith(".md")]
        return files


def main():
    parser = argparse.ArgumentParser(description="ASN Spinoff ➔ Drupal Publisher")
    parser.add_argument("--file", help="Publish a specific markdown file")
    parser.add_argument("--spinoff", help="Publish all markdown files in a specific spinoff directory")
    parser.add_argument("--git-diff", action="store_true", help="Publish changed markdown files from git diff")

    args = parser.parse_args()

    if args.file:
        process_file(args.file)
    elif args.spinoff:
        dir_path = os.path.join("docs", args.spinoff)
        if not os.path.exists(dir_path):
            dir_path = args.spinoff
        if not os.path.exists(dir_path):
            print(f"Error: Directory {dir_path} not found.")
            sys.exit(1)
        files = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(".md")])
        print(f"Found {len(files)} markdown files in {dir_path}")
        for f in files:
            process_file(f)
    elif args.git_diff:
        files = get_git_diff_files()
        print(f"Git diff detected {len(files)} changed markdown files:")
        for f in files:
            print(f" - {f}")
        for f in files:
            process_file(f)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
