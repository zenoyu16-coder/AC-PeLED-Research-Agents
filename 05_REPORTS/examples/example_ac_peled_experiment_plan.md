# Quasi-2D AC-PeLED Pilot Experiment Plan

> Status: planning example only. 本文件不包含实验结果，也不预设 AC 优于 DC。所有未来实验参数必须在执行前填写并冻结。

## Material Passport

- Origin: `02_PROTOCOLS/pn_half_cycle_el_analysis.yaml`, `02_PROTOCOLS/ac_stability_test.yaml`, `01_PAPERS/mechanism_map.md`
- Plan type: future quasi-2D AC-PeLED pilot study
- Architecture scope: quasi-2D PeLED
- Verification status: `UNVERIFIED` until the controls and go/no-go gates below are completed
- Observation/interpretation rule: measured observations、indirect support、author hypothesis 与 causal claim 必须分开记录

## 1. Research Question

在同批次 quasi-2D PeLED 中，当 DC、bipolar AC 与 optional unipolar pulsed drive 采用明确且逐项报告的 stress matching 时：

1. 不同 driving mode 是否产生可重复的 PN half-cycle EL、phase lag、spectral evolution 与 operational stability 差异？
2. 这些差异能否由 current、charge、power、initial radiance、temperature 或 terminal-voltage mismatch 解释？
3. 在 instrument、thermal、capacitive 与 recovery controls 通过后，是否仍存在与 ionic redistribution / interfacial polarization 一致的信号？

## 2. Hypothesis

### Primary experimental hypothesis

Bipolar AC 的 field history 可能使 quasi-2D PeLED 呈现不同于 matched DC baseline 的 half-cycle EL、phase lag、spectral drift 与 retention behavior。

### Mechanism hypothesis

若 bipolar AC 同时表现出不同的 electronic response、较少的 post-stress ionic redistribution，以及更稳定的 spectrum / retention，并且主要 competing explanations 已由 controls 排除，则结果可支持 field reversal 参与改变 ionic redistribution 或 interfacial polarization。

### Falsification criteria

- AC/DC 差异在完成 current、charge、power、initial radiance、temperature 与 terminal-voltage matching 后消失。
- apparent phase lag 可由 dummy load、channel delay 或 detector bandwidth 解释。
- PN asymmetry 随 integration-window definition 明显改变，或只存在于 peak metric 而不见于 integrated metric。
- stability difference 与 temperature history、electrical stress mismatch 或 device batch 更一致。
- post-stress ion mapping 不支持组间 ion-distribution difference，或该差异不能与 stability / spectral observations 对齐。

## 3. Device Scope

| Item | Entry Before Experiment |
|---|---|
| Quasi-2D composition | To be filled |
| Organic spacer / ligand | To be filled |
| Nominal phase distribution | To be filled |
| Device stack | To be filled |
| Transport layers | To be filled |
| Electrode materials and polarity | To be filled |
| Active area | To be filled |
| Encapsulation | To be filled |
| Fabrication batch ID | To be filled |
| Number of independent devices per group | To be filled |
| Device inclusion criteria | To be filled |
| Predefined failure / exclusion criteria | To be filled |

所有 comparison groups 应来自同一 fabrication batch；若无法做到，batch 必须作为 confounder 单独报告。

## 4. Comparison Groups

| Group | Role | Drive Definition | Required Status |
|---|---|---|---|
| DC baseline | operational and spectral stability baseline | polarity、control mode、terminal voltage/current: To be filled | Required |
| Bipolar AC | primary experimental condition | waveform、frequency、duty cycle、positive/negative amplitude、polarity sequence: To be filled | Required |
| Unipolar pulsed | 区分 pulsing effect 与 field reversal effect | waveform、pulse width、frequency、duty cycle、off-state definition: To be filled | Optional；若不执行，记录 `Not performed` |
| Unstressed control | post-stress spectrum / ion mapping reference | storage environment and duration: To be filled | Required when destructive post-stress analysis is used |

