# Contributing

本仓库用于 AC-driven PeLED / quasi-2D PeLED 研究流程。贡献应提高可追溯性、可复现性或审查质量，不追求复杂框架。

## 修改前

1. 先阅读 `00_SYSTEM/project_rules.md`、`workflow.md` 和 `folder_policy.md`。
2. 使用对应 issue template 描述问题、证据和影响范围。
3. 不新增一级目录；`.github/` 仅用于 GitHub 配置。
4. 不提交 PDF、图片、真实原始数据、凭据或仪器导出二进制文件。

## Paper Card

- 使用 `01_PAPERS/paper_card_template.yaml`。
- 缺失信息写 `Not explicitly specified in text`。
- claim 必须有 `evidence_locator`。
- direct evidence、indirect support、author hypothesis 分开。
- 提交前运行 Critic Agent，并更新 `critic_status`。

## Protocol

- protocol 必须对应明确的 AC-driven PeLED / quasi-2D PeLED 场景。
- 新增或修改参数时同步检查 controls、replicates、statistics、failed-device policy 和 exclusion criteria。
- 不把 synthetic example parameter 写成推荐条件。
- 不编造设备能力或论文未报告参数。

## Data Analysis

- Python 依赖仅限 `pandas`、`numpy`、`matplotlib`。
- raw data 保持只读；处理步骤与参数必须记录。
- example CSV 必须标明 synthetic，不得来自真实未公开实验。
- 不提交运行生成的图片、JSON 或 processed outputs。

## Pull Request Checklist

- 变更范围小且与 issue 对应。
- YAML 可解析，CSV header 符合标准，Python 可运行。
- 没有空文件、临时文件、PDF、图片或敏感信息。
- 未删除既有规则；行为变化已更新 README/workflow。
- PR 描述包含验证命令与结果。
