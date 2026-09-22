---
cast_order: 01
voice_asset_id: "VOICE_01"
codename: "青衣"
legal_name: "秦雍琼"
status: "locked"
physical_master: "qingyi_vivian_v2_cultural_anchor.wav"
f0_target: "210Hz-235Hz"
pipeline: "E2 Qwen3-TTS CustomVoice 1.7B · spk_id=Vivian 直出（E1 clone 通道已判废禁用）"
transmission_channel: "Direct Clean"
---

# 青衣 (Qingyi) · 声音资产与精神法统档案

> **“不设红毯，不请明星，不造神迹。十五席列卿依次入座，一人一色，一人一声。”**  
> **“以最低的可见成本，完成一场午夜的学术阅兵。”**  
> **“我不是来告诉诸位应该说什么。我只负责保证，诸位说完以前，灯不会灭。”**  
> **“请党放心，请祖国放心。中国学人没有散场，一直在路上。”**

---

## 一、人物身份、破局动机与政治哲学

- **法定真名/身份**：**秦雍琼**（圈内尊称“秦台长”），38岁。广电总台副台长，常驻道场司仪主控、全剧总承销人、总担保人与政治避雷针。
- **大名寓意**：【秦】承大一统制度法统与川蜀石柱忠贞侯硬骨；【雍】取九州雍州肃穆之台风，温和整饬、大度压场；【琼】美玉风骨，暗通川西青衣江分水母岭“邛崃山”，地缘与法统彻底闭环。
- **家族渊源**：重庆大轰炸遗孤的三代后裔。爷爷是 1940-1941 年大轰炸中失去双亲的孤儿，家族记忆带着血腥硝烟味，天然对一切“官方粉饰做账”免疫。
- **履历文脉**：毕业于歌乐山下**四川外国语大学（SISU）法语与国际新闻系**。曾任总台驻巴黎特派记者多年，深谙西方“词汇法权”与国际传播舆论攻防。

### 核心政治哲学：反英雄（Anti-Hero）对抗 MrBeast
青衣不是在做一个平庸的互联网内容产品，她是在用一场精密算计的“反英雄式午夜学术阅兵”，向历史交卷。

| MrBeast 式资本造神英雄 | 青衣式体制反英雄 |
| :--- | :--- |
| **金钱必须可见**（狂撒数百万美金做奇观） | **赞助人必须隐身**（总Sponsor主动从画面消失） |
| **场面不断升级**（豪车、孤岛、毫秒级多巴胺刺激） | **视觉主动降级**（纯色背景、声波、铅笔字） |
| **主角是组织者**（镜头永远对着MrBeast狂欢） | **主角是十五席学人**（自己退居幕后沏茶保驾） |
| **用刺激争夺注意力**（把人降维成算法数据流） | **用克制筛选注意力**（用纯粹思想留下清醒头脑） |
| **告诉观众“看我做了什么”** | **告诉观众“听他们在说什么”** |
| **以播放量和投流证明成功** | **以听完、重听和激辩证明成功** |

- **“最低可见成本，最高思想密度”**：
  钱并没有少花，只是绝不花在明星通告、华丽舞台和算法买量上，而是全额砸进“声音重工业”——十五套独立成立的声音人格、23篇古文压力测试、法统与创伤物证、Ace变奏基因库、十年后依然能重新生成的自动化管线。
- **青衣的极致张力**：
  - 她是体制内职位最高、最懂宣传纪律的人，却亲手搭建了一个**绝不预设结论**的硬核学术辩论场；
  - 她拥有全场最大的麦克风，却把自己的台词压缩到最克制；
  - **“请党放心，请祖国放心”**不是要求学者统一口径，而是她替这场刺刀见红的争鸣穿上的钢铁防护服——茶台之上，可以拍桌子、可以反驳作者、可以重新核算国家资产负债表，但谁也不许偷换凭证！
- **声学定位（全场基准锚点）**：
  - **定位**：全场**唯一绝对标准普通话**（国字脸新闻主播音）。
  - **质感**：字正腔圆、清澈端庄、沉静威严、温润中带有克制的刀锋感。
  - **基频目标（F0）**：**210Hz ~ 235Hz**（端庄开阔的女中高音）。

---

## 二、声学探索与模型选型演进