分组前记录 device ID、batch、初始 EL、spectrum、current-voltage response 与 observable defects。分组方法与是否 blind-coded：`To be filled`。

## 5. Variables to Fill Before Experiment

### Independent variables

- Driving mode: DC / bipolar AC / optional unipolar pulsed。
- Waveform shape: `To be filled`。
- Frequency: `To be filled`。
- Duty cycle: `To be filled`。
- Terminal-voltage amplitude and definition: `To be filled`。
- Polarity sequence and electrode reference: `To be filled`。
- Rest/recovery schedule: `To be filled`。

### Primary dependent variables

- Positive and negative half-cycle peak EL。
- Positive and negative half-cycle integrated EL。
- `R_PN_peak`、`R_PN_integrated` 与 duration-normalized PN ratio。
- Voltage-EL phase lag，reference / response feature: `To be filled`。
- Luminance or radiance retention。
- Lifetime metric and threshold: `To be filled`。
- EL peak、FWHM、integrated spectrum 与 new spectral features。
- Device or substrate temperature。

### Controlled variables and covariates

- Composition、stack、active area、encapsulation、batch。
- Atmosphere、humidity、ambient / stage temperature。
- Detector、optical geometry、gain、bandwidth、sampling、trigger。
- Preconditioning、initial state、stress duration、measurement intervals。
- Current、charge、power、initial radiance、temperature 与 peak field / terminal voltage matching status。

### Literature-derived unknowns

Guo 2025 stability-test frequency、duty cycle 与 stated voltage 的 peak / peak-to-peak / RMS definition: `Not explicitly specified in text`。这些值不得复制为本 pilot 参数，必须独立填写。

## 6. AC/DC Matching Strategy

不得使用“AC/DC matched”作为单一标签。下表每一项必须分别给出 metric、target、tolerance、measured result 和 verdict。

| Dimension | Definition to Freeze | Measurement / Calculation | Target and Tolerance | Result | Verdict |
|---|---|---|---|---|---|
| Current | current density、cycle-resolved current 或 selected summary: To be filled | synchronized terminal current | To be filled | To be filled | matched / unmatched / not measured |
| Charge | accumulated absolute charge、net charge、positive/negative charge: To be filled | integrate delay-corrected current after displacement-current assessment | To be filled | To be filled | matched / unmatched / not measured |
| Power | time-averaged terminal electrical power definition: To be filled | integrate measured terminal voltage × current | To be filled | To be filled | matched / unmatched / not measured |
| Initial radiance | luminance or radiance and calibration basis: To be filled | calibrated optical measurement before stress | To be filled | To be filled | matched / unmatched / not measured |
| Temperature | sensor type and location: To be filled | identical sensor placement and acquisition rule across groups | To be filled | To be filled | matched / unmatched / not measured |
| Peak field / terminal voltage | peak、peak-to-peak、RMS or instantaneous definition: To be filled | differential voltage measured at device terminals | To be filled | To be filled | matched / unmatched / not measured |

### Matching decision

- Primary matching basis: `To be filled`。
- Secondary matching dimensions: `To be filled`。
- Known unmatched dimensions: `To be filled`。
- Adjustment procedure before stress: `To be filled`。
- Rule when all dimensions cannot be matched simultaneously: report the trade-off and retain unmatched dimensions as competing explanations。

## 7. Measurement Sequence

### Phase A: Freeze the plan

1. Assign sample IDs and comparison groups。
2. Complete all `To be filled` fields that affect stress、timing、detector response、matching or analysis。
3. Freeze polarity convention、integration-window rule、lifetime endpoint、exclusion criteria and stop rules。
4. Create the metadata sheet and raw-data filenames before energizing devices。

### Phase B: Instrument and control qualification

1. Record waveform-source、probe、current monitor、detector and acquisition-chain IDs。
2. Run dummy-load / reference-circuit test through the same electrical acquisition path。
3. Verify voltage、current and optical channel delays with a common timing event or reference source。
4. Verify detector bandwidth、linearity、saturation margin and optical baseline。
5. Define displacement-current separation or reporting method。
6. Mark each control `PASS`、`FAIL` or `UNVERIFIED`。

