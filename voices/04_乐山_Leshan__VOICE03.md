---
cast_order: 04
voice_asset_id: "VOICE_03"
codename: "乐山"
legal_name: "游牧仁"
status: "locked"
physical_master: "03_leshan_乐山.wav"
f0_target: "125Hz-145Hz"
pipeline: "MiMo-TTS (川话1.0档➔降档)"
transmission_channel: "Direct Clean"
---

# 乐山 (Leshan) · 声音资产与生成档案

> **“你莫跟我扯那些书房里的玄龙门阵，老子在广汉鸭子河里刨出来的青铜器，它自己会说话！”**  
> **“大禹镇水镇的是什么？镇的就是上古川西平原的一本大水利账！”**

---

## 一、人物身份与声学设定

- **法定真名/身份**：**游牧仁**（圈内尊称“老游”），52岁。四川省文物考古研究院资深领队，扎根广汉鸭子河三星堆与金沙遗址考古第一线。
- **大名寓意**：“仁者乐山，于牧其仁”。字面看似天高地阔的草原游牧者，实则一辈子深扎农耕地层泥沼，以一铲一刷牧守古蜀苍生大地之仁德；与峨眉梅心易合称茶台**“梅游（没有）组合”**，司马相如子虚乌有望江亭双剑合璧。
- **地理暗线**：
  - 乐山大佛坐镇岷江、大渡河、青衣江三江汇流之口，天然具备“大禹镇水、三江合流”的坐地户气象。
  - 道名记主力核心，深谙道教洞天福地与宫观营造史。
  - 专属衍生专栏：《古蜀账房》（考古发掘一线与物质证据链审计）。
- **声学形态**：
  - **核心语态**：**纯正四川话（日常 1.0 档纯川味 ➔ 讲课自然降档）**。
  - **音色风格**：嗓音粗粝、低沉厚重、中气极足，带有常年风吹日晒的田野泥土味与袍哥式豪爽。
  - **长篇讲课降档铁律（2026-08-30 规范）**：
    - 日常插话、反驳争辩时：全川话输出，生猛泼辣。
    - 展开长篇考古论文论证时：方言密度自然降至川普，保留川话句式（“倒/得/起/哈/噻”）与语气词，确保全国听众对核心考古名词的听觉信息吸收。
  - **基频目标（F0）**：**125Hz ~ 145Hz**（低沉粗粝的男性田野学者声）。

---

## 二、声学探索与生成工程

### 1. 为什么拒绝现代轻佻搞笑川话？
网络上绝大多数四川话 TTS 偏向短视频搞笑、轻浮俏皮，完全违背了 52 岁正高级考古研究员在探方里摸爬滚打三十年的厚重感。乐山的四川话必须是**“古朴沉稳、生猛如铁”**的。

### 2. 方案定格与样音库
- **引擎组合**：OmniVoice（四川方言标签指令）+ 真实田野学者特征声底微调。
- **基准母带文件**：
  - [03_leshan_乐山.wav](file:///home/ben/Music/voice_assets/locked/03_leshan_乐山.wav)（总纲母带）
  - [leshan_chuanpu_01_问好.wav](file:///home/ben/Music/voice_assets/locked/leshan_chuanpu_01_问好.wav)（茶馆日常入席）
  - [leshan_chuanpu_02_白圭.wav](file:///home/ben/Music/voice_assets/locked/leshan_chuanpu_02_白圭.wav)（先秦商贾史论述）
  - [leshan_chuanpu_03_共祖.wav](file:///home/ben/Music/voice_assets/locked/leshan_chuanpu_03_共祖.wav)（学术长篇降档示范）
- **OmniVoice 克隆种子（✅ 全库唯一谱系可查的一条）**：`leshan_seed.pt`（2026-09-18）+ `leshan_ref.wav`（12.11s · instruct `男，中年，低音调，四川话`）
  - **经 SHA-256 比对：`leshan_ref.wav` 与 `leshan_chuanpu_03_共祖.wav` 字节完全相同**（`b299e719…f28da`），即 clone 参考音就是冻结库里的毕业母带 —— design ➔ clone 的血统链在此成立，全库仅此一条。
- **席位通道**：前两期在场肉身；第三期起进驻广汉考古工地，飞书远程带少许现场风噪。
## 三、生成谱系 (Voice Genealogy) · 2026-09-21 补录

> **定版声底**：`03_leshan_乐山.wav` · 8.61s · SHA-256 `3cfca1c949ad7d1468671…`；长篇降档示范 `leshan_chuanpu_03_共祖.wav` · 12.11s · `b299e719…f28da`
> **六合仓**：`~/Music/voice_assets/leshan/` —— 当前 **0/6 格已落**。

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| engine | **OmniVoice（:9098）· 四川方言标签指令** | ✅ |
| mode | **Clone**（`speaker: 乐山`） | ✅ |
| instruct | `男，中年，低音调，四川话` —— **全闭词表合法项，逐字可重跑** | ✅ |
| ref_audio | `leshan_ref.wav` · 12.11s · **SHA-256 `b299e719fdd8639e2a41b6db5350089926ee950ad99199c75793375a1a8f28da`** | ✅ |
| seed | `leshan_seed.pt` · `d8f5714073bff028…`（2026-09-18 09:53） | ✅ |
| post_dsp | 无（前两期 Direct Clean；第三期起工地风噪） | ✅ |
| verdict | 2026-09-18 四选型（`leshan_optA 中年低音`/`optB 中年极低音`/`optC 老年低音`/`optD 老年极低音`）后定 `中年·低音`；`leshan_seed_verify.wav` 为种子自检件 | ✅ |

### ✅ 全库唯一谱系完整的一条

**`leshan_ref.wav` 与冻结库 `leshan_chuanpu_03_共祖.wav` 字节完全相同**（SHA-256 一致），即 clone 参考音就是档案里那条毕业母带：

```text
Voice Design(四选型盲测) ➔ 听定 chuanpu_03_共祖 ➔ 入 locked/ ➔ 抽 leshan_seed.pt ➔ speaker: 乐山
```

Design ➔ Clone 血统闭合，**换机可原样重跑**。本角色可作为其余 16 席的谱系模板。

### 待补

- 档案 §一 定版 `pipeline` 写的是 **MiMo-TTS（川话 1.0 档➔降档）**，而实际冻结的 clone 走 **OmniVoice 四川话标签** —— 两法统并存且互不相认，须由主理人裁定谁是青衣之下的正式路线（〔悬〕）。
