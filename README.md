# AC-PeLED Research Agents

这是一个面向 **AC-driven PeLED、quasi-2D PeLED、perovskite LEDs 与 optoelectronic materials** 的科研 agent 工作流。项目借鉴 ChemAgents 的 `multi-agent + tool + protocol library` 思想，但不依赖机器人硬件，也不调用其未公开的 Literature Database、Protocol Library、Model Library 或 Robot API。

本仓库的目标是用清晰、可审计的文件契约统一管理文献阅读、实验 protocol、数据分析、机理判断和研究日志。第一版刻意保持简单：Markdown/YAML 负责知识与流程，Python 负责可复现的数据计算。

## Quick Start

### First paper card

1. 复制 `01_PAPERS/examples/example_paper_card.yaml`，用 paper ID 重命名。
2. 根据全文、Supporting Information 和 figures 填写 `01_PAPERS/paper_card_template.yaml` 定义的字段。
3. 每条 evidence 写入 `evidence_locator`，定位到 page、section、figure、table 或 supporting item。
4. 未在来源中明确说明的信息写 `Not explicitly specified in text`。
5. 使用 `04_AGENTS/critic_agent.md` 审核，并更新 `critic_status`。

### First protocol

1. 从 `02_PROTOCOLS/` 选择与 research question 最接近的模板。
2. 参考 `02_PROTOCOLS/examples/example_filled_pn_half_cycle_protocol.yaml` 理解填写粒度；该示例仅含 synthetic parameters，不代表推荐实验条件。
3. 用已核验的设备与实验参数替换 `Not explicitly specified in text`。
4. 在执行前锁定 replicates、statistics、failed-device policy、exclusion criteria 与 controls。

### First data analysis

1. 安装最小依赖：`python -m pip install -r requirements.txt`。
2. 阅读 `03_DATA_ANALYSIS/data_format_standard.md`，确认 CSV header 与 metadata。
3. 按 `03_DATA_ANALYSIS/run_example_analysis.md` 运行 synthetic waveform 与 stability examples。
4. 把脚本输出放在本地 analysis output 目录，不提交生成的图片、JSON 或 processed data。

## Recommended v0.1 Workflow

1. Read paper → paper card
2. Add comparison row
3. Update mechanism map
4. Translate gaps into protocol controls
5. Use pilot experiment plan
6. Complete pre-experiment checklist before any AC-PeLED experiment

## 项目目标

- 用 `paper card` 结构化文献，而不是只写自由文本总结。
- 用可复用 protocol 约束实验规划，避免遗漏关键条件。
- 用 agent prompts 分离阅读、机理、实验、分析、优化与 critic 职责。
- 强制区分 `direct evidence`、`indirect support` 和 `author hypothesis`。
- 对论文未明确说明的信息统一写 `Not explicitly specified in text`。
- 为后续 Codex、ChatGPT、Zotero/Obsidian 和 Bayesian optimization 留出清晰接口。

## 目录结构

```text
.
├── 00_SYSTEM/         # 项目规则、工作流与目录政策
├── 01_PAPERS/         # paper card、阅读 prompt、comparison table
├── 02_PROTOCOLS/      # 可复用实验 planning templates
├── 03_DATA_ANALYSIS/  # 数据格式与分析脚本
├── 04_AGENTS/         # 各角色的 agent prompts
└── 05_REPORTS/        # 文献、实验与周报模板
```

不要随意新增一级目录。实际论文资料、实验原始数据与图片应放在团队另行约定的受控存储位置，并在报告中记录路径；不要堆在仓库根目录。

## 如何读一篇新 paper

1. 复制 `01_PAPERS/paper_reading_prompt.md`，连同论文全文或可核验文本交给 ChatGPT/Codex。
2. 逐图检查 figures、caption、Methods 和 Supporting Information。
3. 先完成 `paper_card.yaml`，再写阅读报告。
4. 运行 `04_AGENTS/critic_agent.md` 中的检查清单。
5. 未在正文明确出现的信息写 `Not explicitly specified in text`，不要凭领域常识补齐。

## 如何建立 paper card

1. 复制 `01_PAPERS/paper_card_template.yaml` 并以可追踪的 paper ID 命名。
2. 填写 bibliographic、material、device、driving condition、performance 和 evidence。
3. 对每个关键 figure 记录它支持的 claim 与 caveat。
4. 把作者解释放入 `author_hypothesis`，不要混入 `direct_evidence`。
5. 保存前检查 YAML 缩进与字段完整性。

## 如何更新 comparison table

1. 只从已完成且经 critic 检查的 paper card 取值。
2. 在 `01_PAPERS/comparison_table_template.md` 增加一行。
3. 单位保持一致；无法统一时在单元格中保留原单位并标注。
4. `Mechanism Claim` 与 `Direct Evidence` 分列记录。
5. 缺失条件集中写入 `Missing Details`，避免把空白误当成零或无效。

## 如何根据 research question 调用 protocol

1. 用 `04_AGENTS/research_manager.md` 把 research question 改写为可检验问题。
2. 根据变量选择 `02_PROTOCOLS/` 中最接近的模板。
3. 复制 protocol，逐项核验并用真实实验参数替换 `Not explicitly specified in text`。
4. 明确 independent variables、controlled variables、controls、measurements 与 stopping criteria。
5. 在实验开始前由 `critic_agent` 检查 waveform、frequency、voltage、detector bandwidth、atmosphere、encapsulation 和 device area。

## 如何分析实验数据

数据必须遵循 `03_DATA_ANALYSIS/data_format_standard.md`，并配套 metadata。

```bash
python 03_DATA_ANALYSIS/analyze_el_waveform.py waveform.csv --output-dir analysis
python 03_DATA_ANALYSIS/calculate_pn_ratio.py waveform.csv
python 03_DATA_ANALYSIS/plot_stability.py stability.csv --output stability.png
```

脚本输出是计算结果，不自动等同于物理机理。任何机理解释都要回到 control、仪器带宽、相位同步和误差来源。

## 如何生成 weekly research log

1. 复制 `05_REPORTS/weekly_log_template.md`。
2. 汇总本周新增 paper cards、comparison table 变化、实验计划与分析结果。
3. 对每个结论写明证据等级和待验证问题。
4. 将下周行动写成可执行任务：输入、输出、负责人和完成标准。

## 未来扩展

- **Bayesian optimization**：在数据量、变量定义和质量控制成熟后接入。
- **Zotero/Obsidian integration**：同步 citation metadata、paper card 与机制笔记。
- **Codex automation**：自动检查 YAML/CSV 格式、生成周报草稿和运行分析脚本。

## 研究边界

本仓库是研究组织与分析工具，不替代仪器校准、实验安全流程、作者原文核验或领域专家判断。严禁从 PLQY/TRPL 直接推导 EL/EQE 提升，也不得混淆 AC-driven PeLED、DC PeLED 与 OLED 的工作机制。
