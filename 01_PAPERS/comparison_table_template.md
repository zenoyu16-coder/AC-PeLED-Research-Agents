# Literature Comparison Table

只从已审核的 paper card 更新本表。单位不一致时不得直接横向比较。

> PeLEFET、OLED、PeLED 与 material-only studies 不得视为等价证据；跨 architecture 迁移时必须降级为 background context 或 indirect support，并写明限制。

| Paper | Source Status | Architecture Scope | Device Type | Stack | EML | Driving Mode | Frequency | Voltage | Positive/Negative EL | Key Metric | Stability | Mechanism Claim | Evidence Strength | Direct Evidence | Comparator Matching Basis | Transferable Variable | Required Control | Equipment Needed | Risk if Transferred | Missing Details | Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paper ID / DOI | VERIFIED / UNVERIFIED | PeLED / PeLEFET / OLED / material-only | AC PeLED / DC PeLED / other | Full stack | Composition / dimensionality | Waveform + polarity | Value + unit | peak / p-p / RMS | $I_+$, $I_-$, $R_{PN}$ | EQE / luminance / EL peak | T50 / T80 + protocol | Author claim | direct / indirect / hypothesis / background | Figure/table-backed evidence | luminance / current / power / charge / Not explicitly specified in text | Layer / composition / waveform / process | Reference or discriminating control | Instrument and bandwidth | Confounder / incompatibility / safety | Not explicitly specified in text | High / medium / low + reason |

## 更新检查

- Source Status 是否有 DOI 与 bibliographic metadata 核验依据？
- Architecture Scope 是否避免把 PeLEFET、OLED、PeLED 或 material-only 结果等价处理？
- Driving mode 与 voltage definition 是否清楚？
- Positive/Negative EL 是 peak 还是 integrated intensity？
- Stability 是否包含初始亮度、环境与封装？
- Mechanism claim 是否与 direct evidence 分开？
- Comparator Matching Basis 是否明确，且足以支持横向比较？
- Transferable Variable 是否可独立改变，并有 Required Control？
- Equipment Needed 是否包含 bandwidth、synchronization 或 environment 限制？
- Risk if Transferred 是否说明材料、器件或 measurement incompatibility？
- 是否保留 missing details 与 limitation？
