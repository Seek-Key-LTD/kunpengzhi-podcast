#!/usr/bin/env bash
#
# 把 main 的「文稿投影」同步到同仓 orphan 快照分支 manuscripts。
#
# 投影集（保留原相对路径）：
#   docs/三更道场_*正稿_普通话版.md   主线正稿
#   docs/spinoff_*/**                 番外文稿（整目录）
# 不含 content/（canon 发布版不入分支）。
#
# 语义：orphan 分支无 main 历史；每次同步只追加一条增量提交；无变化则空跑退出。
#
# 环境变量：
#   GIT_TOKEN            必需。Gitea HTTPS oauth2 token（Actions 里传 secrets.GITHUB_TOKEN）
#   MANUSCRIPTS_BRANCH   可选，默认 manuscripts
#   GITEA_HOST           可选，默认 gitea.capitaltrain.cn
#   REPO                 可选，默认 kunpengzhi-podcast
#   GITEA_OWNER          可选，默认 seekkey
#   GITHUB_ENV           可选。存在则写出 NO_CHANGE/COMMIT_SHA/CHANGED_COUNT
#
set -euo pipefail

REPO="${REPO:-kunpengzhi-podcast}"
GITEA_OWNER="${GITEA_OWNER:-seekkey}"
GITEA_HOST="${GITEA_HOST:-gitea.capitaltrain.cn}"
BRANCH="${MANUSCRIPTS_BRANCH:-manuscripts}"
WORK="${WORK:-/var/tmp/manuscripts-sync/$REPO}"

: "${GIT_TOKEN:?GIT_TOKEN is required}"

env_out() {
  # 本地 dry-run 时 GITHUB_ENV 可能不存在，静默跳过即可。
  if [ -n "${GITHUB_ENV:-}" ] && [ -w "${GITHUB_ENV}" ]; then
    echo "$1" >> "$GITHUB_ENV"
  fi
  echo "[out] $1"
}

REMOTE_URL="${REMOTE_URL:-https://oauth2:$GIT_TOKEN@$GITEA_HOST/$GITEA_OWNER/$REPO.git}"

echo "==> clone $GITEA_OWNER/$REPO (main)"
rm -rf "$WORK"
mkdir -p "$(dirname "$WORK")"
git clone --quiet "$REMOTE_URL" "$WORK"
cd "$WORK"
# 中文路径不要转义成八进制，便于通知里直接可读
git config core.quotePath false

SHORT_SHA="$(git rev-parse --short HEAD)"
echo "==> main @ $SHORT_SHA"

# 1. 从 main 工作区构建投影暂存目录（保留原相对路径）
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/docs"

find docs -maxdepth 1 -type f -name '三更道场_*正稿_普通话版.md' -exec cp -p {} "$STAGE/docs/" \;
for d in docs/spinoff_*; do
  [ -d "$d" ] && cp -Rp "$d" "$STAGE/docs/"
done

echo "==> projection: $(find "$STAGE" -type f | wc -l | tr -d ' ') files"

# 2. 取现存的 manuscripts 分支；不存在则建 orphan（无 main 历史）
if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  echo "==> branch $BRANCH exists, continue incrementally"
  git fetch --quiet origin "$BRANCH"
  git checkout --quiet -B "$BRANCH" "origin/$BRANCH"
else
  echo "==> branch $BRANCH missing, bootstrap orphan"
  git checkout --quiet --orphan "$BRANCH"
  git rm -rf --quiet --cached . >/dev/null 2>&1 || true
fi

# 3. 清空工作区（仅保留 .git），灌入投影
find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -Rp "$STAGE"/. ./

# 4. 有变化才提交推送（幂等）。orphan 首提交没有 HEAD，需避开 diff 对 HEAD 的依赖。
HAS_HEAD=0
git rev-parse --verify -q HEAD >/dev/null 2>&1 && HAS_HEAD=1

git add -A

if [ "$HAS_HEAD" = 1 ] && git diff --cached --quiet; then
  echo "==> no change, skip"
  env_out "NO_CHANGE=1"
  exit 0
fi

if [ "$HAS_HEAD" = 1 ]; then
  CHANGED_LIST="$(git diff --cached --name-only)"
else
  CHANGED_LIST="$(git ls-files --cached)"
fi
CHANGED_COUNT="$(printf '%s\n' "$CHANGED_LIST" | sed '/^$/d' | wc -l | tr -d ' ')"

git -c user.name='manuscripts-bot' -c user.email='ci@capitaltrain.cn' \
  commit --quiet -m "manuscripts: sync from main@$SHORT_SHA ($CHANGED_COUNT files)"
git push --quiet origin "$BRANCH"

COMMIT_SHA="$(git rev-parse HEAD)"
echo "==> pushed $BRANCH @ ${COMMIT_SHA:0:7} ($CHANGED_COUNT files)"

printf '%s\n' "$CHANGED_LIST" | sed '/^$/d' | head -50 > "${CHANGED_FILE:-/tmp/manuscripts_changed.txt}"

env_out "NO_CHANGE=0"
env_out "COMMIT_SHA=$COMMIT_SHA"
env_out "CHANGED_COUNT=$CHANGED_COUNT"
