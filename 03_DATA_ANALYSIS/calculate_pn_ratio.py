#!/usr/bin/env python3
"""Calculate positive/negative half-cycle integrated EL and PN ratio."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


REQUIRED_COLUMNS = {"time_s", "voltage_V", "EL_intensity_a.u."}


def validate_waveform(data: pd.DataFrame) -> pd.DataFrame:
    """Validate and return a numeric, time-sorted waveform table."""
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    clean = data.copy()
    for column in REQUIRED_COLUMNS:
        clean[column] = pd.to_numeric(clean[column], errors="raise")
    if clean[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Required waveform columns contain missing values")

    clean = clean.sort_values("time_s").reset_index(drop=True)
    if clean["time_s"].duplicated().any():
        raise ValueError("time_s contains duplicate values")
    if len(clean) < 2 or not np.all(np.diff(clean["time_s"]) > 0):
        raise ValueError("time_s must be strictly increasing")
    return clean


def integrate_masked_signal(data: pd.DataFrame, mask: pd.Series) -> float:
    """Integrate each contiguous polarity segment, then sum the areas."""
    selected_indices = np.flatnonzero(mask.to_numpy())
    if len(selected_indices) < 2:
        raise ValueError("Each voltage half-cycle requires at least two samples")

    segments = np.split(
        selected_indices,
        np.flatnonzero(np.diff(selected_indices) > 1) + 1,
    )
    areas: list[float] = []
    for segment in segments:
        if len(segment) < 2:
            raise ValueError("Each voltage half-cycle requires at least two samples")
        selected = data.iloc[segment]
        areas.append(
            float(
                np.trapezoid(
                    selected["EL_intensity_a.u."].to_numpy(),
                    selected["time_s"].to_numpy(),
                )
            )
        )
    return float(sum(areas))


def calculate_pn_ratio(data: pd.DataFrame) -> dict[str, float]:
    """Return integrated EL values and R_PN = I_positive / I_negative."""
    clean = validate_waveform(data)
    positive = integrate_masked_signal(clean, clean["voltage_V"] > 0)
    negative = integrate_masked_signal(clean, clean["voltage_V"] < 0)
    if np.isclose(negative, 0.0):
        raise ValueError("Integrated EL in the negative half-cycle is zero")
    return {
        "positive_integrated_el": positive,
        "negative_integrated_el": negative,
        "pn_ratio": positive / negative,
    }


def read_waveform(path: Path) -> pd.DataFrame:
    """Read a waveform CSV with a useful file error."""
    if not path.is_file():
        raise FileNotFoundError(f"Waveform CSV not found: {path}")
    return pd.read_csv(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Waveform CSV path")
    parser.add_argument("--json", dest="json_path", type=Path, help="Optional JSON output")
    args = parser.parse_args()

    try:
        metrics: dict[str, Any] = calculate_pn_ratio(read_waveform(args.csv_path))
        text = json.dumps(metrics, indent=2, ensure_ascii=False)
        print(text)
        if args.json_path:
            args.json_path.parent.mkdir(parents=True, exist_ok=True)
            args.json_path.write_text(text + "\n", encoding="utf-8")
    except (FileNotFoundError, OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
