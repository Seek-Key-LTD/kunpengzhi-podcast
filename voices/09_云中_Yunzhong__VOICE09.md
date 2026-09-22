---
cast_order: 09
voice_asset_id: "VOICE_09"
codename: "云中"
legal_name: "云久元"
status: "voice_floor_pending_audition"
physical_master: "file:///home/ben/Music/voice_assets/yunzhong/base.wav"
f0_target: "165Hz-180Hz（《五卷》表B）"
pipeline: "E1 OmniVoice · Voice Design · 男·中年·陕西话·中音调 · speed 0.95（无 seed ⇒ 不可同人重跑，P-01/P-16）"
transmission_channel: "Feishu DSP (MCU)"
---

# 云中 (Yunzhong) · 声音资产与生成档案

> **“五百四十年前，达延汗重整蒙古六万户的时候，土默特万户的战旗就在大同城外。这阴山脚下的九运大账，咱们今晚当着天下人拆开算。”**  
> **“善化寺的斗栱为什么这么结实？因为那是北魏、辽金与大明三代人在刀尖上磨出来的物理榫卯。”**

---

## 一、人物身份与声学设定

- **法定真名/身份**：**云久元**（圈内尊称“云老 / 解教授”），54岁。大同大学古建工程与边塞史教授，大同云冈与九边长城坐地户。
- **大名与宗族密码**：
  - **姓氏【云】**：古阿尔泰语 `Bayan`（巴依/白银/白云鄂博），土默特万户（`Tümen`）贵胄汉化世家大姓。
  - **名【久元】**：取三元九运五百四十年大周期（9 × 60 = 540年）。540 年前正是成化年间达延汗重整土默特万户、北元中兴之际；一纪一元，看尽大明、北元到今日的长城互市沧桑。
- **地理暗线**：
  - 古云中郡、北魏平城、明代大同府。九边重镇第一防线，华严寺善化寺辽金巨构。
- **声学形态**：
  - **核心语态**：**晋北/大同方言底色官话（沉郁苍凉，咬字重如落锤，自带平城黄土与辽金木石的顿挫感）**。
  - **基频目标（F0）**：**125Hz ~ 145Hz**（干硬结实、沧桑稳健的中年学者音）。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/yunzhong/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/yunzhong.json` ＋《五卷人物资产总册》声纹人设 表A/表B。

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **09 云中**（云久元（法定真名 · 大同大学古建工程教授 · 54岁）） | ✅ |
| engine／mode | **OmniVoice（E1）／Voice Design** | ✅ |
| instruct（逐字） | 男，中年，陕西话，中音调 | ✅ |
| speed | 0.95 | ✅ |
| 探针台词（全员同句） | 这笔账我核了三十年。没有出处的话，我一个字都不给播。 | ✅ |
| 传输链路 | 远程位 —— 飞书 MCU 窄带链（300/3200Hz 截断＋粉红噪底＋50Hz 嗡鸣）。⚠ 本声底件是**干音**：传输 DSP 在总装层挂，不进声底层（否则母带被 DSP 焊死，换链路就得重抽声底）。 | ✅ |
| post_dsp | 无（干音直出） |
| 实测 | 5.33s ／ F0 中位 **171.4Hz** ／ IQR 151–205Hz ／ <250Hz 占比 16.3% | ✅ |
| F0 目标带（表B） | 165–180Hz ➔ ✅ 落带内 | ✅ |
| SHA-256 | `b7a815548c008ba55853faa73781f24ebc854385318bbbfc24b794760d19af01` | ✅ |
| 可复现性 | ❌ 声纹级不可（Design 无 seed，P-01）／❌ take 级不可／✅ 环境级（systemd 常驻 :9098） | ✅ |
| 状态 | 待主理人耳朵终审；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- `单方言无音调_20260922/` —— 判废原因：instruct 只女方言、未叠音调档，违反《五卷》声纹人设表 E1 硬门（须 音调＋方言 双件，否则 F0 不可控·坑账 P-05）。改判时间 2026-09-22，非 rm，留此备查。

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `yunzhong_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A/表B 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