### Phase C: Device baseline characterization

1. Inspect device and confirm contact integrity。
2. Apply the frozen preconditioning procedure: `To be filled`。
3. Record synchronized device-terminal voltage、current and EL。
4. Record initial calibrated luminance / radiance and spectrum。
5. Record baseline temperature at the defined sensor location。
6. Confirm group matching feasibility before long stress。

### Phase D: Terminal voltage/current/EL synchronization

1. Use a shared trigger and time base for all three channels。
2. Record measured device-terminal waveform rather than generator setting alone。
3. Save raw, unfiltered voltage、current and EL traces。
4. Apply documented channel-delay correction without overwriting raw data。
5. Reject or flag traces with trigger loss、detector saturation or invalid terminal waveform。

### Phase E: PN half-cycle EL

1. Generate positive and negative windows from delay-corrected terminal-voltage zero crossings。
2. Apply the same boundary / guard-window rule to all groups and devices。
3. Report each window's start、end、duration and valid sample count。
4. Calculate positive/negative peaks、integrated EL and duration-normalized EL。
5. Report `R_PN_peak` and `R_PN_integrated` separately; do not convert one into the other。
6. If the denominator is zero or below the valid detection rule, report the raw values and an undefined ratio。

### Phase F: Phase lag

1. Select voltage reference and EL response feature before analysis: `To be filled`。
2. Subtract measured instrument/channel delay。
3. Report corrected and uncorrected phase lag with uncertainty。
4. Compare with dummy-load and detector-response results。
5. If instrument delay is not resolved, classify device-level phase interpretation as `UNVERIFIED`。

### Phase G: Stability stress

1. Start DC and bipolar AC groups under the frozen matching strategy。
2. Run optional unipolar pulsed group only if its matching and terminal waveform pass qualification。
3. Continuously or periodically record luminance / radiance、spectrum、terminal voltage/current waveform and temperature according to: `To be filled`。
4. Preserve early failures、open/short devices and censored devices in the dataset。
5. Do not adjust stress parameters after group assignment unless the deviation is logged and the affected run is separately classified。

### Phase H: Rest/recovery

1. Pause stress at predefined point(s): `To be filled`。
2. Record rest duration、environment and bias state。
3. Measure luminance / radiance、spectrum、terminal voltage/current、PN metrics and phase lag immediately before and after rest。
4. Classify recovery as observed、not observed or indeterminate。
5. Do not label recovery as ion redistribution without independent ion-sensitive evidence。

### Phase I: Spectral recovery

1. Save raw spectra at baseline、end of stress and after rest。
2. Apply the same wavelength and intensity calibration。
3. Compare EL peak、FWHM、integrated spectrum and new spectral features。
4. Predefine the spectral recovery metric: `To be filled`。
5. Report spectral recovery separately from operational lifetime。

### Phase J: Post-stress analysis

1. Select unstressed、DC-stressed、AC-stressed and, when applicable, after-rest samples using the frozen sampling rule。
2. Perform post-stress ion mapping only if enabled: method `To be filled`。
3. Preserve sample coding、storage、transfer and stress-endpoint metadata。
4. Align ion-distribution observations with each sample's electrical、spectral、thermal and lifetime record。
5. Treat post-stress distribution differences as direct observations of final-state differences, not as complete reconstruction of the dynamic migration path。

## 8. Controls

