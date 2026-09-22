---
cast_order: 05
voice_asset_id: "VOICE_04"
codename: "渔阳"
legal_name: "于鲜洋"
status: "locked"
physical_master: "yuyang_d4_base.wav"
f0_target: "125Hz-150Hz（d4 加厚后实测带）"
pipeline: "E2 Qwen3-TTS CustomVoice 1.7B (Dylan 京普混流) + DSP d4 加厚"
transmission_channel: "Feishu DSP (MCU)（干音入库，窄带链在总装层挂）"
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
  - **基频目标（F0）**：**125Hz ~ 150Hz**（d4 加厚后的实测带；E2 直出的裸 Dylan 在 131–170Hz 间乱跳，主理人判"像个 26 岁的孩子"，厚度由 DSP 层补足，见 §三）。

---

## 二、声学探索与生成工程

### 1. 从纯京味到“京腔金融双语流”
渔阳最难攻克的点在于：不仅北京腔要地道（儿化音自然），而且讲到 Wall Street、Debt-to-GDP、Token API 时不能降智。

### 2. 模型选型：E2 Qwen3-TTS CustomVoice（Dylan）
- 京腔＋中英混流由 **E2** 承担（E1 OmniVoice 做不了这种口音，见 `voices/README.md` §一·B 引擎矩阵）。权重 `~/Projects/rescue/models/qwen3-customvoice`（1.7B-CustomVoice，`spk_id` 含 `dylan`＝`beijing_dialect`）。
- **年龄与厚度不由 `instruct` 管**（主理人实测：instruct 里写"五十多岁"三版输出几乎不变，"26 岁"改不掉）——由 **DSP 加厚层 d4** 管。详见坑账 §一·C。
- **黑名单**：同权重里的 `uncle_fu` 已拉黑，**禁止**充当任何角色声底（坑账 §一·B）。京腔男声**只用 `dylan`**。

