# Project Rules

## 结构规则

1. 不允许随意新增一级目录；结构变更必须先更新本文件与 `workflow.md`。
2. 每篇文献必须先生成 `paper_card.yaml`，再写阅读报告。
3. 每个实验必须先对应一个 `02_PROTOCOLS/` 中的 protocol。
4. 每个数据文件必须配 metadata，至少记录 sample ID、device stack、日期、仪器、操作者、环境与 driving condition。
5. 根目录不存放 PDF、图片、原始数据或临时文件。

## 事实与证据规则

- 论文未明确说明的信息统一写：`Not explicitly specified in text`。
- 禁止把作者推测、示意图或 discussion 写成已证实事实。
- 禁止把 PLQY/TRPL 改善直接等同于 EL/EQE 提升。
- 禁止混淆 AC-driven PeLED、DC PeLED、OLED 的载流子注入、复合和极化机制。
- 所有图表解释必须分为：
  - `direct evidence`：图表直接测量并支持的现象。
  - `indirect support`：与 claim 一致但不能单独证明 claim 的结果。
  - `author hypothesis`：作者提出、尚需额外实验验证的解释。
- champion value 只能作为单器件结果，不能替代统计分布、重复性和 stability protocol。

## 实验规则

- 开始实验前必须填写 waveform、frequency、voltage amplitude、duty cycle 与 measurement environment。
- time-resolved EL 必须记录 detector bandwidth、sampling rate、触发方式和 current synchronization。
- 稳定性结果必须记录 brightness condition、atmosphere、encapsulation、device area 与 lifetime definition。
- 每个因果判断至少需要一个合适 control device 或 control condition。
- 不得假定设备具有未确认的同步、带宽、温控或光谱响应能力。

## Agent 输出规则

- Agent 只能基于提供的论文、数据和明确的项目记录工作。
- 缺失信息不得从记忆、相似论文或常识自动补齐。
- 所有建议必须标注输入依据、假设、风险和下一项验证。
- `critic_agent` 审核未通过的内容不得进入最终报告。
