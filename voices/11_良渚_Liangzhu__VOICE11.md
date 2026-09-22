---
cast_order: 11
voice_asset_id: "VOICE_11"
codename: "良渚"
legal_name: "梁随祝"
status: "voice_floor_pending_audition"
physical_master: "file:///home/ben/Music/voice_assets/liangzhu/base.wav"
f0_target: "175Hz-190Hz（《五卷》表B）"
pipeline: "E1 OmniVoice · Voice Design · 男·中年·中音调 · speed 1.05（无 seed ⇒ 不可同人重跑，P-01/P-16）"
transmission_channel: "Feishu DSP (MCU)"
---

# 良渚 (Liangzhu) · 声音资产与生成档案

> **“五千年了，肉身早化为尘土，但这根双螺旋 DNA 里的单倍群突变，却永生不灭地流在我们的血管里。”**  
> **“生当同衾，死当同穴，君若不弃永相随。这是梁祝的化蝶，更是华夏基因库五千年不断代的四梁八柱！”**

---

## 一、人物身份与声学设定

- **法定真名/身份**：**梁随祝**（圈内尊称“梁首席 / 梁教授”），44岁。浙江大学生命科学学院教授、古DNA与东亚人群演化基因组学首席科学家。
- **大名与宗族密码**：
  - **文学与基因双螺旋**：**“梁山伯祝英台，化而为蝶永相随” ➔ 梁随祝**！毛虫破茧化蝶，正是古DNA穿越数千年冻土与水流、在后代骨血中涅槃重生的最高科学隐喻！
  - **国家探源法统**：谐音暗扣**“四梁八柱，国士无双”**！良渚五千年前的高坝外郭与古DNA血脉连续性，撑起了中华文明探源工程最坚不可摧的“四梁八柱”。
- **声学形态**：
  - **核心语态**：**江浙吴语底色普通话（温润缜密、清冷理性、逻辑如同高精度基因测序仪般分毫不差）**。
  - **基频目标（F0）**：**140Hz ~ 155Hz**（细腻严谨、富有科学诗意的江南知识分子中音）。

<!-- BEGIN:VOICEFLOOR-2026-09-22 -->
## 声底件（2026-09-22 夜 · 六格制度废止，坑账 P-16）

> **本席现行产出物＝一条声底件**：`~/Music/voice_assets/liangzhu/base.wav`。六格（base/probe/attack/defend/break/afterglow）**不再是默认产出**——无 seed 通道撑不起"一人六态"（P-14），情绪差改由总装层（台词＋speed＋DSP）承担。
> 配方单一来源：`multipipeline-audio-render/characters/liangzhu.json` ＋《五卷人物资产总册》声纹人设 表A/表B。

| 字段 | 值 | 可复核性 |
| :--- | :--- | :---: |
| 席位·花名 | **11 良渚**（梁随祝（法定真名 · 浙大生命科学演化首席 · 44岁）） | ✅ |
| engine／mode | **OmniVoice（E1）／Voice Design** | ✅ |
| instruct（逐字） | 男，中年，中音调 | ✅ |
| speed | 1.05 | ✅ |
| 探针台词（全员同句） | 这笔账我核了三十年。没有出处的话，我一个字都不给播。 | ✅ |
| 传输链路 | 远程位 —— 飞书 MCU 窄带链（300/3200Hz 截断＋粉红噪底＋50Hz 嗡鸣）。⚠ 本声底件是**干音**：传输 DSP 在总装层挂，不进声底层（否则母带被 DSP 焊死，换链路就得重抽声底）。 | ✅ |
| post_dsp | 无（干音直出） |
| 实测 | 4.80s ／ F0 中位 **171.4Hz** ／ IQR 136–218Hz ／ <250Hz 占比 13.4% | ✅ |
| F0 目标带（表B） | 175–190Hz ➔ ✅ 落带内 | ✅ |
| SHA-256 | `87978ea7e42eb0238d09a680949ec48199186eedbb15ecc57b0ffaef3dee9335` | ✅ |
| 可复现性 | ❌ 声纹级不可（Design 无 seed，P-01）／❌ take 级不可／✅ 环境级（systemd 常驻 :9098） | ✅ |
| 状态 | 待主理人耳朵终审；通过者抽 seed／固化 prompt 后才谈 `locked/` | ✅ |

**判废与改判留痕**（`不合格隔离/`，禁 `rm`）：

- `F0目标带改判_20260922/` —— 判废原因：《五卷》表B 权威目标带 —— 08 琅琊 140–160Hz（应配 低音调，原配 中音调）；11 良渚 175–190Hz（应配 中音调＋快语速，原配 高音调 得 213.3Hz 偏离）。2026-09-22 按权威带改判重出。

**待办（按主理人法）**

1. 耳朵终审本件 ➔ 通过即抽 seed（E1 `scripts/make_seed.py`）或固化 `voice_clone_prompt`（E2）。
2. 通过件 pickup 入 `locked/`，命名 `liangzhu_<语名>.wav`，**禁数字前缀**，同步 `locked/README.md` 与 `SHA256SUMS.txt`，`sha256sum -c` 核条数。
3. 改判必回写《五卷》表A/表B 与本卡 `genealogy_note`，不许只改音不改档。
<!-- END:VOICEFLOOR-2026-09-22 -->
