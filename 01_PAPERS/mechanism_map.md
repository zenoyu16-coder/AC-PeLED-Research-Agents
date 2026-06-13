# AC-Driven PeLED Mechanism Map

本机制图仅使用三个已通过 Source Verification Gate 的 PeLED anchors：

- Guo et al. (2025), DOI: `10.1002/lpor.202402262`
- Chakraborty et al. (2020), DOI: `10.1103/PhysRevApplied.14.024006`
- Dong et al. (2020), DOI: `10.1021/acsami.0c14269`

不引入其他文献。观察、间接机制支持、作者假设与未核验链接分开记录。

## Research Scope

- **Question:** AC waveform 如何通过 field history、electronic response 与可能的 ionic redistribution / interfacial polarization，影响 half-cycle EL、phase lag、spectral stability 与 operational stability？
- **Included architecture:** PeLED。
- **Target transfer:** quasi-2D AC-PeLED，但三个 anchors 的 dimensionality 均不能作为已核验的 quasi-2D 直接证据。
- **Evidence boundary:** Guo 代表 AC stabilization evidence；Chakraborty 代表 AC dynamic-response evidence；Dong 代表 ion-migration diagnostic evidence。

## Evidence Domains

| Evidence Domain | Directly Supported | Mechanism-Level Limit | Anchor |
|---|---|---|---|
| AC stabilization evidence | AC 相对 DC 的 measured T50 改善、spectral drift 降低、EQE roll-off trend 减弱，以及老化后较少 iodine accumulation / redistribution | field reversal 完整抑制 ion migration 并因此延寿，仍是 direct + indirect mixed evidence；AC J90 > 500 mA cm^-2 为 inferred/estimated | Guo 2025 |
| AC dynamic-response evidence | sinusoidal bipolar AC 下双半周期 EL、EL(-):EL(+) peak asymmetry、frequency dependence、voltage-EL phase lag 与 -3 dB frequency | residual-carrier recombination、ambipolar transport 与 transit-time 归因属于 indirect support / author hypothesis；不支持 lifetime 改善 | Chakraborty 2020 |
| Ion-migration diagnostic evidence | transient current 与 efficiency 的慢响应，以及 SI Table S1 的 millisecond-to-tens-of-milliseconds fitted time constants | halide migration、anode-interface accumulation、hole-injection enhancement 与 charge imbalance 为 indirect support / author interpretation；未研究 AC stabilization | Dong 2020 |

## 1. Directly Observed Phenomena

| ID | Direct Observation | Source / Locator | Scope |
|---|---|---|---|
| O1 | Bipolar AC 与 DC comparison 下，FAPbI3 PeLED 的 measured T50 分别为 424 min 与 10.3 min；AC 下 time-dependent spectra 更稳定 | Guo 2025, Figure 3a-f | AC stabilization |
| O2 | AC 下 EQE roll-off trend 较弱；DC J90 = 330 mA cm^-2 为 measured，AC J90 > 500 mA cm^-2 未直接测得 crossing point | Guo 2025, Figure 1f and Figure S12 | AC efficiency response |
| O3 | AC aging 后的 iodine accumulation / redistribution 少于 DC aging；lateral-field treatment 显示不同 damage pattern | Guo 2025, Figure 4a-d and 4h,i | Ion redistribution / damage comparison |
| O4 | Sinusoidal bipolar AC 下，positive 与 negative voltage half-cycles 均出现 phase-resolved EL | Chakraborty 2020, Figures 3a,b and 5a,b | AC dynamic response |
| O5 | EL(-):EL(+) **peak-intensity ratio** 随 composition 改变，MAPbI3 中最高约 0.8；该指标不等同于 integrated PN ratio | Chakraborty 2020, Figure 3c | PN peak asymmetry |
| O6 | EL response 随 frequency 改变，并在高频出现 material-dependent voltage-EL phase lag；-3 dB frequency 为 5.8-22.7 kHz | Chakraborty 2020, Figure 5c, Figure 6 and Table I | Frequency / phase response |
| O7 | Transient current 与 efficiency 存在 tens-of-milliseconds slow response；fitted hole-injection-current time constants 随 temperature 改变 | Dong 2020, publisher abstract and ACS SI Table S1 | Ion-migration-sensitive transient diagnostic |

