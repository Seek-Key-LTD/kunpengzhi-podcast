---
cast_order: 01
voice_asset_id: "VOICE_01"
codename: "青衣"
legal_name: "秦雍琼"
status: "locked"
physical_master: "qingyi_vivian_v2_cultural_anchor.wav"
f0_target: "210Hz-235Hz"
pipeline: "OmniVoice Seed + Qwen3-TTS (Vivian)"
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
  - 结论：引擎 `/speakers` 里那个“青衣”仍在使用来历不明的旧声底，与档案定版声底**不是同一个人**。要么用定版声底重建种子，要么禁用 clone 通道、只走 Vivian 直出。
- **通道处理**：
  - 在场肉身席位，走**干净近场通道**（无电话窄带，无飞书压缩，保留呼吸声与胸腔温润感）。
## 四、生成谱系 (Voice Genealogy) · 2026-09-21 补录

> **定版声底**：`qingyi_vivian_v2_cultural_anchor.wav` · 25.04s · SHA-256 `e736a495d50b501da1a1f…`
> **六合仓**：`~/Music/voice_assets/qingyi/` —— 当前 **0/6 格已落**（base/probe/attack/defend/break/afterglow 全缺）。

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| engine | **Qwen3-TTS · 预置说话人 `Vivian`** | ✅ |
| mode | **既非 Design 亦非 Clone —— 预置音色直出**（无 instruct、无 ref） | ✅ |
| instruct | `null`（预置音色不适用） | ✅ |
| ref_audio | `null` | ✅ |
| speed | **不可考**（未记档） | ❌ |
| seed | **不可考**（未记档） | ❌ |
| post_dsp | 无（Direct Clean 近场） | ✅ |
| verdict | 2026-09-18 四选型盲测（`comp_qwen3_vivian` / `comp_qwen3_serena` / `comp_omnivoice_seed` / `comp_omnivoice_design`）后，主理人听定 Vivian；Serena 判“过冷”，OmniVoice 两路判“无台长定力” | ⚠ 口述 |

### 旧声底除名与连坐（必读）

- **`01_qingyi_青衣.wav`（7.15s · `2081e0ed…5836`）**：2026-09-21 主理人判定声底不合格，**已除名**（在 Trash，未 `rm`）。**严禁再作任何 clone 参考音。**
- **`qingyi_seed.pt`（`aeaba8af…`）/ `qingyi_ref.wav`（4.45s · `3f4679ab…` · instruct `女，青年` · ref_text“我叫青衣，青衣江的青衣。今天来给您聊聊孔子的故事。”）**：
  该 ref **既不是**已除名的旧母带（时长 7.15s 不符），**也不是**定版 Vivian（25.04s 不符，且 Vivian 根本不经 clone）—— **父母不明，按 §README 谱系铁律 6 判作废**。
  ⚠ 后果：引擎 `/speakers` 现在仍暴露一个名叫“青衣”的 OmniVoice 音色，**它不是本档案的青衣**。在生产中调用 `speaker: 青衣` 即构成声底污染。
- **缺产**：`qingyi_opening_poem_final.wav` / `qingyi_closing_poem_final.wav` 全库查无，§二 原记为虚记，青衣定场／散场诗至今未生产。

### 重跑配方（回退律的正确走法）

定版走预置音色，**一旦 Qwen3-TTS 下线或换版，青衣无法按图重造**。补产顺序：
1. 用定版 Vivian 母带截 10–15s 干净段作 `ref_audio` ➔ 抽新 `qingyi_seed.pt`（把预置音色转成自有 clone，这才是可重跑的资产）；
2. clone 效果不佳 ➔ **不许在 seed 上打补丁**，回退 Voice Design 重发候选（闭词表：`女，青年/中年，中音调/高音调`）；
3. 新声底父母听定后，六格逐格产：`base`(0.95) / `probe`(1.0) / `attack`(1.05) / `defend`(0.92) / `break`(0.85) / `afterglow`(0.80)。
