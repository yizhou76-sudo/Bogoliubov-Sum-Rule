#!/usr/bin/env python3
"""Cross-check the closed-form s-wave T=0 susceptibility against PRB Fig. 3.

This script parses the vector curves from the local page-5 SVG export of
Phys. Rev. B 113, 064511 (2026), extracts the T=0 intercepts of the five
published s-wave curves in Fig. 3, converts them to chi(T=0)/chi_N using the
plot box, and compares them against the closed form

    chi(0)/chi_N = (2/3) F_s(lambda),
    F_s(lambda) = 1 - asinh(lambda)/(lambda sqrt(1 + lambda^2)),

with lambda = (g k_F / k_B T_c0) / (Delta_0 / k_B T_c0) and the weak-coupling
BCS ratio Delta_0 / (k_B T_c0) = pi / exp(gamma_E).
"""

from __future__ import annotations

import math
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
WORK_DIR = REPO_ROOT / "backup" / "unused-figures"

PDF_PATH = REPO_ROOT / "Reference" / "PhysRevB.113.064511.pdf"
SVG_PATH = WORK_DIR / "fig3_page5.svg"
OUT_TSV = WORK_DIR / "fig3_t0_comparison.tsv"
OUT_SUMMARY = WORK_DIR / "fig3_t0_summary.txt"
OUT_CURVE_TSV = WORK_DIR / "fig3_t0_theory_curve.tsv"

# Plot box for Fig. 3 in the page-5 SVG exported by pdftocairo.
PLOT_LEFT = 346.867188
PLOT_TOP = 65.25
PLOT_RIGHT = 535.386719
PLOT_BOTTOM = 217.167969
PLOT_WIDTH = PLOT_RIGHT - PLOT_LEFT
PLOT_HEIGHT = PLOT_BOTTOM - PLOT_TOP

# The five legend values shown in Fig. 3.
G_VALUES = [0.0, 1.0, 2.0, 4.0, 30.0]
EULER_GAMMA = 0.5772156649015329
DELTA0_OVER_KBTC0 = math.pi / math.exp(EULER_GAMMA)

SVG_NS = "{http://www.w3.org/2000/svg}"
PATH_POINT_RE = re.compile(r"([ML])\s*([-0-9.]+)\s+([-0-9.]+)")
TRANSFORM_RE = re.compile(
    r"matrix\(([-0-9.]+),\s*0,\s*0,\s*([-0-9.]+),\s*([-0-9.]+),\s*([-0-9.]+)\)"
)


def parse_page_points(path_d: str, transform: str) -> list[tuple[float, float]]:
    m = TRANSFORM_RE.search(transform)
    if not m:
        return []
    sx = float(m.group(1))
    sy = float(m.group(2))
    tx = float(m.group(3))
    ty = float(m.group(4))
    page_points: list[tuple[float, float]] = []
    for _, x_str, y_str in PATH_POINT_RE.findall(path_d):
        x = float(x_str)
        y = float(y_str)
        page_points.append((tx + sx * x, ty + sy * y))
    return page_points


def inside_plot(x: float, y: float) -> bool:
    return (PLOT_LEFT - 1.0) <= x <= (PLOT_RIGHT + 1.0) and (PLOT_TOP - 1.0) <= y <= (PLOT_BOTTOM + 1.0)


def fs(lam: float) -> float:
    if lam == 0.0:
        return 0.0
    return 1.0 - math.asinh(lam) / (lam * math.sqrt(1.0 + lam * lam))


def chi_theory(g_over_kbtc0: float) -> float:
    lam = g_over_kbtc0 / DELTA0_OVER_KBTC0
    return (2.0 / 3.0) * fs(lam)

def curve_grid() -> list[float]:
    # Denser near the origin where the curvature is strongest.
    left = [0.02 * i for i in range(0, 201)]      # 0.00 .. 4.00
    mid = [4.0 + 0.05 * i for i in range(1, 121)] # 4.05 .. 10.00
    right = [10.0 + 0.10 * i for i in range(1, 201)]  # 10.10 .. 30.00
    return left + mid + right