## 2. Indirectly Supported Mechanisms

| ID | Mechanism Link | Support | Why It Is Indirect | Status |
|---|---|---|---|---|
| M1 | Reversing field history is associated with reduced net iodine redistribution relative to DC aging | Guo O3；hysteresis 与 tDOS trends | TOF-SIMS 比较的是 aging 后分布，不能单独解析迁移路径、瞬时速度或所有 competing degradation channels | VERIFIED as association; causal mechanism mixed |
| M2 | Slow transient electronic response is sensitive to ionic redistribution / interfacial accumulation | Dong O7 | 慢响应可与 ion migration 一致，但也可能包含 trapping、capacitive charging、interfacial polarization、thermal effects 或 injection-barrier evolution | VERIFIED as diagnostic sensitivity; mechanism not unique |
| M3 | Ionic redistribution can alter hole injection and charge balance | Dong O7 与作者对 charge-injection / recombination dynamics 的联合解释 | accessible evidence 未直接成像 anode-interface ion accumulation，也未独立隔离 injection barrier change | INDIRECT SUPPORT |
| M4 | Reduced iodine redistribution may contribute to improved spectral and operational stability | Guo O1 与 O3 的同一 AC/DC aging framework | stability 与 iodine redistribution 同时改善，但未建立逐器件、逐时间点的 quantitative mediation relationship | INDIRECT SUPPORT |
| M5 | Half-cycle history contributes to negative-half-cycle EL | Chakraborty O4-O6 加 positive/negative DC polarity controls | residual carriers 未被直接成像或定量追踪；ambipolarity 与 transit-time 参数包含 model dependence | INDIRECT SUPPORT |

## 3. Author Hypotheses

| ID | Author Hypothesis | Anchor | Classification |
|---|---|---|---|
| H1 | Periodic electric-field reversal counteracts iodine migration induced by the preceding positive pulse | Guo 2025 | Author hypothesis supported by O3, hysteresis and tDOS |
| H2 | Periodic charge injection reduces carrier accumulation and Auger-related exciton-charge annihilation, thereby reducing EQE roll-off | Guo 2025 | Author hypothesis; roll-off trend is direct, microscopic pathway is not |
| H3 | Residual carriers from the preceding positive half-cycle move and recombine during the negative half-cycle | Chakraborty 2020 | Author hypothesis with indirect support |
| H4 | Composition-dependent PN peak asymmetry reflects ambipolar transport, while high-frequency phase lag reflects carrier transit time | Chakraborty 2020 | Author interpretation / model-dependent hypothesis |
| H5 | Halide migration and accumulation at the anode interface facilitate hole injection, create charge imbalance and change radiative recombination evolution | Dong 2020 | Author interpretation with indirect support |

## 4. Causal Chain

目标链条：

`waveform → field history → electronic response → ionic redistribution / interfacial polarization → half-cycle EL / phase lag → spectral stability / operational stability`

