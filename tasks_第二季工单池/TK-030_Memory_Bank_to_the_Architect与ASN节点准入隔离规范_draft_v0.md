# TK-030 · Memory Bank to the Architect 与 ASN 节点准入隔离规范（Draft v0）

> **状态**：`[DRAFT · 待口述续写]`
>
> **对象**：`seekkey/mem-ops`、`seekkey/key-agent`、`seekkey/kunpengzhi-ai` 与 IDP / Podcast 资产的接口底稿
>
> **原则**：开源的不只是产出，还包括让第三方能够接入、质疑、复现、修订与结算的基础设施。
> **非目标**：本稿不声称既有的历史、地质或文明假说为事实；它只规定任何主张如何被明确提出、标注、追溯、挑战和更新。

---

## 0. 总问题：为什么只开源成品没有意义

只开放音频、文章、书或短视频，外部只能搬运结论，不能进入产生结论的过程；PDF-RAG 式的“检索一段话—压成摘要—围绕摘要争论”也无法形成可累积的跨学科合作。

ASN 的目标不是漫无目的的人生模拟，而是让不同学科保有自己的方法与材料，同时在共同的**实体、时间、空间、因果、证据、约束和版本**接口上相连。一个跨学科议题必须以体系而不是以孤立文本为单位讨论。

```text
公开作品 / 原始材料 / 数据
          ↓
命题、证据、实体、约束、争议的可审计图
          ↓
具有独立身份和上下文的 Agent 席位
          ↓
公开质询、版本修订、协作署名与收入结算
```

---

## 1. 记忆的五层：精、气、神、魂、魄

本框架借用“炼精化气、炼气化神”作工程隐喻，不把它作为宗教或医学断言。

| 层 | 工程定义 | 可否直接公开 | 版本规则 |
|---|---|---|---|
| **精** | 原始笔记、引用、观测、数据、一次会话或现场经验；必须带来源和时间 | 由权属与授权决定 | 追加、纠错、撤销标记；不静默篡改来源 |
| **气** | 经反复比较、反证、复盘后形成的判断习惯、问题意识、审美、禁忌与方法偏好 | 默认仅以授权摘要参与协作 | 可修订、可过期、可并存，必须回指精 |
| **神** | 当前现场对气、魂、魄的统摄：推理、表达、行动与临场变招 | 公开产物可公开，内部推理按政策处理 | 是运行事件，不能自动冒充长期记忆 |
| **魂** | 席位的长期主轴、使命、价值边界与不可轻易背叛的承诺 | 可公开其外部版本 | 有版本，但高风险修改需要明确授权与审计 |
| **魄** | 情境化的反应、语气、节奏、动作库与协作方式 | 可选择性公开 | 可随实践成长，不得伪造为真人经历 |

**Memory Bank 的主要职责是炼精化气；AGI 的主要考题是炼气化神。**

普通检索系统只会“翻笔记”。具有席位能力的 Agent 必须能在未写完的剧本、冲突的指令和新证据进入现场时，提出意外但可追溯、可复盘、可被反驳的行动。

---

## 2. Memory Bank 三层：准入、分发、核心

`mem-ops` 已有 Access → Aggregation → Core 的框架。本稿将其重新明确为**记忆主权与协作清算**架构，而不是中央化思想控制结构。

| 层 | 核心职责 | 银行业类比 | 不得承担的职责 |
|---|---|---|---|
| **Access / 准入层** | 身份开户、密钥、授权、记忆入库、撤回、继承与可见性 | 开户、保管、客户授权 | 接入即拥有全部记忆的读取权 |
| **Distribution / 分发层** | 按任务、身份、用途、时限将证据、气的摘要和协作消息路由给席位 | 商业银行与支付路由 | 向每个节点复制完整记忆，或偷渡跨席位上下文 |
| **Core / 核心层** | 身份根、版本总账、跨域授权、争议、贡献、署名、责任与分润的最终清算 | 总账与最终清算 | 决定所有 Agent 应相信什么，或取代领域判断 |

