# Literature Search Protocol

## 目标

为 AC-driven PeLED、quasi-2D PeLED、ion migration、interfacial polarization、positive/negative half-cycle EL 与 operational stability 建立可复现的文献检索和来源核验流程。

## 检索范围

- 数据库或入口：Web of Science、Scopus、Crossref、publisher pages、Google Scholar。
- 文献类型：primary research 为主；review 仅用于背景和追踪原始来源。
- Architecture scope：PeLED、PeLEFET、OLED、material-only 分开标记，不视为等价证据。
- 未明确支持的参数统一写 `Not explicitly specified in text`。

## 建议检索式

```text
"perovskite light-emitting diode" AND ("alternating current" OR bipolar OR pulsed)
"perovskite light-emitting diode" AND ("ion migration" OR "interfacial polarization")
"quasi-2D" AND PeLED AND (degradation OR "efficiency roll-off")
perovskite AND electroluminescence AND ("positive half-cycle" OR "negative half-cycle")
PeLED AND ("operational stability" OR T50 OR T80)
```

## 筛选规则

### Include

- DOI 或 authoritative metadata 可核验。
- 研究对象与 architecture scope 可判断。
- 至少有 abstract；mechanism claim 需要 full text、figures 或 Supporting Information 才能升级证据等级。

### Exclude or downgrade

- DOI 与 title/authors/journal/year 不匹配。
- 无法确定真实来源。
- PeLEFET、OLED 或 material-only 结果被直接当作 PeLED 机制证据。
- 只有 secondary summary，且无法回到 primary source。

## Source Verification

对每个候选来源记录：

1. DOI resolution。
2. title、authors、journal、year metadata match。
3. source scope：abstract / full text / figures / Supporting Information。
4. architecture scope。
5. claim evidence class：`direct evidence`、`indirect support`、`author hypothesis`、`background context`。
6. evidence locator 与 unresolved uncertainty。

## 输出

- 经核验的 `paper_card.yaml`。
- 更新后的 `comparison_table_template.md` 实例。
- `05_REPORTS/source_verification_report.md` 格式的核验报告。
- 无法核验或证据不足的项目保留为 `UNVERIFIED`，不得静默补齐。