### 3. 基准母带（历史件，已判薄）
- ~~[05_yuyang_渔阳.wav](file:///home/ben/Music/voice_assets/locked/05_yuyang_%E6%B8%94%E9%98%B3.wav)~~（总纲母带，9.29s，SHA-256 全值 `2e42cd58a2ea6ca7d09c22ae5414fffe368dafad5b9d3801daca77f6dab6aaef`；2026-09-21 21:26 随旧 `locked` 索引事件进 Trash，**未经正式除名程序**，待主理人裁定恢复或除名）
- ~~`yuyang_qwen3_dylan.wav`~~ / ~~`yuyang_mixed_02_debt_as_money.wav`~~ / ~~`yuyang_mixed_03_token_api.wav`~~ —— 2026-09-21 夜主理人判"薄"（<250Hz 占比 8.9%–17.1%，四件 F0 乱跳 131–170Hz 差 39Hz＝同席位不同人），已被 **d4 六格**取代；`yuyang_mixed_01_dead_people.wav` 仍留仓作频谱参照，不入正片。
- **席位通道**：前两期挂飞书窄带传输；第三期起肉身常驻成都茶台，转为高保真大电容麦克风通道。

## 三、生成谱系 (Voice Genealogy) · 2026-09-22 d4 定版

> **定版声底**：`locked/yuyang_d4_base.wav` · 6.97s · F0 128.3Hz · <250Hz 占比 12.3% · SHA-256 `6098fc034f1858edaa4c64be9c517ffbfa287421765b2ca5f6ff38fa127c98d6`
> **verdict**：主理人 2026-09-21 夜试听圈定 **d4**（弃 d2/d3），2026-09-22 晨确认"就按这个来"，其余候选件清出。**耳朵是唯一验收终端（P-07）。**
> **六合仓**：`~/Music/voice_assets/yuyang/` —— **6/6 格已落**，六格已 pickup 进 `locked/`。

### 可原样重跑配方

```bash
# 角色差异全部在 characters/yuyang.json 的 audition 块；驱动器只有 scripts/audition.py
python3 scripts/audition.py --character yuyang          # 六格（含 post_dsp 加厚）
```

| 字段 | 值 |
| :--- | :--- |
| engine | **E2 Qwen3-TTS** — 权重 `~/Projects/rescue/models/qwen3-customvoice`（1.7B-CustomVoice） |
| 运行环境 | `~/Apps/Qwen3-TTS/.venv/bin/python`（transformers **4.57.3**）；⚠ miniconda 的 transformers 5.x 载权重报 `KeyError: 'default'`（ROPE_INIT_FUNCTIONS） |
| mode | **Custom Voice**（预置音色直出，无 ref_audio、无 seed —— 声纹由 `spk_id` 固定，天然可重跑） |
| speaker | **`Dylan`**（`spk_is_dialect: beijing_dialect`） |
| language | `Chinese`（文本内中英混流，**必须同句混说**，禁止单出英文句） |
| speed | E2 无 speed 入口，语速写进 `instruct` |
| 权重路径 | `~/Projects/rescue/models/qwen3-customvoice` |

**逐格 `instruct`**（自然语言；只管情绪/节奏，**不管年龄与声道粗细**）——六条共享前缀：
`五十多岁的老北京男人，京片子儿化音地道，嗓音沉，说话不紧不慢，夹英文时毫不客气，像在彭博终端前对账`

| 格 | 前缀之后的差异后缀 |
| :--- | :--- |
| base | `，句尾自然带一点上扬的笑意` |
| probe | `，这一句是反问，尾音拖住，留半口气让对方接` |
| attack | `，压着火说，字字砸下来，音量不抬但气势重` |
| defend | `，冷、短、不解释，说完就停` |
| break | `，提到旧事，嗓子发哑，句子说到一半咽回去` |
| afterglow | `，收场，放松下来，带一点疲惫的温和` |

**逐格台词**（中英混流）

| 格 | 台词 |
| :--- | :--- |
| base | Board 上那帮人跟我讲的不是 numbers，是 story。可我要的是 balance sheet，不是 bedtime story。 |
| probe | 您这句 returns，说的是 gross 还是 net？没写清楚，我这边只能记一个 question，不能记一个结论。 |
| attack | 别跟我拿 model 说事。您要是真信这一套，您自己先 buy in，别拉着大伙儿给您抬轿子。 |
| defend | 字我没 sign，人我还在这儿。您爱找谁对账找谁去，我这儿 door 永远开着。 |
| break | 零八年那会儿我要是早点 stop，我兄弟也不至于到今天。算了，说这个没用。 |
| afterglow | 得，今儿个就到这儿。Tomorrow 太阳一出来，该还的钱，一分也跑不了。 |

**post_dsp（加厚层 d4 —— 年龄感的真正来源）**

```
asetrate=24000*0.86,aresample=24000,atempo=1.1627906976744185,bass=g=8:f=170,equalizer=f=320:t=q:w=1:g=2
```
降调比 0.86 ＋ 170Hz 低频架升 8dB ＋ 320Hz 抬 2dB，`atempo` 补回原速。落盘命令由 `audition.py:apply_post_dsp()` 执行，逐字配置见 `characters/yuyang.json → audition.post_dsp.af`。

### 六格实测清单（冻结件，`locked/yuyang_d4_*.wav`）

| 格 | 时长 | F0 中位 | IQR | <250Hz 占比 | SHA-256（全值） |
| :--- | ---: | ---: | :--- | ---: | :--- |
| `base` | 6.97s | 128.3Hz | 91–168 | 12.3% | `6098fc034f1858edaa4c64be9c517ffbfa287421765b2ca5f6ff38fa127c98d6` |
| `probe` | 8.09s | 171.4Hz | 115–220 | 22.5% | `737b6106583ce8a4698ad8a3e7d87960971c585a0f31e60ef14173a5fd76f02a` |
| `attack` | 7.70s | 143.7Hz | 87–188 | 42.1% | `19e5e48a45a0e93bd44d82c0c1005492800056bbc0c9d06e662fec6ed220edc2` |
| `defend` | 6.72s | 137.1Hz | 98–209 | 12.7% | `a685eb3ef1aebbed1ad528f21280ce725b18ece980809670749954db4d702cac` |
| `break` | 6.08s | 133.3Hz | 101–188 | 22.4% | `582f4a2ccbdc295babf231088ce82fc2a0422f8ae891b3142908cfd21c3e2363` |
| `afterglow` | 5.77s | 195.1Hz | 123–222 | 11.8% | `bcce3c904c3837fc0105ed68a81caf15358ffb752293a1ca865735a7f372d49e` |

> ⚠ `probe`/`afterglow` 两格 F0 出带（171/195Hz 对 125–150）。测量含英文段会被倍频带偏，**不作跨格判据**；主理人既已圈定 d4 整批，此二格以耳朵复核为准。

### 谱系缺口与改判记录

- **2026-09-21 P-08 旧账本条误记**：坑账曾记"青衣/渔阳冻结件实出 E2 但**无常驻服务 ⇒ 不可原样重跑**"。实地核查推翻：本机 `~/Projects/rescue/models/qwen3-customvoice` 权重齐全（含 `vivian`／`dylan`），Custom Voice 走 `spk_id` 即定声纹 ⇒ **可原样重跑，无需 seed**。
- **档案 `physical_master` 曾误写 `04_yuyang_渔阳.wav`**（席位 05／声学号 VOICE_04 撞号，P-09），旧名不得再引用。
- **两步法（E2 出口音 ➔ E1 clone 出肉身）作废**：`yuyang_seed.pt`／`yuyang_ref.wav` 已挪 Trash，`POST /reload_seeds` 后 E1 `/speakers` 无"渔阳"。渔阳**只在 E2 侧**，厚度走 DSP。
- 实验场 `character_samples/` 内 20 余条 `yuyang_*` 历史候选从未归档 verdict，重跑前先清账。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/yuyang/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/yuyang.json` ＋《五卷人物资产总册》声纹人设 **表A（2026-08-30）**。（本档旧版引用的「表B」不存在，系我自造，坑账 P-19。）

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **05 渔阳**（于鲜洋（法定真名 · 央财金融史教授）／老于（浑名）） | ✅ |
| engine／mode | **Qwen3-TTS（E2）／Custom Voice** | ✅ |
| instruct（逐字） | — | ✅ |
| speed | E2 无 speed 入口 | ✅ |
| 台词（本席定稿句·逐字） | Board 上那帮人跟我讲的不是 numbers，是 story。可我要的是 balance sheet，不是 bedtime story。 | ✅ |
| 传输链路 | 远程位 —— 飞书 MCU 窄带链（300/3200Hz 截断＋粉红噪底＋50Hz 嗡鸣）。⚠ **本席例外**：`post_dsp` 的 d4 加厚链已**焊进** locked 六格母带（音高下移＋低频抬升，非传输链），故本席冻结件不是干音；换链路不必重抽声底，但改 d4 参数等于换母带 —— 须按除名三件套走。 | ✅ |
| post_dsp | `asetrate=24000*0.86,aresample=24000,atempo=1.1627906976744185,bass=g=8:f=170,equalizer=f=320:t=q:w=1:g=2` | ✅ |
| 实测 | 6.97s ／ F0 中位 **128.3Hz** ／ IQR 91–168Hz ／ <250Hz 占比 12.3% | ✅ |
| F0 目标带 | **不存在**（原「表B」F0 列系我自造、无《五卷》出处，P-19 已作废；F0 中位测的是本句说调不是声底，P-20 取消达标判定） | ✅ |
| SHA-256 | `6098fc034f1858edaa4c64be9c517ffbfa287421765b2ca5f6ff38fa127c98d6` | ✅ |
| 可复现性 | ❌ 不可（Voice Design 无 seed／无 prompt 入口，同参数重跑必换脸，P-01/P-13） | ✅ |
| 状态 | 2026-09-22 主理人圈定 d4 六格，已 pickup 至 voice_assets/locked/yuyang_d4_<state>.wav；六格 SHA 见 voices/05_渔阳_Yuyang__VOICE04.md §三。；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- `E1clone两步法_改判E2加DSP_20260921/`
- `E2候选_已定d4路线_20260922/`
- `_AB_base_unclefu.wav/`

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `yuyang_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
