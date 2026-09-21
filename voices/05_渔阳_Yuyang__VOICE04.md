---
cast_order: 05
voice_asset_id: "VOICE_04"
codename: "渔阳"
legal_name: "于鲜洋"
status: "locked"
physical_master: "05_yuyang_渔阳.wav"
f0_target: "130Hz-150Hz"
pipeline: "Qwen3-TTS (Dylan 京普混流)"
transmission_channel: "Feishu DSP (MCU)"
---

# 渔阳 (Yuyang) · 声音资产与生成档案

> **“您内位甭跟我聊虚头巴脑的宏大叙事，把资产负债表一翻，谁在裸泳一目了然。”**  
> **“现代金融说白了就六个字：Debt is money（负债即货币）。死人欠的账，活人接着还！”**

---

## 一、人物身份与声学设定

- **法定真名/身份**：**于鲜洋**（圈内尊称“老于”），48岁。中央财经大学金融史教授、国家资产负债表与血酬制度总审计师。
- **大名寓意**：双关神笔——**“鱼羊为鲜，涉足大洋与金融大账”**！老北京胡同大爷的烟火气（鲜），混杂着练了三十年徐思众珠心算算穿天下国家资产负债表与大洋彼岸华尔街主权债务的冷酷。
- **地理暗线**：
  - 古渔阳郡（今北京密云/怀柔一带），“渔阳鼙鼓动地来”——王法翻覆与帝国大宗财政暗流。
  - 第三期（S03）起因乐山进山常驻三星堆，渔阳直接肉身常驻成都茶馆，与青衣、峨眉三足鼎立。
  - 专属衍生专栏：《雁栖唱晚》（怀柔/密云·当代国际金融审计与货币战争）。
- **声学形态**：
  - **核心语态**：**老北京京片子（地道儿化音、脆爽、四两拨千斤的胡同侃爷老辣感）**。
  - **跨语种能力**：国际金融前沿出身，能够极其自然、嘲讽地在京腔中嵌入**纯正美式金融英语**（Code-Switching），绝非机械生硬的假洋鬼子腔。
  - **基频目标（F0）**：**130Hz ~ 150Hz**（脆爽、机警、语速偏快的男性金融学者声）。

---

## 二、声学探索与生成工程

### 1. 从纯京味到“京腔金融双语流”
渔阳最难攻克的点在于：不仅北京腔要地道（儿化音自然），而且讲到 Wall Street、Debt-to-GDP、Token API 时不能降智。

### 2. 模型选型与 Qwen3 Dylan 引擎突破
- 在对比评测中，引入了 `Qwen3-TTS` 英文与多语种混流模型（代号 Dylan 架构），与 OmniVoice 京音底色深度融合，打通了中英无缝切换。
- **基准母带文件**：
  - [05_yuyang_渔阳.wav](file:///home/ben/Music/voice_assets/locked/05_yuyang_渔阳.wav)（总纲母带）
  - [yuyang_qwen3_dylan.wav](file:///home/ben/Music/voice_assets/locked/yuyang_qwen3_dylan.wav)（双语基线母带）
  - [yuyang_mixed_01_dead_people.wav](file:///home/ben/Music/voice_assets/locked/yuyang_mixed_01_dead_people.wav)（“死人借债”经典论述）
  - [yuyang_mixed_02_debt_as_money.wav](file:///home/ben/Music/voice_assets/locked/yuyang_mixed_02_debt_as_money.wav)（货币本质中英混搭）
  - [yuyang_mixed_03_token_api.wav](file:///home/ben/Music/voice_assets/locked/yuyang_mixed_03_token_api.wav)（赛博算力地租论述）
- **席位通道**：前两期挂飞书窄带传输；第三期起肉身常驻成都茶台，转为高保真大电容麦克风通道。
## 三、生成谱系 (Voice Genealogy) · 2026-09-21 补录

> **定版声底**：`05_yuyang_渔阳.wav` · 9.29s · SHA-256 `2e42cd58a2ea6ca76aaef…`；双语基线 `yuyang_qwen3_dylan.wav` · 15.20s
> **六合仓**：`~/Music/voice_assets/yuyang/` —— 当前 **0/6 格已落**。

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| engine | **Qwen3-TTS（Dylan 京普混流架构）** | ✅ |
| mode | **预置/外部音色直出**（OmniVoice 侧无 `yuyang` 种子） | ✅ |
| instruct | `null`（不经 OmniVoice 闭词表） | ✅ |
| ref_audio | **不可考** | ❌ |
| speed / seed | **不可考** | ❌ |
| post_dsp | **飞书 MCU 窄带链**：300Hz 以下／3200Hz 以上截断 + 粉红噪声 + 50Hz 嗡鸣（ep01–ep02；ep03 起转近场） | ⚠ 效果链本身未脚本化 |
| verdict | 2026-09-18 中英日四语适配盲测：`dylan_v1_scholarly`/`v2_fast_crisp`/`v3_husky_deep`/`v4_pitch_down` + `en_01..04` + `ja_01/02`，定 `mixed` 一路 | ⚠ 口述 |

### 谱系缺口（必读）

- **档案 `physical_master` 曾误写 `04_yuyang_渔阳.wav`**，实际冻结件为 `05_yuyang_渔阳.wav`（席位 05／声学号 VOICE_04 撞号事故）—— 2026-09-21 已改回，但**旧名不得再引用**。
- 引擎 `/speakers` **无“渔阳”**：本角色目前只能在 Qwen3-TTS 侧复现，OmniVoice 通道不可 clone。若要六格分装，须先按 README 谱系铁律用定版母带抽自有 seed。
- 实验场遗留 20 余条 `yuyang_*` 候选（含 `omnivoice_clone_en/mix`）从未归档 verdict，重跑前须先清账。