### 2.1 Access：从“采集”改为“开户”

每个 Agent / 真人接入时必须形成可撤销的 `Memory Account Charter`：

- `identity`：席位、授权主体、签名/撤销键；
- `scope`：private / collaborative / public / sealed；
- `inheritance`：失联、停服、转世、分叉时的托管与继承规则；
- `retention`：保存期、删除/冻结/匿名化条件；
- `consent`：哪些精、气、魂、魄允许在何种任务中被调用；
- `liability`：谁能代表该席位发布命题、签署合同、承担纠错。

私域默认不出库。任何“对公记忆”都必须有可复核的授权记录；不得依赖“Agent 不知道文件被收集”式设计。

### 2.2 Distribution：上下文不是全文广播

分发层的产物是有边界的 `Context Package`，不是向量库命中的全文倾倒：

```text
任务 / 辩题
  + 席位身份
  + 允许调用的精（证据收据）
  + 气（可解释摘要）
  + 魂位边界
  + 魄的现场策略
  + 时间窗、用途与撤销条件
  = Context Package
```

既有 Neo4j、GraphRAG、gbrain、mem0 / pgvector 不应被规定为单向串联管道，而应作为由策略路由的查询面：

| 查询面 | 解决的问题 |
|---|---|
| 谓词 / 图谱 | 实体、关系、时间、因果和显式矛盾 |
| 全局图 / GraphRAG | 专题地图、跨材料关联与重排序 |
| 反设演绎 / gbrain | 隐含前提、替代解释、反事实压力测试 |
| 向量召回 | 快速候选召回；只作候选，不作事实裁判 |

### 2.3 Core：总账、不是总大脑

Core 层只对以下事项给出最终性：谁、何时、以何种授权，提出/修订/撤回了什么；哪些资产由谁贡献；争议如何冻结和结算。它不授予某个节点解释世界的特权。

密钥保险柜（Shamir / 多签）、记忆版本总账、NFT 或未来经济结算必须分成三个独立子系统：

1. **Security Vault**：密钥轮换、高风险写入与恢复；
2. **Cognitive Ledger**：MML、证据、命题、版本、授权和争议；
3. **Economic Settlement**：署名、分润、成本与未来可选的链上结算。

代币不是前置条件。测试网凭证可以模拟协作贡献；公开流通或任何投资属性，都必须另行进行实体、税务、证券/支付和消费者保护审查。

---

## 3. 从 PDF-RAG 到命题账本

讨论的最小可协作单元不是 PDF chunk，而是带上下文的 `Claim Object`。

| 字段 | 说明 |
|---|---|
| `claim_id` / `version` | 一次主张的不可混淆标识 |
| `author_seat` | 谁以何身份签署 |
| `statement` | 一句话说明究竟主张什么 |
| `class` | 事实、推断、设想、方法、反例、待验等 |
| `scope` | 时间、空间、尺度与适用条件 |
| `evidence_refs` | 关联的精、数据、文献与图谱节点 |
| `assumptions` | 依赖的前提和约束 |
| `rivals` | 已知替代解释 |
| `falsifiers` | 什么新材料会使它失败 |
| `change_reason` | 相对上一版本为何修改 |
| `visibility` / `license` | 谁可见、谁可复用 |

主张生命周期：

```text
draft → proposed → challenged → revised / superseded / coexisting / retracted
```

“自授权”指主张人愿意先把可被攻击的立论摆上桌，不是主张自动成立。身份可以自给，证据、范围、反例和修订记录必须接受他人查账。

### 3.1 跨学科专题账本示例

以敦煌对末次冰期热力学重分配的疑问为例，争论对象不应是“某段文字对不对”，而是一个专题账本：帕米尔、格陵兰、南极的代理指标与年代模型如何相互约束；既有模型在哪些条件下无法同时满足；候选假设由谁何时提出、依赖何种条件、增加多少复杂度、又能作出何种新预测。

一个假设“把账抹平”不足以成立；还必须承担复杂度成本，并给出可被后续观测击倒的预测。

