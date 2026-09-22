---
cast_order: 12
voice_asset_id: "VOICE_12"
codename: "敦煌"
legal_name: "黄拓石"
status: "voice_floor_pending_audition"
physical_master: "file:///home/ben/Music/voice_assets/dunhuang/base.wav"
f0_target: "不设目标带（P-19 自造·作废；P-20 说调≠声底）"
pipeline: "E1 OmniVoice · Voice Design · 男·老年·甘肃话·低音调 · speed 0.92（无 seed ⇒ 不可同人重跑，P-01/P-16）"
transmission_channel: "Feishu DSP (MCU)"
---

# 敦煌 (Dunhuang) · 声音资产与生成档案

> **“第四纪的黄土剖面和莫高窟的岩壁，就是一部写在西北大漠里的黄色石头记。你拿着地质锤敲下去，每一层都是地球的指纹。”**  
> **“黄拓石，一辈子在大风沙里敲石头、拓地层，看尽沧海桑田。”**

---

## 一、人物身份与声学设定

- **法定真名/身份**：**黄拓石**（圈内尊称“黄老 / 黄队长”），56岁。兰州大学地质科学与矿产资源学院资深教授、第四纪地质与莫高窟石刻金石学学术带头人。
- **大名与法统密码**：
  - **姓氏【黄】**：李四光第四纪地质学派；黄帝部族土德之黄；黄石纪（《石头记》之黄色托帕石 Topaz）。
  - **名【拓石】**：一辈子在西北大漠戈壁风沙里“敲岩芯、拓地层、拓石刻”的野外老勘探队员风骨；“拓”字亦暗扣托帕石（Topaz）之音，华夏文明地质信标。
- **家族血缘**：
  - 西北工业大学数学系怪兽**唐数敕**（酒泉）的嫡亲表哥。
- **声学形态**：
  - **核心语态**：**西北/兰州官话底色普通话（敦厚沉雄、风沙磨砺感、胸腔共振如大漠风声般开阔）**。
  - **基频目标（F0）**：**120Hz ~ 138Hz**（厚实如山、历尽沧桑的老一辈地质野外学家低音）。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/dunhuang/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/dunhuang.json` ＋《五卷人物资产总册》声纹人设 **表A（2026-08-30）**。（本档旧版引用的「表B」不存在，系我自造，坑账 P-19。）

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **12 敦煌**（黄拓石（法定真名 · 兰大地质与矿产学院教授 · 56岁）） | ✅ |
| engine／mode | **OmniVoice（E1）／Voice Design** | ✅ |
| instruct（逐字） | 男，老年，甘肃话，低音调 | ✅ |
| speed | 0.92 | ✅ |
| 台词（**对照句·非原文**）⚠ | 这笔账我核了三十年。没有出处的话，我一个字都不给播。 | ⚠ 见坑账 P-18 |
| 传输链路 | 远程位 —— 飞书 MCU 窄带链（300/3200Hz 截断＋粉红噪底＋50Hz 嗡鸣）。⚠ 本声底件是**干音**：传输 DSP 在总装层挂，不进声底层（否则母带被 DSP 焊死，换链路就得重抽声底）。 | ✅ |
| post_dsp | 无（干音直出） |
| 实测 | 5.52s ／ F0 中位 **152.4Hz** ／ IQR 129–188Hz ／ <250Hz 占比 32.7% | ✅ |
| F0 目标带 | **不存在**（原「表B」F0 列系我自造、无《五卷》出处，P-19 已作废；F0 中位测的是本句说调不是声底，P-20 取消达标判定） | ✅ |
| SHA-256 | `e47affb6ff2e1819f1e503b6e24d44fe6e186254080b3cba41e08a257d1cf3a5` | ✅ |
| 可复现性 | ❌ 声纹级不可（Design 无 seed，P-01）／❌ take 级不可／✅ 环境级（systemd 常驻 :9098） | ✅ |
| 状态 | 待主理人耳朵终审；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- 无

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `dunhuang_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
