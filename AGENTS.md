# AGENTS · 鲲鹏志播客

## 🚨 碰声音资产：动手前必读坑账（一票否决项）

**`/home/ben/Projects/gitea/multipipeline-audio-render/docs/VOICE_PITFALL_LEDGER.md`**
配套工作纪律：`multipipeline-audio-render/AGENTS.md`；法统与引擎矩阵：`voices/README.md` §一·B；冻结库规矩：`~/Music/voice_assets/locked/README.md`。

四条硬约束（正文以坑账为准，此处仅是入口）：

1. **驱动器只有三个**（`audition.py` / `make_seed.py` / `asr_ref_text.py`），角色差异只写在 `characters/<id>.json`，**不为单个角色写 Python**。
2. **一人一条声底件（P-16）**：六格制度已废止（E1/E2 无 seed 通道，连抽必换脸；E2 clone 通道又不收 instruct）。**Voice Design 仍只准选型**，产出的是待终审的声底件，不是冻结资产；**E1 speaker 不在 `/speakers` 会静默回落 Design**，调用必带预检。
3. **引擎参数唯一来源＝《五卷人物资产总册》表A／表B**（`content/special/`）：`instruct`、`speed`、F0 目标带以表为准，改表必同步改角色卡。E1 `instruct` 是闭词表＋硬门（音调档与方言档须双件齐全），形容词写进去直接 500。
4. **音频目录禁 `rm`**；`locked/` 入仓即冻结；**耳朵是唯一验收终端**（F0／低频占比／声纹余弦都只是粗筛代理，P-07/P-15）。

<!-- OPENWIKI:START -->

## OpenWiki

This repository has a generated `openwiki/` evidence index. It is optional just-in-time context, not required startup reading.

- Treat source code and tests as authoritative. A brief's unknowns and review items are verification gaps, not automatic requirements.
- Prefer the narrowest quiet validation that proves the changed behavior. Preserve complete failure output.

The scheduled OpenWiki GitHub Actions workflow refreshes the repository wiki. Do not hand-edit generated OpenWiki pages unless explicitly asked; prefer updating source code/docs and letting OpenWiki regenerate.

<!-- OPENWIKI:END -->
