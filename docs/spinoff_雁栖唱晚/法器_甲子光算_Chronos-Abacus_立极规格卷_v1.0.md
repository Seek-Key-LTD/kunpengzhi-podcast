# 《甲子光算》（Chronos-Abacus）立极规格卷 v1.0

**三更道场·案头主动总线感应法器立项与工程基准**  
*专属学者席位：渔阳（于鲜洋 · 央财大账房）*

---

## 1. 宗旨与器物定义

* **器物定性**：三更道场案头核心法器、可触摸的离散时序校验总线。
* **一句话定义**：**珠动辨事，杆照知神；光不是装饰，光是校验和。**
* **核心哲学分层**：
  * **珠（人事 / 状态）**：离散状态累加与周期行进。
  * **梁（法界 / 门槛）**：靠梁生效，离梁归虚；霍尔磁感无接触采样。
  * **杆（天道 / 奇偶律）**：主动显示阴阳双态，承担实时奇偶校验。
  * **光（敕令 / 校验和）**：合法则定，非法则拒；以光显相，自证自律。

---

## 2. 数学骨架与代数校验逻辑

六十甲子非 $10 \times 12 = 120$ 的直接笛卡尔积，而是由十干与十二支同步轮转的最小公倍周期锁定：

$$\operatorname{lcm}(10, 12) = 60$$

### 2.1 零点基准与奇偶律（Parity Law）

以 **甲子** 为绝对坐标零点：

$$\text{Index} = 0, \quad \text{Stem} = 0 (\text{甲}), \quad \text{Branch} = 0 (\text{子})$$

系统判定合法性必须严格满足 **同奇偶约束**：

$$\operatorname{parity}(\text{Stem}) \equiv \operatorname{parity}(\text{Branch}) \pmod 2$$

* **阳态（明）**：$\text{Index} \equiv 0 \pmod 2$（偶数位）。光态清亮稳定，显向外之象（甲子、丙寅、戊辰、庚午、壬申……）。
* **阴态（暗）**：$\text{Index} \equiv 1 \pmod 2$（奇数位）。光态幽暗低亮，显向内之象（乙丑、丁卯、己巳、辛未、癸酉……）。
* **非法配对（断绝）**：$\operatorname{parity}(\text{Stem}) \neq \operatorname{parity}(\text{Branch})$。触发异相拦截（如甲丑、乙子），光态立即进入告警。

---

## 3. 核心机械与档位拓扑（甲子核心版）

采用双档并行结构，两档独立拨动，机械自由，法则刚性。

### 3.1 天干档（十态：$0 \sim 9$）

* **下室**：5 颗下珠，单珠权值 $= 1$（覆盖 $0 \sim 5$ 步长，实际靠梁取值 $0 \sim 4$，满 5 进上）。
* **上室**：1 颗上珠，单珠权值 $= 5$。
* **表达域**：$0 \sim 9$ 对应 `甲(0), 乙(1), 丙(2), 丁(3), 戊(4), 己(5), 庚(6), 辛(7), 壬(8), 癸(9)`。

### 3.2 地支档（十二态：$0 \sim 11$）

* **下室**：5 颗下珠，单珠权值 $= 1$（覆盖 $0 \sim 5$ 步长）。
* **上室**：1 颗上珠，单珠权值 $= 6$（半周天阴阳跳跃）。
* **表达域**：$0 \sim 11$ 对应 `子(0), 丑(1), 寅(2), 卯(3), 辰(4), 巳(5), 午(6), 未(7), 申(8), 酉(9), 戌(10), 亥(11)`。

---

## 4. 传感与硬件链路架构

```
[ 磁芯算珠 (NdFeB) ]
         │ (滑移靠梁)
         ▼
[ 横梁内嵌微型线性/开关霍尔阵列 (Hall Array) ]
         │ (离散有效态读取: 1/0)
         ▼
[ 低功耗微控制器 (MCU: ESP32-S3 / RP2040) ]
         │
         ├── 1. 计算 Stem_Val 与 Branch_Val
         ├── 2. 校验 Parity(Stem) == Parity(Branch)
         └── 3. 查表计算六十甲子绝对偏移
         │
         ▼
[ 驱动底板恒流芯片 (PWM / I2C Driver) ]
         │
         ▼
[ 档杆底部可寻址 Micro-LED (石英/雾面玉质光导纤维) ]
```

### 4.1 接触与传感准则

* **绝对杜绝物理滑动电阻/弹片**：避免手汗、氧化、物理磨损引起的阻抗漂移。
* **单阈值靠梁判定**：感应点设在紧贴横梁的木槽内，算珠只有紧密贴梁才触发状态更新；行程中途处于悬空浮动态，MCU 执行迟滞滤波，杜绝信号抖动。

