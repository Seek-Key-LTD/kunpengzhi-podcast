# AGENTS · 鲲鹏志播客

## 🚨 碰声音资产：动手前必读坑账（一票否决项）

**`/home/ben/Projects/gitea/multipipeline-audio-render/docs/VOICE_PITFALL_LEDGER.md`**
配套工作纪律：`multipipeline-audio-render/AGENTS.md`；法统与引擎矩阵：`voices/README.md` §一·B；冻结库规矩：`~/Music/voice_assets/locked/README.md`。

三条硬约束（正文以坑账为准，此处仅是入口）：

1. **驱动器只有三个**（`audition.py` / `make_seed.py` / `asr_ref_text.py`），角色差异只写在 `characters/<id>.json`，**不为单个角色写 Python**。
2. **Voice Design 只准选型、不准产六格**（E1 无 seed，连续调用必成不同人）；**E1 speaker 不在 `/speakers` 会静默回落 Design**，调用必带预检。
3. **音频目录禁 `rm`**；`locked/` 入仓即冻结；**耳朵是唯一验收终端**。

<!-- OPENWIKI:START -->

## OpenWiki

This repository has a generated `openwiki/` evidence index. It is optional just-in-time context, not required startup reading.

- Treat source code and tests as authoritative. A brief's unknowns and review items are verification gaps, not automatic requirements.
- Prefer the narrowest quiet validation that proves the changed behavior. Preserve complete failure output.

The scheduled OpenWiki GitHub Actions workflow refreshes the repository wiki. Do not hand-edit generated OpenWiki pages unless explicitly asked; prefer updating source code/docs and letting OpenWiki regenerate.

<!-- OPENWIKI:END -->