| Control | Required Action | Pass Criterion | If Not Passed |
|---|---|---|---|
| Dummy load | Run same cables、probes、amplifiers and time base with electrical reference | apparent delay / transient is quantified and traceable | phase-lag mechanism claim blocked |
| Detector bandwidth | Verify amplitude/phase response over interpreted waveform content | detector response does not create or erase reported EL features | affected PN / phase metrics marked `UNVERIFIED` |
| Channel delay | Calibrate voltage、current and optical channels | correction and uncertainty are documented | synchronization-based interpretation blocked |
| Displacement current | Use reference capacitor、non-emissive or below-EL-threshold control: To be filled | mixed current components are identified or explicitly retained | current peak cannot be called pure injection current |
| Temperature monitoring | Use identical sensor type、location and rule across groups | temperature history is recorded and comparison status assigned | Joule heating remains a competing explanation |
| Polarity verification | Record wiring map and measured terminal polarity | labels agree with measured terminal voltage and control trace | PN labels invalid; repeat acquisition |
| Optical baseline | Verify dark signal、linearity、saturation and geometry | all analyzed signals satisfy frozen validity rules | affected trace excluded only under predefined criterion |
| Polarity reversal | Reverse sequence or wiring under re-verified terminal polarity: To be filled | stress and matching metadata remain interpretable | electrode asymmetry remains unresolved |

## 9. Data Files to Generate

Use one immutable raw-data folder per run and one derived-data folder generated from copies or read-only raw inputs.

| File | Minimum Contents | Status |
|---|---|---|
| `experiment_manifest.yaml` | plan version、operator、date、group definitions、frozen parameters、protocol versions | To be generated |
| `device_metadata.csv` | device ID、batch、stack、composition、area、encapsulation、group、failure status | To be generated |
| `matching_table.csv` | all six matching dimensions、targets、results、uncertainties、verdicts | To be generated |
| `instrument_calibration.yaml` | detector bandwidth、linearity、dummy-load result、channel delays、probe map | To be generated |
| `waveforms_raw_<device>_<timepoint>.csv` | timestamp、terminal voltage、current、EL、trigger marker | To be generated |
| `pn_metrics.csv` | windows、peaks、integrals、durations、all PN ratio definitions、validity flags | To be generated |
| `phase_lag.csv` | method、reference、raw delay、instrument correction、corrected result、uncertainty | To be generated |
| `stability_timeseries.csv` | stress time、retention signal、terminal electrical metrics、temperature、device status | To be generated |
| `spectra_raw_<device>_<timepoint>.csv` | wavelength、raw intensity、calibration reference | To be generated |
| `recovery_log.csv` | pre-rest、rest and post-rest measurements with timing metadata | To be generated |
| `ion_mapping_manifest.yaml` | sample code、stress endpoint、method、target species、normalization and file links | To be generated if enabled |
| `deviations_and_failures.md` | deviations、instrument interruptions、failed/censored devices and decisions | To be generated |
| `observation_interpretation_table.md` | direct observation、support class、competing explanation、claim verdict | To be generated |

## 10. Go / No-Go Gates

### Gate A: Device readiness

**GO** when sample IDs、batch、initial optical/electrical state and predefined failure criteria are complete。  
**NO-GO** when contacts are unstable、group assignment is undocumented or baseline data are missing。

### Gate B: Instrument readiness

**GO** when dummy-load、detector bandwidth/linearity、channel delay、trigger and terminal-voltage checks pass。  
**NO-GO** for PN / phase analysis when instrument delay or detector response can explain the target signal。

### Gate C: Matching readiness

**GO** when every matching dimension has a measured status and the primary matching rule is satisfied。  
**CONDITIONAL GO** when known mismatches are accepted and explicitly retained as confounders。  
**NO-GO** when only generator settings are available or initial radiance / temperature cannot be compared。

### Gate D: Pilot stability start

**GO** when baseline spectrum、temperature、terminal waveform and data logging are valid for all required groups。  
**NO-GO** when any required group lacks valid synchronized data or the stress stop rule is undefined。

### Gate E: Mechanism interpretation

**GO for observation reporting** when direct measurements and uncertainties are complete。  
**GO for indirect mechanism support** only when the relevant positive and discriminating controls pass。  
**NO-GO for suppressed-ion-migration claim** unless matching、thermal record、rest/recovery or polarity control、and independent ion-sensitive evidence are all available and major competing explanations are addressed。

## 11. What This Experiment Can Prove

When the relevant gates pass, this pilot can establish:

- Whether the studied quasi-2D PeLED batch exhibits measurable PN half-cycle EL under the selected waveform。
- Whether peak、integrated and duration-normalized PN metrics differ among defined groups。
- Whether corrected voltage-EL phase lag depends on the selected drive condition。
- Whether DC、bipolar AC and optional unipolar pulsed groups show different observed retention or spectral evolution under the documented matching status。
- Whether rest produces measurable electrical、optical or spectral recovery。
- Whether post-stress samples show different final-state ion distributions, if ion mapping is performed。

这些结论属于 direct observation，必须附带 measurement conditions、matching verdict 与 uncertainty。

## 12. What This Experiment Cannot Prove

本 pilot 单独不能证明：

- AC 普遍提高所有 quasi-2D PeLED 的 operational stability。
- PN asymmetry 必然来自 residual-carrier recombination 或 ambipolar injection。
- phase lag 是 ion migration 或 interfacial polarization 的特异性指标。
- slow response、hysteresis 或 spectral recovery 单独证明 ion migration。
- post-stress ion-distribution difference 完整重建了动态 migration path。
- AC stabilization 完全由 suppressed ion migration 造成。
- half-cycle EL 或 phase lag 能预测 lifetime，除非另行预注册并验证 predictive analysis。

若 over-attribution gate 未通过，机制结论必须写为 `UNVERIFIED`，同时保留 heating、stress mismatch、capacitive response、reversible injection/barrier change、electrode/transport-layer degradation 与 phase segregation 等 competing explanations。

## 13. Required Metadata Checklist

### Device and fabrication

- [ ] Experiment ID、plan version、operator、date。
- [ ] Device ID、batch ID、group assignment。
- [ ] Quasi-2D composition、spacer、phase-distribution characterization。
- [ ] Full stack、layer process、electrode orientation、active area。
- [ ] Encapsulation、storage and transfer history。
- [ ] Planned、completed、failed and censored device counts。

### Drive and polarity

- [ ] DC、bipolar AC and optional unipolar waveform definitions。
- [ ] Frequency、duty cycle、pulse width or rest state: `To be filled`。
- [ ] Peak / peak-to-peak / RMS / instantaneous terminal-voltage definition。
- [ ] Wiring map、probe polarity、positive/negative half-cycle convention。
- [ ] Measured device-terminal voltage and synchronized current。

### Instrumentation

- [ ] Waveform source、voltage probe、current monitor、detector、spectrometer and acquisition-system IDs。
- [ ] Sampling rate、bandwidth、gain、filtering and baseline method。
- [ ] Shared trigger / time base。
- [ ] Voltage、current and optical channel-delay calibration。
- [ ] Dummy-load result。
- [ ] Detector linearity、saturation and wavelength/intensity calibration。
- [ ] Displacement-current control and interpretation status。

### PN and phase analysis

- [ ] Positive/negative integration-window rule and guard interval。
- [ ] Actual window times、durations and sample counts。
- [ ] Peak、integrated and duration-normalized metrics reported together。
- [ ] Numerator、denominator and undefined-ratio reasons。
- [ ] Phase reference、response feature、raw delay、correction and uncertainty。

### Stability and recovery

- [ ] Preconditioning、initial radiance and baseline spectrum。
- [ ] Current、charge、power、initial radiance、temperature and terminal-voltage matching table。
- [ ] Atmosphere、humidity and temperature sensor location。
- [ ] Stress intervals、measurement intervals、stop rule and deviations。
- [ ] Retention metric、threshold and censoring rule。
- [ ] Rest duration、environment and bias state。
- [ ] Spectral-recovery definition and raw spectra。
- [ ] Polarity-reversal design and result。

### Post-stress and interpretation

- [ ] Unstressed / DC / AC / after-rest sample mapping。
- [ ] Ion-mapping method、target species、normalization and interface reference, if enabled。
- [ ] Direct observations listed separately from causal interpretations。
- [ ] Controls completed、missing or failed。
- [ ] Competing explanations excluded and remaining。
- [ ] Final support class: direct observation / indirect support / author hypothesis / `UNVERIFIED`。