### 4.2 供电与外观约束

* **外观零开孔**：无外露 USB 口，底座内置 Qi 标准无线受电线圈与扁平锂电池。
* **暗置唤醒**：内置微加速度计/微震动传感器，案头有扣击或算珠拨动即瞬间唤醒；长置 300 秒无动作自入休眠（玉色尽敛）。

---

## 5. 光学语汇与时序状态机

导光杆为高透石英棒或亚光雾化人造玉石，底部注入双色微型发光核心（冷白 / 琥珀）。

| 系统状态 | 数学判定 | 导光杆视觉呈现 | 语义指示 |
| --- | --- | --- | --- |
| **纯阳位** | $\text{Stem} \equiv \text{Branch} \equiv 0 \pmod 2$ | **双杆极清冷白高光**（恒定流明 100%） | 阳道顺行，气象外显 |
| **纯阴位** | $\text{Stem} \equiv \text{Branch} \equiv 1 \pmod 2$ | **双杆玄玉幽光**（30% 亮度，缓慢呼吸） | 阴道内敛，气象潜藏 |
| **非法位** | $\text{Stem} \not\equiv \text{Branch} \pmod 2$ | **双杆短促琥珀频闪**（3Hz，闪 3 次后自灭） | 错配逆乱，拒绝入历 |
| **归元零位** | $\text{Stem} = 0 \text{ 且 } \text{Branch} = 0$ | **双杆自梁心向两极涌动光芒**后定于纯阳 | 甲子开天，立极复始 |

---

## 6. 物理材质工艺规范

1. **盘体外框与中梁**：雷击枣木、乌木或深沉老红木，手工擦生漆，亚光黑褐色，吸收散色杂光。
2. **导光档杆**：光学级高纯度石英玻璃棒，外径 4.0mm，表面微酸洗雾化，光线柔和匀亮。
3. **下室五行珠（五色五行）**：
   * **木（1位）**：绿松石 / 斑竹
   * **火（2位）**：朱砂琉璃 / 红玛瑙
   * **土（3位）**：蜜蜡 / 沉香木
   * **金（4位）**：纯银 / 砗磲 / 白铜
   * **水（5位）**：黑曜石 / 乌木
   * *注：每颗珠体内部精密铣孔，封胶预埋 N52 微型微米钕磁体，配重完全均一。*

---

## 7. 仓库落地方案与代码规范（Agent Implementation Tasks）

交由工程团队与代码 Agents 执行时，仓库结构按以下模块初始化：

```text
chronos-abacus/
├── firmware/                 # 固件源码 (C / Rust for embedded)
│   ├── src/
│   │   ├── main.rs           # 状态机主循环
│   │   ├── hall_matrix.rs    # 磁感应离散去抖驱动
│   │   ├── calendar_engine.rs# 干支对齐、CRT算法与模校验
│   │   └── optical_bus.rs    # PWM/LED 阴阳光效驱动
├── hardware/                 # 硬件工程 (KiCad / CAD)
│   ├── pcb/                  # 霍尔阵列板与主控母板原理图
│   └── enclosure/            # 枣木外框与石英导管 3D 机械工程图
├── docs/                     # 哲学架构与立项文档
│   └── specification_v1.0.md # 本规格文档
└── tests/                    # 算法仿真测试
    └── test_sixty_cycle.py   # 60甲子穷举与非法态遍历验证脚本
```

### 核心校验算法参考实现（`calendar_engine`）

```python
def verify_chronos_state(stem: int, branch: int) -> dict:
    """
    stem: 0~9 (甲~癸)
    branch: 0~11 (子~亥)
    """
    if not (0 <= stem <= 9 and 0 <= branch <= 11):
        return {"valid": False, "error": "RANGE_OUT_OF_BOUNDS"}

    # 1. 奇偶一致性校验 (Parity Law)
    is_stem_even = (stem % 2 == 0)
    is_branch_even = (branch % 2 == 0)

    if is_stem_even != is_branch_even:
        return {
            "valid": False,
            "light_state": "AMBER_FLASH",
            "error": "PARITY_MISMATCH"
        }

    # 2. 计算六十甲子绝对索引 (CRT 映射)
    # index ≡ stem (mod 10), index ≡ branch (mod 12)
    # index = (6 * stem - 5 * branch) % 60
    index = (6 * stem - 5 * branch) % 60

    # 3. 判定阴阳光态
    light_state = "YANG_BRIGHT" if (index % 2 == 0) else "YIN_BREATH"

    return {
        "valid": True,
        "index": index,
        "polarity": "YANG" if (index % 2 == 0) else "YIN",
        "light_state": light_state
    }
```
