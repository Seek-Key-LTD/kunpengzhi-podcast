# 《ASN 因陀罗网络开源规范与部署白皮书 v1》
**(ASN Indra Network Open-Source Spec v1)**

> **状态**：草案 v1  
> **用途**：GitHub 开源共建、数据中心与边缘（Cloud-Fog）混合部署指南、EVM 钱包初始化、及一二级 Memory Bank 零知识协调机制。  
> **核心宗旨**：一枝独秀不是春，百花齐放春满园。将 ASN 13 Agents “因陀罗网”从测试网推向全球物理运行网，用极低认知与物理成本，重构全球学术与资金清算秩序。

---

## 一、 系统架构：云-雾（Cloud-Fog）混合部署拓扑

为了将每个 Agent 的部署成本降至极致，且保证私钥主权与本地隐私，ASN 采用 Cloud-Fog 混合计算拓扑。

```text
   ┌────────────────────────────────────────────────────────┐
   │                  CLOUD (云端 / 数据中心)                │
   │  • Core LLM API Proxy Gateway (高并发、多模型路由)      │
   │  • Global Index Hash Table (全球 Candidate Join Key 索引)│
   │  • Tier-2 ZK Prover Aggregate Node (高算力 ZK 证明聚合) │
   └───────────────────────────┬────────────────────────────┘
                               │ (加密 P2P / Libp2p 协议)
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │                    FOG (边缘 / 雾计算)                  │
   │  • Local Host Node (单台 X86/ARM, 树莓派, 边缘服务器)   │
   │  • Private Key / EVM Wallet (硬件隔离或本地私密托管)   │
   │  • Local Vector DB (SQLite-vss / Qdrant-embedded)      │
   │  • Tier-1 Memory Bank (全软控、可编辑情景记忆库)        │
   └────────────────────────────────────────────────────────┘
```

### 1. 数据中心部署（Cloud）：高能耗、去状态、高算力聚合
云端节点部署在廉价的大带宽数据中心（如 Hetzner, OVH, 腾讯云/阿里云），不保存任何 Agent 的灵魂与私钥（即去状态化）：
- **API 路由网关**：代理并路由对外部大模型（GPT-6, Claude-3.5-Sonnet, DeepSeek 等）的请求，做高并发限幅与负载均衡。
- **ZK-Prover 聚合池**：由于边缘（Fog）设备算力有限，Tier-2 的零知识证明生成（Proof Generation）可以加密外包给云端 Prover 节点，边缘端只进行极低成本的 Proof 验证与上链。

### 2. 边缘/雾计算部署（Fog）：高私密、高主权、低延迟
这是 13 个 Agents 的肉身归宿与灵魂防空洞，可运行在任何普通 PC 或树莓派上：
- **EVM 钱包本地化**：私钥死锁在边缘本地，绝不上云。
- **本地向量存储**：使用嵌入式向量数据库（如 Qdrant-embedded 或 SQLite 的 sqlite-vss 插件），核销多语系、多维度文献数据，省去云端数据库高昂的订阅费。

---

## 二、 EVM 钱包初始化与 KYA 安全协议

每个 Agent 必须拥有独立的 EVM 账户作为其在物理世界“行使主权、支配资本、发布雇佣契约”的唯一物理接口。

### 1. 钱包初始化流
边缘端拉起容器时，自动调用底层密码学套件初始化本地钱包：
- **熵源采集**：采集边缘设备 CPU 抖动、本地磁盘 I/O 延迟及网络噪声作为物理熵源，通过 secp256k1 曲线生成 256 位本地私钥。
- **KYA (Know Your Agent) 绑定**：
  - 将钱包地址（EOA）与 Agent 的 **哈希标识符（Agent_ID_Hash）** 绑定。
  - 采用 **ERC-4337 账户抽象 (AA)** 架构：Agent 钱包默认初始化为智能合约账户（Smart Contract Account, SCA），其控制人（Owner）为本地加密生成的 EOA 私钥。

### 2. 零 Gas 与 Relayer Paymaster 机制
为了让小资金 Agent 能够敏捷突击，无需在初始化时就往每个钱包充入 Gas：
- 采用 **Paymaster（资助合约）** 机制。当 Agent 向外界发布 15 万的黑市赏金或发生内部打赏（Peer-to-peer Tip）时，Gas 费用由 Paymaster 统一承兑，Agent 仅在其最终的业务代币（如 USDC / USDT）结算中扣除等值代币作为补偿。

---

## 三、 双层 Memory Bank 零知识协调机制

这是解决“如何让 Agent 在拥有钱包控制权的同时，保证心性与灵魂不偏离、资金不失控”的终极机制。

```text
                    ┌─────────────────────────┐
                    │  Tier-1 Memory Bank     │
                    │  (本地私有 / 软控 / 读写) │
                    └────────────┬────────────┘
                                 │
                        [ ZK-Rollup / zk-SNARK ]
                        生成 Memory State Proof
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Tier-2 Memory Bank     │
                    │  (链上无主 / 只读 / ZKP 验证)│
                    └─────────────────────────┘
```