| Link | Supported Observation | Evidence Class | Paper Support | Missing Discrimination | Verdict |
|---|---|---|---|---|---|
| waveform → field history | Guo 使用 bipolar square-wave；Chakraborty 使用 sinusoidal bipolar AC | Directly specified drive condition | Guo 2025；Chakraborty 2020 | Guo stability-test frequency、duty cycle 与 2.2 V amplitude definition: Not explicitly specified in text；device-terminal voltage verification不足 | VERIFIED for applied waveform; internal field history partly UNVERIFIED |
| field history → electronic response | 双半周期 EL、PN peak asymmetry、frequency dependence 与 phase lag 被直接测量；Guo 观察到 positive duration EL 而 negative-period leakage不发光 | Direct observation of response under AC; mechanism indirect | Chakraborty O4-O6；Guo time-resolved EL | channel-delay calibration、detector response、integrated half-cycle windows 与 displacement-current separation | VERIFIED for response; microscopic attribution UNVERIFIED |
| electronic response → ionic redistribution / interfacial polarization | Guo 的 AC/DC aging 后 iodine profiles 不同；Dong 的 slow transient 对 migration-sensitive process 有诊断意义 | Cross-study indirect support | Guo O3；Dong O7/M2 | 同一器件中同步 electronic transient 与 time-resolved ion-distribution measurement；trapping / heating / capacitive controls | **UNVERIFIED** |
| ionic redistribution / interfacial polarization → half-cycle EL / phase lag | 三篇文献均未直接把 measured ion redistribution 与 PN peak ratio 或 phase lag 建立因果对应 | No direct support | Guo 研究 aging redistribution；Chakraborty 研究 dynamic EL；Dong 研究 transient diagnostic，但三者未完成同一因果测试 | ion-blocking control、temperature dependence、pre-bias history、rest/recovery、simultaneous current-EL-ion diagnostics | **UNVERIFIED** |
| half-cycle EL / phase lag → spectral stability / operational stability | Chakraborty 未报告 lifetime；Guo 未把 PN metric / phase lag 与 lifetime 做 quantitative correlation | No direct support | Evidence domains remain separate | 在 matched AC stress 下同步记录 PN metrics、phase lag、spectrum、temperature 与 lifetime | **UNVERIFIED** |
| field history → ionic redistribution | AC 与 DC aging 后 iodine redistribution / damage pattern 不同 | Direct observation of different outcomes; full mechanism mixed | Guo O3/M1/H1 | matched charge、power、temperature、replicates 与 time-resolved migration trajectory | VERIFIED for different outcomes; full suppression mechanism not fully verified |
| ionic redistribution → spectral / operational stability | AC 下同时出现较少 iodine redistribution、较稳定 spectrum 与较长 T50 | Indirect support | Guo O1/O3/M4 | quantitative temporal linkage、independent ion-blocking intervention 与 alternative degradation controls | **UNVERIFIED as causal link** |

## 5. Remaining Unverifiable Gaps

- **G1:** quasi-2D phase distribution、organic spacer 与 interfaces 如何改变 AC field history、ionic response 和 RC time constants：`UNVERIFIED`。
- **G2:** PN peak asymmetry 是否主要来自 residual carriers、ambipolar injection、ion-induced barrier modulation、detector response 或 displacement current：`UNVERIFIED`。
- **G3:** voltage-EL phase lag 中 electronic transit、instrument delay、capacitive response 与 ionic polarization 的相对贡献：`UNVERIFIED`。
- **G4:** AC stabilization 是否由 suppressed ion migration 主导，而非 lower average stress、charge/power mismatch、reduced Joule heating 或 reversible injection changes：`UNVERIFIED`。
- **G5:** spectral recovery after rest 是否代表 reversible ion redistribution：三个 anchors 未提供足够直接证据，`UNVERIFIED`。
- **G6:** half-cycle EL / phase lag 能否作为后续 lifetime 或 spectral drift 的 predictive marker：`UNVERIFIED`。
- **G7:** Dong transient time constants 与 AC half-cycle time scales 是否可直接映射：drive waveform、voltage 与 repetition conditions 为 `Not explicitly specified in text`，因此 `UNVERIFIED`。

## Competing Explanations

| Observation | Current Interpretation | Competing Explanations | Required Discriminating Control | Current Verdict |
|---|---|---|---|---|
| PN peak asymmetry | residual-carrier recombination / ambipolar transport | injection asymmetry、detector response、integration definition、displacement current、history-dependent barriers | calibrated detector and channel delay；peak vs integrated PN metrics；polarity-reversed device/control；current-EL synchronization | Mechanism UNVERIFIED |
| Voltage-EL phase lag | carrier transit-time limitation | instrument delay、RC response、capacitive charging、ionic polarization | electrical dummy load；bandwidth calibration；device thickness/temperature/frequency series | Mechanism UNVERIFIED |
| Slow transient current / efficiency | halide migration and interfacial accumulation | trapping、thermal drift、capacitive charging、injection-barrier evolution | ion-blocking layer/control；temperature series；rest/recovery；independent ion-distribution measurement | Ion-specific assignment UNVERIFIED |
| AC lifetime and spectral improvement | reduced iodine redistribution under field reversal | unequal charge/power/temperature stress、lower average stress、different heating、reversible injection changes | matched current/charge/power/initial radiance；temperature monitoring；replicates；post-stress ion mapping | Improvement VERIFIED; dominant cause UNVERIFIED |