### 1. 为什么必须是全场唯一“标准普”？
在全剧策划之初，主理人即确立“方言立人设、防角色离散”铁律。其余所有嘉宾（峨眉、乐山、渔阳、紫金、竹湖等）全带浓烈地方腔调。如果司仪也带口音，整台播客将陷入听觉混乱与方言泥潭。因此，青衣是全场的“音高坐标原点”与“听觉基石”。

### 2. 引擎选型历程
- **候选 1：开源标准女声**：音色单薄如客服，缺乏广电总台副台长的政治站位与文化定力，打回。
- **候选 2：Qwen-TTS / Qwen3 评书与播音模型**：
  - 测试了 `Serena`（过于冷淡理智）与 `Vivian`（文化主播质感）。
  - `Vivian` 呈现出极佳的“文化大屏主播”风范，音韵饱满，咬字工整，成为重要对比基线。
- **候选 3：OmniVoice 种子母带 + 深度对齐**：
  - 以 4.45s 端庄女声参考音（`qingyi_ref.wav`，instruct `女，青年`）抽取 `qingyi_seed.pt`，入驻 `kunpengzhi-audio-engine` 角色库。
  - ~~渲染《三更道场定场诗》开场与闭场（`qingyi_opening_poem_final.wav` / `qingyi_closing_poem_final.wav`）~~ —— **经全盘核查（2026-09-21）：这两个文件从未落盘，本条记录为虚记**。青衣的定场诗／散场诗至今未生产。
- **定版归属**：候选 2 的 `Vivian` 长叙事件胜出为唯一法统声底；候选 1 与 OmniVoice 定场诗旧母带 `01_qingyi_青衣.wav` 均于 2026-09-21 除名。

---

## 三、定版资产与声学参数

