# 贡献者指南 · 三更道场播客仓库

**许可证**: 本仓库所有内容（文稿、代码、配置）均采用 **GNU GPLv3** 授权。
提交即表示你同意将自己的贡献以相同许可证开放。

---

## 项目结构

```
kunpengzhi-podcast/
├── docs/                    # 播客文稿（Markdown）
│   ├── 三更道场_第X期_*.md  # 正稿（对话体）
│   └── ...
├── scripts/                 # 工具脚本
├── AGENTS.md                # Agent接口文档
├── CONTRIBUTING.md          # 本文件
└── LICENSE                  # GPLv3
```

## 贡献流程

### 1. Fork → Branch → PR

```bash
# Fork仓库到你自己的Gitea/GitHub账号
# 创建特性分支
git checkout -b feature/your-feature
# 提交
git commit -m "feat: 描述你的改动"
# 推送到你的fork
git push origin feature/your-feature
# 在Gitea/GitHub上发起Pull Request
```

### 2. 分支命名规范

| 前缀 | 用途 |
|---|---|
| `feature/` | 新功能、新文稿 |
| `fix/` | 修复错误 |
| `docs/` | 文档更新 |
| `ep{N}/` | 第N期播客相关改动 |

### 3. 文稿格式要求

- **文件编码**: UTF-8
- **换行符**: LF（非CRLF）
- **标题层级**: `#` = 期数标题, `##` = 幕标题, `###` = 小节
- **角色标注**: `**角色名**（方言/音色·身份）：`
- **证据标注**: `〔史〕` = 史料, `〔推〕` = 推演, `〔锤〕` = 实锤, `〔悬〕` = 悬疑, `〔账〕` = 账目

### 4. 提交信息规范

采用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
type(scope): 简短描述

详细描述（可选）
```

类型：`feat` / `fix` / `docs` / `style` / `refactor` / `test` / `chore`

示例：
```
feat(ep4): 新增幕八元曲符号过载章节
fix(ep3): 修正潮汐历法日期计算错误
docs: 更新CONTRIBUTING.md
```

### 5. 审核标准

- 至少 **1位维护者** 审核通过方可合并
- 涉及史实的改动需附 **参考文献来源**
- 涉及方言/音色的改动需说明 **发音依据**
- **字形物理决定论内容只能放在本仓库，不能推到kunpengzhi思想库**

---

## 内容红线

- **不碰宗教敏感词**（之前已踩过线，严格回避）
- **政治人物/在世人物不引用**
- **涉军话题严格考古限定**
- 播客版文稿中，**字形物理决定论假说仅限播客仓库**

## 许可证说明

GPLv3 的核心要求：
1. 你可以自由使用、修改、分发本仓库内容
2. 基于本仓库的衍生作品 **必须** 以相同许可证（GPLv3）发布
3. 必须保留原始版权声明和许可证
4. 修改必须标注

Markdown文稿视为代码（对CI/CD pipeline而言），因此GPLv3覆盖一切。

---

## 联系方式

- Gitea Issues: 提交issue讨论
- 维护者: houzhonglogic / jingminzhang / murenmark