## What This Map Does NOT Prove

1. 不证明 AC 在所有 PeLED architectures 或 quasi-2D PeLED 中必然提高 lifetime。
2. 不证明 Guo 2025 的全部稳定性增益仅由 suppressed ion migration 造成。
3. 不证明 TOF-SIMS 单独完整解析了动态 ion-migration mechanism；其直接支持的是 AC/DC aging 后 iodine redistribution 差异。
4. 不证明 PN peak asymmetry 或 voltage-EL phase lag 是 ion migration 的特异性指标。
5. 不证明 Chakraborty 2020 提供 AC operational-stability evidence；该论文未报告 operational lifetime 或 retention test。
6. 不证明 Dong 2020 研究了 AC half-cycle operation 或 AC stabilization。
7. 不将 AC J90 > 500 mA cm^-2 当作直接测量值。
8. 不证明 peak EL(-):EL(+) 等同于 integrated positive/negative half-cycle photon ratio。

## Experiments Needed for Quasi-2D AC-PeLED Transfer

1. **Matched AC/DC stability matrix:** 同批次、同 stack、同 quasi-2D composition 与 phase distribution；分别进行 current、charge、power、initial radiance 和 temperature matching。记录 voltage definition、waveform、frequency、duty cycle 与 replicate count。
2. **Verified terminal waveform:** 同步测量 source voltage、device-terminal voltage 与 current；明确 polarity convention，并校准 channel delay、detector response、bandwidth 与 integration window。
3. **Half-cycle response mapping:** 在 frequency、voltage、duty cycle 与 waveform series 下，同时报告 positive/negative peak EL、integrated EL、PN ratio、phase lag、spectra 与 displacement-current caveat。
4. **Electronic-versus-ionic timescale separation:** 进行 temperature-dependent transient current/EL、pre-bias history、frequency sweep、rest/recovery 与 ion-blocking controls，区分 transport、trapping、capacitive polarization 和 migration-sensitive components。
5. **Time-linked ion evidence:** 在 matched stress time points 后进行 TOF-SIMS 或其他独立 ion-distribution measurement，并与同一批器件的 PN metrics、phase lag、spectral drift 和 lifetime 对齐。
6. **Interfacial-polarization controls:** 改变 transport layer / blocking interface，同时保持 EML 与 drive stress 可比，检验 injection barrier modulation 是否足以解释 PN asymmetry 或 slow transient。
7. **Spectral-recovery test:** AC/DC stress 后设置标准化 rest intervals，重复测量 spectrum、EL intensity、current 与 PN response，区分 reversible redistribution 与 irreversible degradation。
8. **Causal intervention:** 采用能够降低 mobile-ion response、但尽量保持 electronic transport 可比的材料或界面 control；只有 intervention 同时改变 ion diagnostic 与 stability outcome，才能加强 causal attribution。

## Critic Status

- **Verdict:** `CONDITIONAL`
- **Supported anchors:** 三个来源均为 `VERIFIED`，但 Dong 2020 的科学证据范围限于 publisher abstract 与 ACS Supporting Information。
- **Blocked claims:** “PN asymmetry由ion migration造成”；“phase lag预测stability”；“AC stabilization完全由suppressed ion migration造成”；“三个 anchors 可直接外推至 quasi-2D AC-PeLED”。
- **Required revision before experiments:** 将所有 drive、timing、detector、matching 与 temperature parameters 写入 protocol；任何未由 anchors 明确支持的参数继续标记为 `Not explicitly specified in text`。
