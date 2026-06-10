# Run Example Analysis

本目录中的 CSV 是 **synthetic data**，只用于确认格式和脚本运行，不代表真实器件或推荐 AC driving condition。

## 1. 安装依赖

在仓库根目录运行：

```bash
python -m pip install -r requirements.txt
```

## 2. PN ratio

```bash
python 03_DATA_ANALYSIS/calculate_pn_ratio.py \
  03_DATA_ANALYSIS/examples/example_waveform.csv
```

输出 integrated positive/negative EL 与 integrated PN ratio。当前脚本不计算 peak 或 duration-normalized ratio；这两项在 protocol 中定义，后续实现前不得假装已有输出。

## 3. Full waveform analysis

```bash
python 03_DATA_ANALYSIS/analyze_el_waveform.py \
  03_DATA_ANALYSIS/examples/example_waveform.csv \
  --output-dir analysis_output/example_waveform
```

生成 `metrics.json` 与 waveform plot。phase lag 是 cross-correlation placeholder，只有确认 detector bandwidth 和 channel delay 后才能物理解读。

## 4. Stability

```bash
python 03_DATA_ANALYSIS/plot_stability.py \
  03_DATA_ANALYSIS/examples/example_stability.csv \
  --output analysis_output/example_stability.png
```

示例会跨过 80% retention，用于检查 T80 interpolation。输出目录被 `.gitignore` 排除。

## 5. Interpretation Boundary

- synthetic output 只证明代码路径可运行。
- 不从示例 PN ratio 推断 carrier injection、ion migration 或 interfacial polarization。
- 不把 synthetic T80 当作器件 lifetime。
- 将真实数据用于分析前，必须补齐 metadata 与 protocol Definition of Done。
