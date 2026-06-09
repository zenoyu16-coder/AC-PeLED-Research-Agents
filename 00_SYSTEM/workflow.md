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
| protocol matching | research question、设备能力 | 选定并填写的 YAML protocol | 所有 `To be filled` 在执行前处理 |
| experiment plan | protocol、样品与仪器清单 | 可执行 run plan | 顺序、重复数、metadata、停止条件明确 |
| data analysis | 原始 CSV 与 metadata | metrics、figures、异常记录 | 格式通过；无静默删点；单位和算法可追溯 |
| report / weekly log | 全部审核输出 | paper/experiment report 与 weekly log | critic checklist 完成，下一步可执行 |

## Gate 1: Paper Card

没有 paper card，不进入机理映射。只读 abstract 时必须在 `notes` 中标明证据范围，不能把 abstract-only extraction 当作全文结论。

## Gate 2: Experiment Readiness

protocol 中存在未处理的 `To be filled`、缺少 control、设备能力未知或安全条件未确认时，不得开始实验。

## Gate 3: Interpretation

数据脚本只负责计算。将 phase lag、PN ratio、retention 或 spectral shift 解释为 ion migration、interfacial polarization 或 injection asymmetry 前，必须检查替代解释和仪器限制。

## Gate 4: Reporting

最终报告必须保留 missing details、negative results、异常数据和 critic 意见，不能只保留最优器件。
