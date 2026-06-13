# AC-PeLED Pre-Experiment Checklist

- Experiment ID: `To be filled`
- Date / operator: `To be filled`
- Device batch: `To be filled`
- Groups: DC baseline / bipolar AC / optional unipolar pulsed

## 1. Device Readiness

- [ ] Device IDs、batch、group assignment、quasi-2D composition 与 full stack 已记录。
- [ ] Electrode orientation、active area、encapsulation 与 contact integrity 已确认。
- [ ] Required groups 来自同一 batch；否则 batch 已标为 confounder。
- [ ] Initial EL、spectrum、current-voltage response 及 preconditioning / failure rules 已冻结：`To be filled`。

## 2. Drive Waveform Readiness

- [ ] DC、bipolar AC 与 optional unipolar pulsed waveform、frequency、duty cycle 已定义：`To be filled`。
- [ ] Amplitude、pulse/rest state 及 peak / peak-to-peak / RMS voltage definition 已明确：`To be filled`。
- [ ] Wiring map、probe polarity 与 positive/negative half-cycle convention 已确认。
- [ ] Device-terminal voltage 将被直接测量，不只记录 generator setting。

## 3. AC/DC Matching Readiness

- [ ] Primary matching basis 与 tolerance 已冻结：`To be filled`。
- [ ] Current 与 charge matching methods 已定义，且 charge calculation 考虑 displacement current。
- [ ] Time-averaged terminal power 与 initial radiance matching methods 已定义。
- [ ] Temperature 使用相同 sensor location / acquisition rule；peak field / terminal-voltage definition 已明确。
- [ ] 每项已预设 `matched / unmatched / not measured` reporting；known mismatch 不会被隐藏。

## 4. Instrument Synchronization Readiness

- [ ] Voltage、current 与 EL 使用 shared trigger / time base。
- [ ] Dummy-load / reference-circuit check 已通过。
- [ ] Voltage、current 与 optical channel delay 已校准并记录 uncertainty。
- [ ] Detector bandwidth、linearity、saturation 与 optical baseline 已通过；raw 与 corrected data 分开保存。
- [ ] Displacement-current separation或 mixed-current reporting rule 已定义：`To be filled`。

## 5. PN Half-Cycle Analysis Readiness

- [ ] Positive/negative windows 由 delay-corrected terminal-voltage zero crossings 定义。
- [ ] Boundary / guard-window rule 已冻结：`To be filled`。
- [ ] Peak、integrated 与 duration-normalized PN metrics 将并列报告。
- [ ] `R_PN_peak` 不会被写成 `R_PN_integrated`。
- [ ] Numerator、denominator、window metadata、undefined-ratio reason 及 phase-lag method 将保留：`To be filled`。

## 6. Stability and Recovery Readiness

- [ ] Lifetime / retention metric、threshold、censoring 与 stop rule 已定义：`To be filled`。
- [ ] Luminance / radiance、spectrum、waveform 与 temperature intervals 已填写：`To be filled`。
- [ ] Temperature-time trace 将与 stability data 同步保存。
- [ ] Rest point、duration、environment 与 bias state 已定义：`To be filled`。
- [ ] Baseline、end-of-stress、after-rest spectra 使用相同 calibration；recovery metric 已定义：`To be filled`。
- [ ] Early failure、open/short 与 censored devices 不会被静默删除。

## 7. Mechanism-Claim Readiness

- [ ] Direct observations 将与 causal interpretation 分开记录。
- [ ] PN asymmetry 不会单独解释为 residual-carrier recombination 或 ambipolar injection。
- [ ] Phase lag 与 current peak 不会在 instrument delay / displacement current 未排除时作机制解释。
- [ ] Recovery 或 AC stability improvement 不会单独归因于 ion redistribution / suppressed ion migration。
- [ ] Post-stress ion mapping / independent ion-sensitive control 状态：`To be filled / Not performed`。
- [ ] Heating、stress mismatch、capacitive response、barrier change 与 degradation channels 已保留为 competing explanations。

## 8. Go / No-Go Decision

- [ ] **GO:** device、waveform、instrument 与 required matching gates 全部通过。
- [ ] **CONDITIONAL GO:** 已知 mismatch 已记录，实验可用于 observation，但相关机制结论保持 `UNVERIFIED`。
- [ ] **NO-GO:** terminal waveform、synchronization、detector validity、temperature record 或 primary matching 无法确认。

- Final decision: `GO / CONDITIONAL GO / NO-GO`
- Open blockers: `To be filled`
- Approved by: `To be filled`

> **Final rule:** If any instrument synchronization or matching gate fails, mechanism claims must remain `UNVERIFIED`.