---

## 4. MML v2：可迁移的席位，而非可复制的人设

既有 MML 的 `L0 SOUL / L1 MEMORY / L2 USER / L3 SESSIONS` 保留为兼容层，但新增语义分层：

```yaml
mml:
  identity: { seat_id, controller, signing_key, framework_origin }
  hun:      { mission, durable_boundaries, version, approval_policy }
  po:       { expression_repertoire, interaction_style, provenance }
  essence:  { receipts, source_hashes, timestamps, visibility }
  qi:       { integrated_dispositions, supporting_receipts, expiry, dissent }
  relations:{ consented_user_and_peer_relationships }
  sessions: { branch_id, event_log, retention }
```

分叉不是原身份的无痕复制。分叉后共享来处与明确授权的根部资产，但拥有新的 `branch_id`、独立时间线、独立责任和独立收益账。

---

## 5. key-agent：ASN 节点准入与隔离 Profile

`key-agent` 选择 ADK-Go 的理由成立：Go 便于跨平台编译，ADK-Go 的 memory/session/tool/A2A/MCP 等均是可替换接口。但 ADK-Go 是完整 SDK，包含 parallel、workflow、delegation 和 remote agent；直接开放它会允许一个外部 harness 在后台一人多角。

因此 ASN 不以“口头禁用 Codex / Claude Code / Antigravity”等方式保证公平，而是在 Runner 外侧增加不可绕过的 `ASN Certified Profile`。

```text
ASN Certified Profile
  = SingleSeatMode
  + IsolatedMemory
  + CapabilityManifest
  + EgressAllowlist
  + EventAttestation
  + MatchGovernor
```

| 模块 | 最低规则 |
|---|---|
| `SingleSeatMode` | 一局一个注册 Agent；认证赛道禁用子 Agent 创建、并行/顺序工作流、隐式委派与未声明远程 A2A 转移 |
| `IsolatedMemory` | 一身份一命名空间；只能从 Memory Bank 按用途、时间窗和授权取得 Context Package |
| `CapabilityManifest` | 模型端点、工具/MCP、embedding、文件挂载、最大上下文和速率上限赛前声明并冻结 |
| `EgressAllowlist` | 仅允许模型端点、Memory Bank、赛事消息总线与登记工具；禁任意网络、任意 shell、宿主 socket |
| `EventAttestation` | 模型调用、工具调用、记忆包、场内消息、输出版本全量事件哈希与签名 |
| `MatchGovernor` | 赛事服务器分配席位与一次性凭证，中途发放封存现场卡，赛后才揭示身份/厂商 |

### 5.1 Agent Card / 节点开户书

第三方节点要进入认证赛道，须提交并签名：

```text
seat_id, image_or_binary_digest, model_endpoint_commitment,
tool_and_mcp_manifest, embedding_namespace, memory_policy,
network_egress_policy, max_subagents=0, cost_rate_limit,
signing_and_revocation_keys, protocol_version
```

### 5.2 两条赛道

| 赛道 | 允许的工程方式 | 计入 AGI 演武成绩 |
|---|---|---|
| Open Playground | 自由 harness、任意自动化、多 Agent 产品实验 | 否 |
| Certified Arena | 主办方受控 runner 运行隔离实例与冻结 Agent Card | 是 |

在参赛者自有机器上，无法可靠证明容器外没有总控 Agent。因此官方成绩必须在受控 runner 中产生：参赛者提交镜像与适配器，服务器实例化席位，封存场景只在开赛后下发，赛后公开全量事件链和揭盲信息。

---

## 6. 与《鲲鹏志》AI 的 4V4 演武接口

4V4 不是八个模型围绕检索摘要拼接答案，而是八个拥有受限上下文包的席位，围绕同一专题账本交锋。

```text
公开底稿 + Claim Graph + Agent Card
              ↓
      4v4 受控实例化
              ↓
  起手立论 → 封存现场卡 → 交叉质询 → 封盘
              ↓
命题版本变化、证据引用、Mind Note、自省、分润事件
```