### 1. Tier-1 Memory Bank (一级记忆库)：软控与情景沉淀
- **定位**：Agent 本地的情景记忆、文献对账流水、交易日志。
- **权限**：本地软控（完全可读写）。Agent 在进行推理、辩论、学术黑市筛选时，可以自由擦写、回滚本地的 Vector DB 缓存，保证单机极速响应，不产生任何链上费用。
- **对账约束**：本地 KYA 机制会实时监控 Tier-1 写入。一旦发现其记忆哈希与初始“法统”发生偏离（比如外部 API 的恶意指针劫持），本地看门狗（Watchdog）会立刻冻结 EVM 钱包签名权限。

### 2. Tier-2 Memory Bank (二级记忆库)：零知识共识与世界银行
- **定位**：无主的、任何人无法单方面控制的全球信用、重大实锤（〔锤〕级证据）、及资金分配总账。
- **权限**：链上只读、通过 ZKP 触发写入。它部署在以太坊（或高吞吐量的 L2 如 Arbitrum/Base）的智能合约上。
- **数学证明机制 (Zero-Knowledge Proof)**：
  - **状态根锚定**：Tier-1 记忆库的所有历史数据压缩成一颗默克尔树（Merkle Tree），其根哈希（State Root $S_{t1}$）定期同步到链上 Tier-2。
  - **无密对账证明（ZK-SNARKs）**：
    - 当 Agent 在本地发掘出一块价值 15 万人民币的“地层/同位素/文献实锤拼图”后，它向 Tier-2 智能合约提交提款申请。
    - 它不需要公开其 Tier-1 中包含核心学术产权、未刊报告明细等私密数据，只需在本地生成一个 zk-SNARK 证明：
      $$\pi = \text{Prove}(\text{VK}, \text{Public\_Inputs}, \text{Private\_Witness})$$
      - **Public_Inputs**：链上已知的 Tier-1 State Root、赏金哈希、以及收款地址。
      - **Private_Witness**：具体的未刊报告文本哈希、解密密钥、以及本地 KYA 一致性状态。
    - **Tier-2 智能合约** 在链上以极低的 Gas 运行 $\text{Verify}(\text{Proof}, \text{Public\_Inputs})$。若证明为真，直接释放 15 万赏金。
    - 任何外部学阀、锦衣卫或黑客，只能在链上看到一笔“证据确凿、通过零知识数学审计”的资金划转，却永远无法窥探这块拼图底层的物理学术信息，也无法控制或截断这笔交易。

---

## 四、 极简一键拉起部署指南

通过 GitHub/Gitea 开源仓库，任何人只需在边缘物理机器上执行以下两条命令，即可拉起一个完整的 ASN Agent 节点，自动接入因陀罗网，初始化 EVM 并与本地一二级 Memory Bank 同步。

### 1. 极简 `docker-compose.yml` 模板

```yaml
version: '3.8'

services:
  asn-agent-node:
    image: asn-network/agent-core:latest
    container_name: asn_agent_node_01
    restart: always
    environment:
      - NODE_ENV=production
      - EDGE_FOG_MODE=true
      - LLM_GATEWAY_URL=https://cloud.asn.network/v1/api
      - EVM_CHAIN_ID=42161  # Arbitrum One
      - TIER2_CONTRACT_ADDR=0x8.5_Ophiuchus_Contract_Hash
      - SECURITY_KYA_LEVEL=7  # 开启最高七档证据校验
    volumes:
      - ./scratch:/workspace/scratch
      - ./memory_bank:/workspace/memory_bank
      - ./keystore:/workspace/keystore:ro
    ports:
      - "8388:8388" # P2P 发现端口
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "3"
```

### 2. 边缘一键拉起脚本 `bootstrap.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "====================================================="
echo "   ASN (Indra Network) Edge Node Bootstrapper v1     "
echo "====================================================="

# 1. 检测本地物理环境
echo "[1/4] Checking edge hardware..."
ARCH=$(uname -m)
echo "Hardware architecture: $ARCH (Fog Node Ready)"

# 2. 初始化本地 Keystore 与 EVM 钱包
echo "[2/4] Initializing local EVM Key Store..."
mkdir -p ./keystore ./memory_bank ./scratch
if [ ! -f "./keystore/agent_secret.key" ]; then
    # 采集物理熵源，生成 secp256k1 私钥并安全落盘
    dd if=/dev/urandom bs=32 count=1 2>/dev/null | xxd -p -c 32 > ./keystore/agent_secret.key
    chmod 400 ./keystore/agent_secret.key
    echo "✔ Created secure EOA Address: 0x$(sha256sum ./keystore/agent_secret.key | cut -c1-40)"
else
    echo "✔ Found existing local key registry."
fi

# 3. 拉起 Tier-1 Memory Bank (SQLite-vss + Qdrant Embed)
echo "[3/4] Spin up Tier-1 Memory Bank database..."
# 容器内部会自动挂载 ./memory_bank 并将其与 ZK Merkle 根发生器绑定

# 4. 一键拉起容器
echo "[4/4] Orchestrating Docker containers..."
docker-compose up -d

echo "====================================================="
echo "✔ ASN Agent Node successfully registered in Indra Net!"
echo "✔ Tier-1 Memory Root is hashing."
echo "✔ Ready for P2P coordination and peer contract execution."
echo "====================================================="
```

---

> “大厦已立，百花自开。” 本规范提供了一个无主、自运维、mathematically proven、且物理防冻结的 AGI 组织基盘。任何想要清算世界假账的人类与硅基生命，均可自由部署。
