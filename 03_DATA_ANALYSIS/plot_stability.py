#!/usr/bin/env python3
"""Plot stability retention and estimate T80 from a standard CSV."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


NOT_REACHED = "T80 not reached in this dataset"


def estimate_t80(
    time_s: pd.Series, retention: pd.Series
) -> float | str:
    """Estimate the first 80% crossing by linear interpolation."""
    time = pd.to_numeric(time_s, errors="raise").to_numpy(dtype=float)
    values = pd.to_numeric(retention, errors="raise").to_numpy(dtype=float)
    if len(time) != len(values) or len(time) < 2:
        raise ValueError("T80 estimation requires at least two paired samples")
    if np.any(np.diff(time) <= 0):
        raise ValueError("time_s must be strictly increasing")

    threshold = 0.8
    below = np.flatnonzero(values <= threshold)
    if len(below) == 0:
        return NOT_REACHED
    index = int(below[0])
    if index == 0:
        return float(time[0])

    t0, t1 = time[index - 1], time[index]
    r0, r1 = values[index - 1], values[index]
    if np.isclose(r0, r1):
        return float(t1)
    return float(t0 + (threshold - r0) * (t1 - t0) / (r1 - r0))


def load_stability(path: Path) -> tuple[pd.DataFrame, str]:
    """Load stability data and choose luminance or relative EL signal."""
    if not path.is_file():
        raise FileNotFoundError(f"Stability CSV not found: {path}")
    data = pd.read_csv(path)
    if "time_s" not in data:
        raise ValueError("Missing required column: time_s")

    candidates = ["luminance_cd_m2", "EL_intensity.a.u."]
    signal_column = next(
        (column for column in candidates if column in data and data[column].notna().any()),
        None,
    )
    if signal_column is None:
        raise ValueError("No usable luminance_cd_m2 or EL_intensity.a.u. column")

    clean = data[["time_s", signal_column]].dropna().copy()
    clean["time_s"] = pd.to_numeric(clean["time_s"], errors="raise")
    clean[signal_column] = pd.to_numeric(clean[signal_column], errors="raise")
    clean = clean.sort_values("time_s").reset_index(drop=True)
    if clean.empty or np.isclose(clean.loc[0, signal_column], 0.0):
        raise ValueError("Initial stability signal must be non-zero")
    return clean, signal_column


def plot_stability(path: Path, output_path: Path) -> float | str:
    """Calculate retention = I_t / I_0, save a plot, and return T80."""
    data, signal_column = load_stability(path)
    retention = data[signal_column] / data.loc[0, signal_column]
    t80 = estimate_t80(data["time_s"], retention)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(data["time_s"], retention, marker="o", label="Retention")
    axis.axhline(0.8, color="tab:red", linestyle="--", label="80%")
    if isinstance(t80, float):
        axis.axvline(t80, color="tab:orange", linestyle=":", label=f"T80={t80:.3g} s")
    axis.set_xlabel("Time (s)")
    axis.set_ylabel(r"Retention $I_t / I_0$")
    axis.set_ylim(bottom=0)
    axis.grid(alpha=0.25)
    axis.legend()
    figure.tight_layout()
    figure.savefig(output_path, dpi=200)
    plt.close(figure)
    return t80


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output", type=Path, default=Path("stability_retention.png"))
    args = parser.parse_args()
    try:
        print(plot_stability(args.csv_path, args.output))
    except (FileNotFoundError, OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