def main() -> int:
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    if not SVG_PATH.exists():
        if not PDF_PATH.exists():
            print(f"Missing source PDF: {PDF_PATH}", file=sys.stderr)
            return 1
        subprocess.run(
            ["pdftocairo", "-svg", "-f", "5", "-l", "5", str(PDF_PATH), str(SVG_PATH)],
            check=True,
        )

    if not SVG_PATH.exists():
        print(f"Missing SVG export: {SVG_PATH}", file=sys.stderr)
        return 1

    root = ET.parse(SVG_PATH).getroot()

    color_points: dict[str, list[tuple[float, float]]] = {}
    for el in root.iter(f"{SVG_NS}path"):
        stroke = el.attrib.get("stroke")
        if not stroke or stroke == "rgb(0%, 0%, 0%)":
            continue
        d = el.attrib.get("d", "")
        transform = el.attrib.get("transform", "")
        pts = parse_page_points(d, transform)
        if not pts:
            continue
        if not any(inside_plot(x, y) for x, y in pts):
            continue
        color_points.setdefault(stroke, []).extend((x, y) for x, y in pts if inside_plot(x, y))

    if len(color_points) != 5:
        print(f"Expected 5 curve colors in Fig. 3, found {len(color_points)}: {sorted(color_points)}", file=sys.stderr)
        return 1

    extracted = []
    for color, pts in color_points.items():
        xmin = min(x for x, _ in pts)
        left_pts = [(x, y) for x, y in pts if abs(x - xmin) < 1e-6]
        y_page = sum(y for _, y in left_pts) / len(left_pts)
        chi_digitized = (PLOT_BOTTOM - y_page) / PLOT_HEIGHT
        extracted.append(
            {
                "color": color,
                "xmin_page": xmin,
                "y_page": y_page,
                "chi_digitized": chi_digitized,
            }
        )

    # The left endpoints are ordered monotonically by g in Fig. 3.
    extracted.sort(key=lambda row: row["chi_digitized"])

    rows = []
    for g_value, row in zip(G_VALUES, extracted):
        lam = g_value / DELTA0_OVER_KBTC0
        chi_exact = chi_theory(g_value)
        abs_diff = abs(row["chi_digitized"] - chi_exact)
        rows.append(
            {
                "gkF_over_kBTc0": g_value,
                "lambda": lam,
                "chi_digitized": row["chi_digitized"],
                "chi_theory": chi_exact,
                "abs_diff": abs_diff,
                "stroke_rgb": row["color"],
                "y_page": row["y_page"],
            }
        )

    max_abs_diff = max(row["abs_diff"] for row in rows)
    rms_abs_diff = math.sqrt(sum(row["abs_diff"] ** 2 for row in rows) / len(rows))

    with OUT_TSV.open("w", encoding="utf-8") as fh:
        fh.write(
            "gkF_over_kBTc0\tlambda\tchi0_digitized_over_chiN\tchi0_theory_over_chiN\tabs_diff\tstroke_rgb\ty_page\n"
        )
        for row in rows:
            fh.write(
                f"{row['gkF_over_kBTc0']:.12g}\t"
                f"{row['lambda']:.12g}\t"
                f"{row['chi_digitized']:.12g}\t"
                f"{row['chi_theory']:.12g}\t"
                f"{row['abs_diff']:.12g}\t"
                f"{row['stroke_rgb']}\t"
                f"{row['y_page']:.12g}\n"
            )

    with OUT_CURVE_TSV.open("w", encoding="utf-8") as fh:
        fh.write("gkF_over_kBTc0\tchi0_theory_over_chiN\n")
        for g_value in curve_grid():
            fh.write(f"{g_value:.12g}\t{chi_theory(g_value):.12g}\n")

    with OUT_SUMMARY.open("w", encoding="utf-8") as fh:
        fh.write("Fig. 3 T=0 cross-check against the closed form\n")
        fh.write(f"SVG source: {SVG_PATH}\n")
        fh.write(f"Delta0/(k_B Tc0) = pi/exp(gamma_E) = {DELTA0_OVER_KBTC0:.15f}\n")
        fh.write(f"Maximum absolute difference in chi/chi_N = {max_abs_diff:.12g}\n")
        fh.write(f"RMS absolute difference in chi/chi_N = {rms_abs_diff:.12g}\n")

    print("gkF/kBTc0  lambda         digitized       theory          abs diff")
    for row in rows:
        print(
            f"{row['gkF_over_kBTc0']:10.6g}  "
            f"{row['lambda']:12.8f}  "
            f"{row['chi_digitized']:12.9f}  "
            f"{row['chi_theory']:12.9f}  "
            f"{row['abs_diff']:11.9f}"
        )
    print(f"max abs diff = {max_abs_diff:.9g}")
    print(f"rms abs diff = {rms_abs_diff:.9g}")
    print(f"wrote {OUT_TSV.relative_to(REPO_ROOT)}")
    print(f"wrote {OUT_CURVE_TSV.relative_to(REPO_ROOT)}")
    print(f"wrote {OUT_SUMMARY.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
