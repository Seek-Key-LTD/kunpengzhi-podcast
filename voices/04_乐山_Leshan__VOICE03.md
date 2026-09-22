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

### ⚠ 谱系闭合 ≠ 声底成立（主理人听感一票否决 2026-09-21）

**`leshan_ref.wav` 与冻结库 `leshan_chuanpu_03_共祖.wav` 字节完全相同**（SHA-256 一致），即 clone 参考音就是档案里那条毕业母带：

```text
Voice Design(四选型盲测) ➔ 听定 chuanpu_03_共祖 ➔ 入 locked/ ➔ 抽 leshan_seed.pt ➔ speaker: 乐山
```

Design ➔ Clone 血统闭合，**换机可原样重跑** —— 但这只证明“文件没接错”，不证明“人是对的”。

**主理人裁定：`leshan_ref.wav`（即 `leshan_chuanpu_03_共祖.wav`）这条声底听感上就是峨眉，不是乐山。**
故本条记录降为**程序性合格、实体性作废**：

- `leshan_seed.pt` / `leshan_ref.wav` 谱系可查，但**声底判错，不得作为乐山资产**；
- 冻结库内 `leshan_chuanpu_01/02/03` 三条同源件**连坐待裁**（01 问好 6.94s、02 白圭 5.37s、03 共祖 12.11s）；
- `03_leshan_乐山.wav`（8.61s）与之是否同一声底，须耳朵复核后才能定；
- **回退动作**：按 §README 谱系铁律，回 ① Voice Design 重发乐山候选（闭词表 `男，中年/老年，低音调/极低音调，四川话` 四格已盲测在实验场 `leshan_optA..optD`），听定新声底父母 ➔ 重抽 seed ➔ 旧 seed 连同产出整批进 Trash。

**教训写死**：SHA-256 一致、时长一致、路径可追，全部是**同义反复的自检**，一条也不能替代耳朵。谱系核查只能抓“接错线”，抓不出“长错脸”。

### 待补

- 档案 §一 定版 `pipeline` 写的是 **MiMo-TTS（川话 1.0 档➔降档）**，而实际冻结的 clone 走 **OmniVoice 四川话标签** —— 两法统并存且互不相认，须由主理人裁定谁是青衣之下的正式路线（〔悬〕）。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/leshan/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/leshan.json` ＋《五卷人物资产总册》声纹人设 **表A（2026-08-30）**。（本档旧版引用的「表B」不存在，系我自造，坑账 P-19。）

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **04 乐山**（游牧仁（法定真名 · 省考古院资深领队）／老尤（浑名）） | ✅ |
| engine／mode | **OmniVoice（E1）／Voice Design** | ✅ |
| instruct（逐字） | 男，中年，四川话，低音调 | ✅ |
| speed | 0.93 | ✅ |
| 台词（本席《五卷》原文金句·逐字） | 你莫跟我扯那些书房里的玄龙门阵，老子在广汉鸭子河里刨出来的青铜器，它自己会说话！ | ✅ |
| 传输链路 | 在场位 —— 近场电容麦，干净无损通道，不挂传输 DSP。 | ✅ |
| post_dsp | 无（干音直出） |
| 实测 | 7.90s ／ F0 中位 **167.8Hz** ／ IQR 133–222Hz ／ <250Hz 占比 27.1% | ✅ |
| F0 目标带 | **不存在**（原「表B」F0 列系我自造、无《五卷》出处，P-19 已作废；F0 中位测的是本句说调不是声底，P-20 取消达标判定） | ✅ |
| SHA-256 | `cd1b6ff59392821555e6f9774499d956d74e341e885162c438deaa1700b87a13` | ✅ |
| 可复现性 | ❌ 声纹级不可（Design 无 seed，P-01）／❌ take 级不可／✅ 环境级（systemd 常驻 :9098） | ✅ |
| 状态 | 待主理人耳朵终审；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- 无

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `leshan_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