- **核心母带文件**：
  - [qingyi_vivian_v2_cultural_anchor.wav](file:///home/ben/Music/voice_assets/locked/qingyi_vivian_v2_cultural_anchor.wav)（**当前唯一法统声底** · 25.04s · Qwen3-TTS `Vivian` 文化主播长篇叙事）
  - ~~`01_qingyi_青衣.wav`~~（**2026-09-21 除名作废**：主理人听感判定声底不合格（客服感、无台长定力），已从 `voice_assets/locked/` 剔除，**严禁再作为任何 clone 参考音引用**）
  - `qingyi_opening_poem_final.wav` / `qingyi_closing_poem_final.wav`（**缺档**：§二所述渲染结果从未落盘，全库查无此二文件；青衣定场诗／散场诗仍待生产）
  - 盲测对照件（实验场 `character_samples/`，非资产）：`qingyi_comp_qwen3_vivian.wav`、`qingyi_comp_qwen3_serena.wav`、`qingyi_comp_omnivoice_seed.wav`、`qingyi_comp_omnivoice_design.wav`、`qingyi_vivian_v1_storyteller.wav`、`qingyi_vivian_v3_cold_neutral.wav`、`qingyi_vivian_v4_cynical_boss.wav`
- **OmniVoice 克隆种子（⚠ 法统断裂）**：
  - `qingyi_seed.pt`（2026-05-31）+ `qingyi_ref.wav`（4.45s，instruct `女，青年`，ref_text“我叫青衣，青衣江的青衣……”）
  - 该 ref 既不是已作废的 `01_qingyi_青衣.wav`（7.15s），也不是定版的 `qingyi_vivian_v2`（25.04s），**父母不明**。
  - **2026-09-21 夜主理人已裁**：**只走 Vivian 直出**。用定版母带抽 seed 转 E1 clone 的重铸六格已产出一批，试听判"**这个声音一听阅历就不够**"，全部判废挪 `voice_assets/qingyi/不合格隔离/E1clone重铸_判废20260921/`。**青衣永久禁止走 E1 Clone 通道**。
- **通道处理**：
  - 在场肉身席位，走**干净近场通道**（无电话窄带，无飞书压缩，保留呼吸声与胸腔温润感）。
## 四、生成谱系 (Voice Genealogy) · 2026-09-22 二次改判

> **定版声底（＝clone 的参考音）**：`locked/qingyi_vivian_v2_cultural_anchor.wav` · 25.04s · SHA-256 `e736a495d50b501d8fe1e3fd5764e3e23dce419b0f52861751b5e4f9f64a1a1f`
> **声纹固化件**：`~/Projects/rescue/seeds/e2_prompts/qingyi_vivian_xvec.pt`（E2 `VoiceClonePromptItem`，`x_vector_only_mode=true`，由 `scripts/audition.py` 首跑时抽取）
> **六合仓**：`~/Music/voice_assets/qingyi/` —— 现 **1/6 格**（`base.wav`，clone 首件，SHA `bbfd0a2a7be5a9d6b5cba5f7a783039e627a1de4bb4690e66a105eeece2dfb65`，**待耳朵终审**）

### 改判史（三次，全留此立此存照）

| # | 日期 | 当时的说法 | 结局 |
|:--:|:---|:---|:---|
| 1 | 2026-09-21 夜 | 用 E1 clone 重铸青衣正声 | 主理人判"**这个声音一听阅历就不够**"，六格判废 ｜
| 2 | 2026-09-22 晨 | "E2 Vivian 直出六格＝一人六态；`spk_id` 焊死声纹 ⇒ 可原样重跑" | **虚记，被耳朵推翻**：主理人判"**这里边肯定是 6 个人**" |
| 3 | 2026-09-22 午 | 读源码坐实（坑账 **P-14**） | `generate_custom_voice` **无 seed、无 prompt 入口**，codebook 每次调用重采样；且逐格不同 `instruct` **会连音色一起改** ⇒ 直出六格＝六次独立发声，结构上就不保证同人 |

**现行唯一合法路线**：E2 **Voice Clone** —— base 权重 `~/Apps/Qwen3-TTS/model_local_full` ＋ 上面那颗 `.pt`。代价写死在协议里：**clone 通道不接收 instruct**，六格的情绪差一律由**台词**承担（标点、句式、语气词、断句）。

```bash
# 角色差异全部在 characters/qingyi.json 的 audition 块；驱动器只有 scripts/audition.py
~/Apps/Qwen3-TTS/.venv/bin/python scripts/audition.py --character qingyi                # 出六合（clone）
~/Apps/Qwen3-TTS/.venv/bin/python scripts/audition.py --character qingyi --takes 4      # 选型：连抽候选，落试音室不进仓
```

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| engine | **E2 Qwen3-TTS** | ✅ |
| mode | **Voice Clone**（不再是 Custom Voice） | ✅ |
| 权重 | `~/Apps/Qwen3-TTS/model_local_full`（**base**，`tts_model_type: base` —— CustomVoice 权重不支持 clone） | ✅ |
| 运行环境 | 只能用 `~/Apps/Qwen3-TTS/.venv/bin/python`（transformers **4.57.3**）；miniconda 的 5.x 会 `KeyError: 'default'` | ✅ |
| 声纹种子 | `qingyi_vivian_xvec.pt`（父母＝定版母带，`x_vector_only_mode=true`：只取说话人向量，不带 ref_text 的 ICL，免得把母带台词复述进新格） | ✅ |
| speaker | `Vivian` —— **仅作"声底父母从哪来"的记号，不参与本次调用** | ✅ |
| language | `Chinese`；speed：E2 无入口 | ✅ |
| instruct | **不适用**（本通道不接收）。旧六格的逐格 instruct 见下表，只作选型记录 | ✅ |
| post_dsp | **无**（Direct Clean 近场，不做加厚；青衣的阅历感由声底本身承担 —— 与渔阳相反） | ✅ |
| 可复现性 | ✅ **声纹级**（prompt 存盘，换机可同人重跑）／⚠ **take 级不可**（P-12：重跑必重听）／⚠ **环境级**（非常驻，需手动起单次进程） | ✅ |

### 听感对照（2026-09-22 交主理人裁）

试音室 `~/Music/san_geng_dao_chang_audition/听感对照_qingyi_20260922/`：
`甲_定版母带_Vivian.wav`（`e736a495…`）／`乙_新clone_base.wav`（`bbfd0a2a…`，10.08s F0 212.4Hz 低频占比 5.5%）／`丙_旧CustomVoice连抽_base.wav`（`3f065e72…`，10.56s）。
**要裁的问题**：乙是不是甲？丙又是不是甲？—— 只有耳朵算数（P-07）。

### ⚠ 声纹余弦不能替耳朵（P-15，本日实测）

曾想用 E2 `extract_speaker_embedding` 的余弦矩阵机器坐实"六个人"。拿真·不同人做对照组后作废：紫金↔青衣 0.920–0.923、渔阳(男)↔青衣 0.936–0.943、**乐山(川话男)↔青衣定版母带 0.955–0.972**，而青衣六格互比 0.965–0.993。动态范围只有 0.92–0.99 ⇒ 抓得住"接错线"，**抓不住"换脸"**。`--identify` 从此只作粗筛（<0.93 查混线），禁止据此判同人。

### 已判废：E2 CustomVoice 六连抽（2026-09-21 21:54 产 · 六件挪 `voice_assets/qingyi/不合格隔离/E2_CustomVoice六连抽_判六人_20260922/`，未 `rm`）

> 下表数据保留备查：它同时是"**逐格换 instruct ⇒ 逐格换脸**"的现场证据（`defend` 掉到 177.8Hz、`afterglow` 冲到 229.7Hz，同一"人"跨度 52Hz）。

**逐格 `instruct`**（自然语言，只管情绪/节奏；主理人实测 E2 **不听年龄指令**，见坑账 §一·C）

| 格 | instruct | 台词 | 时长 | F0 中位 | IQR | <250Hz 占比 | SHA-256 | `bbfd0a2a7be5a9d6b5cba5f7a783039e627a1de4bb4690e66a105eeece2dfb65` | ✅ |
| :--- | :--- | :--- | ---: | ---: | :--- | ---: | :--- |
| base | 四十多岁的女性副台长，央视级字正腔圆标准普通话，端庄沉稳，中高频明亮但不尖，吐字干净有控制力，带着长期主持大局的阅历感 | 各位师傅、朋友，这里是FM九九点八。今晚三更开卷，我们把该审的账，摊在桌面上看。 | 10.56s | **212.4Hz** | 178–231 | 25.2% | `3f065e72fc9f68c66dfde338e40203d57612db7dc4393263724c7e6c00d33761` |
| probe | 同一个人，语气转为不动声色的试探，尾音略收，咬字放慢半拍，不抬高音量 | 你这句话，出处在哪儿？我做了三十年编辑，没有出处的引号，我一个字都不给播。 | 14.24s | **224.3Hz** | 194–261 | 29.2% | `376e1212bba93aa3affc0fbf34060548988995fe5590ed0af984dc4e56748bd0` |
| attack | 同一个人，公事公办的硬，胸腔下沉，字字落地，压着说而不是喊，权威感来自不容置辩 | 这段掐掉。不是我不敢播，是你这套话经不起核。明天把材料送到台里，我当面跟你算。 | 9.76s | **216.2Hz** | 186–253 | 20.4% | `e069e45424007a7ca1c8a1c72ceea85b2fbf7c4167c250e2ad651f5bfa8a4bc4` |
| defend | 同一个人，冷静简短，一句说完不停顿，不带情绪解释第二遍 | 安全线我来顶。白天的KPI我认，但深夜这一小时，谁也别想拿算法来替我说话。 | 10.80s | **177.8Hz** | 162–205 | 66.3% | `b43ddc2a62910cc772d1f82dc68e8d3f4ba10af151014d2f2c1390689e1a8559` |
| break | 同一个人，连续开会五小时后的疲态，喉底微微发涩，语速放慢，但不哭腔、不失态 | 开了五个小时的会，我这嗓子也是涩的。可有些事，你不说，就没有人替你说。 | 13.28s | **190.5Hz** | 164–214 | 38.0% | `2deabc8674d4c9dd64934deb063c133a6c2a8521550d75176b195384fd159d6d` |
| afterglow | 同一个人，收束全场，气声增多，音色温暖一点，像关灯前最后那句话 | 今天就到这里。窗外还在下雨，各位收好这份卷宗，我们三更再会。 | 7.44s | **229.7Hz** | 202–270 | 43.8% | `d9e9197113d4021afcaa2c3d3ea10ffb24113efabdbc163003d93e551f966dd4` |

> `defend`/`break` 两格 F0 落带下（目标 210–235）。占比 66.3% 说明那两句偏低胸腔为主，**是否同一人须耳朵裁**（P-07），客观指标只抓接错线。
> 仓内另存 `_AB_base.wav`（试音对照件，非资产）与 `ref_text.txt`（E1 路线遗留的 ASR 反写文本，随 E1 路线作废，留此仅备查）。

### 旧声底除名与连坐（必读）

- **`01_qingyi_青衣.wav`（7.15s · `2081e0ed…5836`）**：2026-09-21 主理人判定声底不合格，**已除名**（在 Trash，未 `rm`）。**严禁再作任何 clone 参考音。**
- **`qingyi_seed.pt`（`aeaba8af…`）/ `qingyi_ref.wav`（4.45s · `3f4679ab…`）**：父母不明，2026-09-21 已挪 Trash。⚠ 引擎 `/speakers` 目前仍暴露一个名叫"青衣"的 OmniVoice 音色，**它不是本档案的青衣**，调用 `speaker: 青衣` 即构成声底污染（E1 侧唯一合法用法见坑账 P-02）。
- **E1 Clone 重铸路线（2026-09-21 夜）**：六格已按"定版母带抽 seed ➔ clone"产出并试听，主理人判"**这个声音一听阅历就不够**"，全部判废，隔离于 `voice_assets/qingyi/不合格隔离/E1clone重铸_判废20260921/`。**从此青衣不走 E1，只走 E2 Vivian。**
- **缺产**：`qingyi_opening_poem_final.wav` / `qingyi_closing_poem_final.wav` 全库查无，§二 原记为虚记，青衣定场／散场诗至今未生产。

### 待办（按主理人法）

1. **今晨**：主理人试听上表六格 ➔ 通过者 pickup 入 `locked/`（命名 `qingyi_<state>.wav`，禁数字前缀），同步 `SHA256SUMS.txt`。
2. 定场诗／散场诗用同一 `speaker=Vivian` 直出，**不引入第二条声纹**。
3. **禁止**再为青衣抽 seed 或走 Design：预置音色的声纹即资产，环境级依赖记明权重路径与 venv 已足够（坑账 P-13）。
### 待办（按主理人法）

1. **今日**：主理人听"听感对照"三件 ➔ 定"乙是不是青衣"。是 ➔ 出齐其余五格；不是 ➔ **不许在 prompt 上打补丁**，回 Custom Voice 用 `--takes N` 重选声底父母，重抽 `.pt`，本档案留改判记录。
2. 六格过耳后 pickup 入 `locked/`（命名 `qingyi_<state>.wav`，禁数字前缀），同步 `SHA256SUMS.txt` 并 `sha256sum -c` 核条数。
3. 定场诗／散场诗与六合**同一条 clone 通道**出（`--states` 只跑 base 词表外文本另议），不引入第二条声纹。
4. **禁止**再走 E1（判废于第 1 次改判）；**禁止**用 Custom Voice 直出任何"六格基线"（P-14）。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/qingyi/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/qingyi.json` ＋《五卷人物资产总册》声纹人设 **表A（2026-08-30）**。（本档旧版引用的「表B」不存在，系我自造，坑账 P-19。）

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **01 青衣**（秦雍琼（法定真名）／秦台长（浑名）） | ✅ |
| engine／mode | **Qwen3-TTS（E2）／Voice Clone** | ✅ |
| instruct（逐字） | —（E2 Voice Clone 不接收 instruct；声纹由 `~/Projects/rescue/seeds/e2_prompts/qingyi_vivian_xvec.pt` 锁） | ✅ |
| speed | E2 无 speed 入口 | ✅ |
| 台词（本席定稿句·逐字） | 各位师傅、朋友，这里是FM九九点八。今晚三更开卷，我们把该审的账，摊在桌面上看。 | ✅ |
| 传输链路 | 在场位 —— 近场电容麦，干净无损通道，不挂传输 DSP。 | ✅ |
| post_dsp | 无（干音直出） |
| 实测 | 10.08s ／ F0 中位 **212.4Hz** ／ IQR 175–264Hz ／ <250Hz 占比 5.5% | ✅ |
| F0 目标带 | **不存在**（原「表B」F0 列系我自造、无《五卷》出处，P-19 已作废；F0 中位测的是本句说调不是声底，P-20 取消达标判定） | ✅ |
| SHA-256 | `bbfd0a2a7be5a9d6b5cba5f7a783039e627a1de4bb4690e66a105eeece2dfb65` | ✅ |
| 可复现性 | ⚠ 取决于 prompt 是否在档：`~/Projects/rescue/seeds/e2_prompts/qingyi_vivian_xvec.pt` | ✅ |
| 状态 | 2026-09-22 改判：E2 Custom Voice 六连抽整体作废，六件挪 voice_assets/qingyi/不合格隔离/E2_CustomVoice六连抽_判六人_20260922/；改 mode=Voice Clone（base 权重 + x-vector prompt）重产六格。F0/低频占比只是辅助，身份度用 audition.py --identify 声纹余弦矩阵坐实，终审仍是耳朵。；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- `E1clone重铸_判废20260921/`
- `E2_CustomVoice六连抽_判六人_20260922/`

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `qingyi_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
