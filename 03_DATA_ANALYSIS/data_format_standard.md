# Data Format Standard

所有 CSV 使用 UTF-8、逗号分隔、第一行为固定 column names。数值列不得混入单位字符串；单位写在列名或 metadata 中。缺失值保持为空并在 metadata 解释，不能用 `0` 代替。

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
notes: "Not explicitly specified in text"
```

## Quality Checks

- 时间必须单调递增且无重复 sample time。
- waveform channels 必须来自同一 time base，或记录 alignment 方法。
- 不得静默删除负值、outlier 或 failed device。
- normalization 必须保留原始信号与 reference definition。
- 文件名、sample ID 和报告中的引用必须一致。
