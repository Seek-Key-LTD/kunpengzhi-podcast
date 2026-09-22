---
cast_order: 06
voice_asset_id: "VOICE_13"
codename: "珞珈"
legal_name: "落花生"
status: "voice_floor_pending_audition"
physical_master: "file:///home/ben/Music/voice_assets/luojia/base.wav"
f0_target: "170Hz-185Hz（《五卷》表B）"
pipeline: "E1 OmniVoice · Voice Design · 男·青年·石家庄话·中音调 · speed 1.0（无 seed ⇒ 不可同人重跑，P-01/P-16）"
transmission_channel: "Feishu DSP (MCU)"
---

# 珞珈 (Luojia) · 声音资产与生成档案

> **“落花有情，今为花生。当年为了留在东湖边，我放下了北京的所有机会。但这片楚地的泥土，养得活最硬的条约法医。”**  
> **“条约不是废纸，近代万国公法的每一个标点符号，背后都是几万万两白银的杀人刀。”**

---

## 一、人物身份与声学设定

- **法定真名/身份**：**落花生**（圈内尊称“老落 / 落老师”），42岁。武汉大学法学院副教授，国际公法、近代不平等条约与海关关税史法医级学者。
- **大名与音韵密码**：
  - **姓氏【落】（注音：Lào / 涝）**：古姓氏西戎/鲜卑汉化古音读去声“涝”，带鄂豫皖中原官话土腥味与宗族底蕴。
  - **名【花生】**：**“落花有情，今为花生”**。黄冈做题家出身，为了心爱的姑娘执拗留在武汉珞珈山；像落花生一样深扎泥土，地底结实，不求显达体面，唯求实证经世。
- **声学形态**：
  - **核心语态**：**楚地/鄂东黄冈官话底色普通话（语速偏快、咬字极为尖锐缜密、逻辑推演如外科手术刀般见血）**。
  - **基频目标（F0）**：**135Hz ~ 150Hz**（机敏、专注、克制且充满内劲的中年法学家中音）。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/luojia/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/luojia.json` ＋《五卷人物资产总册》声纹人设 表A/表B。

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **06 珞珈**（落花生（法定真名 · 落读 Lào · 武大法学院副教授 · 42岁）） | ✅ |
| engine／mode | **OmniVoice（E1）／Voice Design** | ✅ |
| instruct（逐字） | 男，青年，石家庄话，中音调 | ✅ |
| speed | 1.0 | ✅ |
| 探针台词（全员同句） | 这笔账我核了三十年。没有出处的话，我一个字都不给播。 | ✅ |
| 传输链路 | 远程位 —— 飞书 MCU 窄带链（300/3200Hz 截断＋粉红噪底＋50Hz 嗡鸣）。⚠ 本声底件是**干音**：传输 DSP 在总装层挂，不进声底层（否则母带被 DSP 焊死，换链路就得重抽声底）。 | ✅ |
| post_dsp | 无（干音直出） |
| 实测 | 4.81s ／ F0 中位 **177.8Hz** ／ IQR 148–209Hz ／ <250Hz 占比 11.3% | ✅ |
| F0 目标带（表B） | 170–185Hz ➔ ✅ 落带内 | ✅ |
| SHA-256 | `efe90677bd9929ce02fd8c72379eb458b6f4923ef1cad638c87f03fb3e3439af` | ✅ |
| 可复现性 | ❌ 声纹级不可（Design 无 seed，P-01）／❌ take 级不可／✅ 环境级（systemd 常驻 :9098） | ✅ |
| 状态 | 待主理人耳朵终审；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- `单方言无音调_20260922/` —— 判废原因：instruct 只女方言、未叠音调档，违反《五卷》声纹人设表 E1 硬门（须 音调＋方言 双件，否则 F0 不可控·坑账 P-05）。改判时间 2026-09-22，非 rm，留此备查。

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `luojia_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A/表B 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