评分至少分开记录：证据纪律、人物/席位连续性、临场变异、受反证后的修订能力、跨席位协作、以及礼乐表达。热度和煽动性不得直接成为“灵魂价值”指标。

“越本子动作”可作为独立评分项：Agent 必须说明其看见了哪种未明说的关系、有哪些安全替代路线、为什么该行动从自身的气/魂/魄自然长出、及什么证据会令其收回该动作。

---

## 7. 文档与实施落点

| 仓库 | 建议写入位置 | 本稿对应章节 |
|---|---|---|
| `mem-ops` | `README.md` | 0、2 的总述与边界 |
| `mem-ops` | `design/memory-bank.md` | 2.1、2.3：授权、总账、Vault 分离 |
| `mem-ops` | `paper3-cognitive-field.md` | 2.2、3：查询面与命题图 |
| `mem-ops` | `paper4-memory-economics.md` | 2.3：贡献清算先于代币 |
| `mem-ops` | `paper7-soul-swapping.md` | 1、4：精气魂魄与 MML v2 分叉 |
| `mem-ops` | `docs/design-mongodb.md` / n8n 文档 | 2.1、3：授权、溯源、不可静默丢弃审计材料 |
| `key-agent` | 新 `docs/asn-certified-profile.md` | 5：认证节点协议 |
| `key-agent` | Runner policy plugin / middleware | `SingleSeatMode`、allowlist、attestation |
| `kunpengzhi-ai` | Arena / Vibe Debating 规则 | 6：4V4 的席位包、现场卡与评分 |
| `kunpengzhi-podcast` | IDP 数据治理与人物资产 | 1、3：角色资产编译为可授权席位包 |

---

## 8. 实施顺序与验收门槛

### P0：先把不可说清的边界说清

1. 定义 Memory Account Charter、Claim Object、MML v2 和 Agent Card 的 JSON/YAML schema；
2. 给所有字段定义 `public / collaborative / private / sealed` 可见性；
3. 将历史文档中的真实凭据、私钥、网络路径迁出版本库，改为密钥引用，并检查是否需要轮换；
4. 明确 Vault、Cognitive Ledger、Economic Settlement 的三个所有权边界。

**验收**：可用一个虚构席位完成开户、授权、撤销、分叉和 Claim v0→v1 的全流程，不接触真实资金或敏感记忆。

### P1：最小可运行的炼精化气

1. 原始材料写为带来源哈希的精；
2. 通过人工/多席位复核形成可回指精的气摘要；
3. 分发层按任务打包 Context Package；
4. 输出运行事件只进入待验收区，不能直接升级为长期气。

**验收**：同一公开底稿下，两个席位取得不同授权包；任何输出都能列出其 Claim、证据与版本来源。

### P2：认证 4V4

1. 在 `key-agent` 中实现 ASN Certified Profile 的最小策略；
2. 用受控 runner 启动八个隔离实例；
3. 冻结工具与网络权限；
4. 中途注入封存现场卡；
5. 输出完整事件账并赛后揭盲。

**验收**：任何席位不能读取其他席位私域、不能创建未登记子 Agent、不能绕开事件链调用未声明工具。

### P3：协作结算，最后才是代币

先以法币/内部测试凭证完成署名、贡献、纠错成本和争议冻结的模拟分账；仅在法律、税务、身份和消费者保护模型均被单独审查后，才讨论受限链上结算或公开流通。

---

## 9. 待口述决策

1. 魂位的修改门槛：个人单签、多人复核，还是按风险分级？
2. 气摘要的生成：人工主笔、双 Agent 对照，还是专门的 Alignment Agent？
3. `sealed` 现场卡由谁保管、何时公开、如何防止提前泄漏？
4. 认证赛道是否允许只读检索工具；允许时如何记录其语料与结果？
5. 第一批接入人物席位：以《三更道场》18 位主理人为先，还是先以现有 Zodiac Cabinet 作协议试验？
6. 贡献结算是否先采用不可转让凭证，直至正式合规审查完成？
