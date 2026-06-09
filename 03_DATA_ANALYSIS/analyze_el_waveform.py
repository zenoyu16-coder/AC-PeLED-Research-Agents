#!/usr/bin/env python3
"""Analyze synchronized AC voltage, current and EL waveform data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from calculate_pn_ratio import calculate_pn_ratio, validate_waveform


REQUIRED_COLUMNS = {
    "time_s",
    "voltage_V",
    "current_mA",
    "EL_intensity_a.u.",
}


def load_waveform(path: Path) -> pd.DataFrame:
    """Load and validate the standard waveform CSV."""
    if not path.is_file():
        raise FileNotFoundError(f"Waveform CSV not found: {path}")
    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    data["current_mA"] = pd.to_numeric(data["current_mA"], errors="raise")
    return validate_waveform(data)


def estimate_phase_lag(data: pd.DataFrame) -> dict[str, Any]:
    """Estimate voltage-to-EL lag by cross-correlation as a screening metric.

    This is a computational placeholder, not a calibrated physical phase
    measurement. Instrument channel delay and waveform harmonics must be
    checked before interpretation.
    """
    time = data["time_s"].to_numpy()
    voltage = data["voltage_V"].to_numpy(dtype=float)
    el = data["EL_intensity_a.u."].to_numpy(dtype=float)
    if np.isclose(np.std(voltage), 0.0) or np.isclose(np.std(el), 0.0):
        return {
            "phase_lag_s": None,
            "method": "cross_correlation_placeholder",
            "warning": "Phase lag unavailable for a constant signal.",
        }

    dt = float(np.median(np.diff(time)))
    voltage_centered = voltage - np.mean(voltage)
    el_centered = el - np.mean(el)
    correlation = np.correlate(el_centered, voltage_centered, mode="full")
    lags = np.arange(-len(voltage_centered) + 1, len(el_centered))
    lag_samples = int(lags[int(np.argmax(correlation))])
    return {
        "phase_lag_s": lag_samples * dt,
        "phase_lag_samples": lag_samples,
        "method": "cross_correlation_placeholder",
        "warning": (
            "Correct detector bandwidth and channel delay before physical "
            "interpretation."
        ),
    }


def plot_waveform(data: pd.DataFrame, output_path: Path) -> None:
    """Plot voltage and EL against the shared time axis."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure, voltage_axis = plt.subplots(figsize=(9, 5))
    el_axis = voltage_axis.twinx()
    voltage_axis.plot(data["time_s"], data["voltage_V"], color="tab:blue", label="Voltage")
    el_axis.plot(
        data["time_s"],
        data["EL_intensity_a.u."],
        color="tab:red",
        label="EL intensity",
    )
    voltage_axis.set_xlabel("Time (s)")
    voltage_axis.set_ylabel("Voltage (V)", color="tab:blue")
    el_axis.set_ylabel("EL intensity (a.u.)", color="tab:red")
    voltage_axis.grid(alpha=0.25)
    figure.tight_layout()
    figure.savefig(output_path, dpi=200)
    plt.close(figure)


def analyze(path: Path, output_dir: Path) -> dict[str, Any]:
    """Run metrics and plotting for one waveform CSV."""
    data = load_waveform(path)
    metrics: dict[str, Any] = calculate_pn_ratio(data)
    metrics.update(estimate_phase_lag(data))

    output_dir.mkdir(parents=True, exist_ok=True)
    plot_waveform(data, output_dir / "el_waveform.png")
    (output_dir / "metrics.json").write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return metrics


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("analysis_output"))
    args = parser.parse_args()
    try:
        print(json.dumps(analyze(args.csv_path, args.output_dir), indent=2))
    except (FileNotFoundError, OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
