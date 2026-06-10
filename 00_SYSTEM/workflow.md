# Research Workflow

```text
New Paper
→ paper_card.yaml
→ mechanism chain
→ comparison table
→ possible experiment idea
→ protocol matching
→ experiment plan
→ data analysis
→ report / weekly log
```

| Step | Input | Output | 检查标准 |
|---|---|---|---|
| New Paper | 全文、Supporting Information、可信 metadata | 可追踪 paper ID 与来源 | 标题、DOI、版本和附件范围可核验 |
| paper card | 论文文本与 figures | 完整 `paper_card.yaml` | 所有字段存在；缺失信息使用指定文本 |
| mechanism chain | paper card、关键 figures | Material–Structure–Carrier–Device chain | 每个箭头标注 evidence level，不跳跃归因 |
| comparison table | 已审核 paper card | 新增 comparison row | 单位一致；claim 与 evidence 分列 |
| experiment idea | research gap、可迁移 protocol | 可证伪 hypothesis | 指明变量、control、预期结果与替代解释 |
| protocol matching | research question、设备能力 | 选定并填写的 YAML protocol | 执行前用已核验参数替换所有缺失信息标记 |
| experiment plan | protocol、样品与仪器清单 | 可执行 run plan | 顺序、重复数、metadata、停止条件明确 |
| data analysis | 原始 CSV 与 metadata | metrics、figures、异常记录 | 格式通过；无静默删点；单位和算法可追溯 |
| report / weekly log | 全部审核输出 | paper/experiment report 与 weekly log | critic checklist 完成，下一步可执行 |

## Gate 1: Paper Card

没有 paper card，不进入机理映射。只读 abstract 时必须在 `notes` 中标明证据范围，不能把 abstract-only extraction 当作全文结论。

## Gate 2: Experiment Readiness

protocol 中仍有 `Not explicitly specified in text`、缺少 control、设备能力未知或安全条件未确认时，不得开始实验。

## Gate 3: Interpretation

数据脚本只负责计算。将 phase lag、PN ratio、retention 或 spectral shift 解释为 ion migration、interfacial polarization 或 injection asymmetry 前，必须检查替代解释和仪器限制。

## Gate 4: Reporting

最终报告必须保留 missing details、negative results、异常数据和 critic 意见，不能只保留最优器件。

## Definition of Done

### Paper Card

paper card 只有在以下条件全部满足时才算完成：

- source scope 明确，记录使用了 full text、abstract、Supporting Information 和 figures 中的哪些部分。
- bibliographic、material、device、driving condition、performance 和 evidence 字段均已处理。
- 每个关键 claim 都有 evidence locator，能定位到 page、section、figure、table 或 supporting item。
- direct evidence、indirect support、author hypothesis 已分开。
- 所有缺失项写 `Not explicitly specified in text`。
- `critic_status` 为 `PASS`，或 required revisions 已关闭并可追溯。

### Experiment Plan

experiment plan 只有在以下条件全部满足时才算完成：

- research question、hypothesis 和 falsification criterion 明确。
- 已选定 protocol，关键参数不再保留 `Not explicitly specified in text`。
- variables、controls、replicates、statistics、failed-device policy 和 exclusion criteria 已预先定义。
- waveform、frequency、voltage、duty cycle、detector bandwidth、environment、device area 与 encapsulation 已确认。
- raw data naming、metadata、停止条件和安全依赖已记录。
- Critic Agent verdict 允许进入执行阶段。

### Data Analysis

data analysis 只有在以下条件全部满足时才算完成：

- raw data 保持只读，processed data 可由记录的步骤重新生成。
- 数据格式、单位、metadata、time base 和 instrument limits 已检查。
- baseline correction、smoothing、filtering、normalization 和 exclusions 均记录方法与参数。
- metrics、figures、异常与 failed devices 同时保留。
- observation、calculated metric 和 physical interpretation 已分开。
- analysis command、script version、input files 与 output files 可追溯。

### Weekly Log

weekly log 只有在以下条件全部满足时才算完成：

- 本周 paper cards、protocol changes、experiments 和 analyzed datasets 均有链接或路径。
- 新增机制判断标明 evidence level 与 unresolved alternative explanation。
- negative results、blocked items、missing parameters 和 critic findings 未被省略。
- 下周行动包含 input、expected output、owner 或 responsibility、completion criterion。
- 关键决策可追溯到 paper card、protocol、data analysis 或 issue。
