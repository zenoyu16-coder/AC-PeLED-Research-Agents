# Data Format Standard

所有 CSV 使用 UTF-8、逗号分隔、第一行为固定 column names。数值列不得混入单位字符串；单位写在列名或 metadata 中。缺失值保持为空并在 metadata 解释，不能用 `0` 代替。

## 文件命名规则

推荐格式：

```text
YYYYMMDD_sampleID_measurement_condition_stage.ext
```

示例：

```text
20260610_deviceA_pn-waveform_100Hz_raw.csv
20260610_deviceA_pn-waveform_100Hz_processed.csv
```

规则：

- `sampleID` 必须与 metadata、protocol 和 report 一致。
- `measurement` 使用稳定词汇，如 `waveform`、`spectrum`、`stability`。
- `condition` 只写用于区分文件的关键条件，不把完整 metadata 塞进文件名。
- `stage` 只能是 `raw` 或 `processed`。
- 不使用空格、中文标点、`final`、`new`、`latest` 等不可追踪名称。

## Raw / Processed 边界

**Raw data** 是仪器直接导出或仅完成无损格式转换的数据。raw file 不覆盖、不手工删点、不平滑、不归一化。

**Processed data** 是经过 baseline correction、time alignment、smoothing、filtering、normalization、unit conversion 或 exclusion 后的数据。每个 processed file 必须记录：

- source raw file path 或 immutable identifier
- processing script 与 version/commit
- execution command
- processing timestamp
- operator
- 所有处理步骤及参数

分析脚本生成的图片、JSON 与 processed CSV 默认不提交到 Git；只有经过审核、具有长期复用价值的标准示例可以进入仓库。

## Signal Processing 记录要求

### Baseline correction

- 记录 baseline window、算法、offset 值和处理前后单位。
- 说明 baseline 是按整条 trace、每周期还是每个 half-cycle 估算。
- 不得用 baseline correction 隐藏 detector drift 或真实 negative signal。

### Smoothing

- 默认不 smoothing；若使用，记录算法、window length、polynomial order 等参数。
- 同时保留 unsmoothed result，并确认关键 peak、phase 与 integration metric 对参数不敏感。

### Filtering

- 记录 filter type、cutoff frequency、order、zero-phase/causal 设置和 sampling rate。
- cutoff 必须与 detector bandwidth 和目标 waveform frequency 一起解释。
- 不得用 filtering 创建或消除 half-cycle EL。

所有未采用的处理也应明确写 `none`，而不是留空。

## 1. EL waveform data

```csv
time_s,voltage_V,current_mA,EL_intensity_a.u.
```

| Column | 含义 | Unit |
|---|---|---|
| `time_s` | 共享 time base；必须单调递增 | s |
| `voltage_V` | 实际测得的器件或监测点电压 | V |
| `current_mA` | 与 voltage/EL 同步的电流 | mA |
| `EL_intensity_a.u.` | detector baseline 处理后的 EL signal | a.u. |

## 2. EL spectra data

```csv
wavelength_nm,intensity_a.u.
```

| Column | 含义 | Unit |
|---|---|---|
| `wavelength_nm` | 校准后的 wavelength | nm |
| `intensity_a.u.` | 光谱强度；注明 raw、corrected 或 normalized | a.u. |

## 3. Stability data

```csv
time_s,luminance_cd_m2,EL_intensity.a.u.,voltage_V,current_mA,EL_peak_nm
```

| Column | 含义 | Unit |
|---|---|---|
| `time_s` | 从 stability test 开始计时 | s |
| `luminance_cd_m2` | 绝对 luminance；不可用时留空 | cd m^-2 |
| `EL_intensity.a.u.` | 相对 EL signal | a.u. |
| `voltage_V` | 记录时刻的实际电压 | V |
| `current_mA` | 记录时刻的电流 | mA |
| `EL_peak_nm` | EL peak wavelength | nm |

## 必须记录的 Metadata

每个 CSV 必须有同 basename 的 metadata 记录，至少包含：

```yaml
sample_id: "Not explicitly specified in text"
device_stack: "Not explicitly specified in text"
device_area: "Not explicitly specified in text"
fabrication_batch: "Not explicitly specified in text"
measurement_datetime: "Not explicitly specified in text"
operator: "Not explicitly specified in text"
instrument_models: "Not explicitly specified in text"
detector_bandwidth: "Not explicitly specified in text"
sampling_rate: "Not explicitly specified in text"
trigger_and_channel_delay: "Not explicitly specified in text"
driving_mode: "Not explicitly specified in text"
waveform: "Not explicitly specified in text"
frequency: "Not explicitly specified in text"
voltage_definition_and_value: "Not explicitly specified in text"
duty_cycle: "Not explicitly specified in text"
atmosphere: "Not explicitly specified in text"
temperature_and_humidity: "Not explicitly specified in text"
encapsulation: "Not explicitly specified in text"
calibration_or_baseline_processing: "Not explicitly specified in text"
source_raw_file: "Not explicitly specified in text"
processing_script_and_version: "Not explicitly specified in text"
processing_command: "Not explicitly specified in text"
baseline_correction: "none / method and parameters"
smoothing: "none / method and parameters"
filtering: "none / method and parameters"
notes: "Not explicitly specified in text"
```

## Quality Checks

- 时间必须单调递增且无重复 sample time。
- waveform channels 必须来自同一 time base，或记录 alignment 方法。
- 不得静默删除负值、outlier 或 failed device。
- normalization 必须保留原始信号与 reference definition。
- 文件名、sample ID 和报告中的引用必须一致。
