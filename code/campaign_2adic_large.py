#!/usr/bin/env python3
"""2-adic peak campaign for a multicore box.

Resolves tau_S - tau_arch at Lambda >= 16. The mass at lambda=2 is
known by h->0 extrapolation at Lambda=4 and 8 (~0.49). This run is
the *shape* plus the same mass at Lambda=16, 24 (and optional 32).

GPU: do not use the A6000. Bottleneck is scipy.special.sici on CPU
grids. Scale by processes, one (Lambda, cpu) per process.

Usage (from repo root or from code/):

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \\
      python3 code/campaign_2adic_large.py --jobs default --workers 8

    python3 code/campaign_2adic_large.py --jobs night --workers 12

Resume is automatic: completed rows in the JSONL are skipped.

Output:
    report/campaign_2adic_large.jsonl
    report/campaign_2adic_large.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from trace_dist import tau_curve  # noqa: E402

EXPECTED = float(np.log(2) / np.sqrt(2))
def _out_paths():
    tap = os.environ.get("TAPER", "0")
    if float(tap or 0) > 0:
        return (ROOT / "report" / "campaign_2adic_taper.jsonl",
                ROOT / "report" / "campaign_2adic_taper.csv")
    return (ROOT / "report" / "campaign_2adic_large.jsonl",
            ROOT / "report" / "campaign_2adic_large.csv")


# Default: finish Lambda=16 (cpu 80 already at w=0.14) then 24.
JOBS = {
    "default": [
        (16, 80),
        (16, 96),
        (16, 112),
        (16, 128),
        (24, 64),
        (24, 80),
        (24, 96),
    ],
    "night": [
        (16, 80),
        (16, 96),
        (16, 112),
        (16, 128),
        (16, 160),
        (24, 64),
        (24, 80),
        (24, 96),
        (24, 128),
        (32, 64),
        (32, 80),
        (32, 96),
    ],
    "smoke": [(16, 32), (16, 48)],
    "taper16": [(16, 80), (16, 112), (16, 160)],
}


def lams_grid():
    return np.concatenate(
        [
            np.linspace(0.30, 0.90, 61),
            np.linspace(0.905, 1.095, 77),
            np.linspace(1.10, 3.30, 221),
        ]
    )


def memory_gb(Lam: float, cpu: int) -> float:
    # Fmat builds a few (N_out x N_in) float64 arrays.
    n_in = int(Lam * cpu)
    r = Lam * 3.3 * 1.02
    n_out = int(np.ceil(r * cpu))
    return 8 * n_out * n_in * 6 / 1e9


def one_job(Lam: float, cpu: int) -> dict:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    os.environ.setdefault("MKL_NUM_THREADS", "1")
    lams = lams_grid()
    t0 = time.time()
    tap = float(os.environ.get("TAPER", "0.2"))
    tA = tau_curve(Lam, False, lams, cells_per_unit=cpu, taper=tap)
    tS = tau_curve(Lam, True, lams, cells_per_unit=cpu, taper=tap)
    d = tS - tA
    dt = time.time() - t0

    def mass(center: float, half: float) -> float:
        m = np.abs(lams - center) < half * center
        return float(np.trapezoid(d[m] / lams[m], lams[m]))

    i2 = int(np.argmin(np.abs(lams - 2.0)))
    i5 = int(np.argmin(np.abs(lams - 0.5)))
    row = {
        "Lam": float(Lam),
        "cpu": int(cpu),
        "h": 1.0 / cpu,
        "sec": round(dt, 2),
        "mem_gb_est": round(memory_gb(Lam, cpu), 2),
        "w2": mass(2.0, 0.12),
        "w2_tight": mass(2.0, 0.06),
        "w2_wide": mass(2.0, 0.25),
        "w05": mass(0.5, 0.12),
        "peak2": float(d[i2]),
        "peak05": float(d[i5]),
        "expected": EXPECTED,
        "taper": float(os.environ.get("TAPER", "0.2")),
        "profile_lams": [float(x) for x in lams[i2 - 20 : i2 + 21]],
        "profile_d": [float(x) for x in d[i2 - 20 : i2 + 21]],
    }
    return row


def load_done(path: Path) -> set:
    done = set()
    if not path.exists():
        return done
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        done.add((float(r["Lam"]), int(r["cpu"])))
    return done


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    slim = {k: v for k, v in row.items() if k not in ("profile_lams", "profile_d")}
    slim["profile_lams"] = row["profile_lams"]
    slim["profile_d"] = row["profile_d"]
    with path.open("a") as f:
        f.write(json.dumps(slim) + "\n")
        f.flush()


def write_csv(jsonl: Path, csv_path: Path) -> None:
    rows = []
    if jsonl.exists():
        for line in jsonl.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                rows.append(
                    {
                        k: r[k]
                        for k in (
                            "Lam",
                            "cpu",
                            "h",
                            "w2",
                            "w2_tight",
                            "w2_wide",
                            "w05",
                            "peak2",
                            "peak05",
                            "sec",
                            "mem_gb_est",
                        )
                        if k in r
                    }
                )
    if not rows:
        return
    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--jobs", choices=sorted(JOBS), default="default")
    p.add_argument("--workers", type=int, default=max(1, os.cpu_count() // 4 or 1))
    p.add_argument("--lam", type=float, action="append")
    p.add_argument("--cpu", type=int, action="append")
    args = p.parse_args()

    if args.lam and args.cpu:
        jobs = [(L, c) for L in args.lam for c in args.cpu]
    else:
        jobs = list(JOBS[args.jobs])

    global OUT_JSONL, OUT_CSV
    OUT_JSONL, OUT_CSV = _out_paths()
    done = load_done(OUT_JSONL)
    todo = [(L, c) for L, c in jobs if (float(L), int(c)) not in done]
    print(f"expected mass {EXPECTED:.4f}")
    print(f"already {len(done)}  todo {len(todo)}  workers {args.workers}")
    for L, c in todo:
        print(f"  job Lam={L} cpu={c}  ~{memory_gb(L,c):.1f} GB/process")

    if not todo:
        write_csv(OUT_JSONL, OUT_CSV)
        print("nothing to do")
        return

    # One BLAS thread per process so workers do not fight.
    os.environ["OMP_NUM_THREADS"] = "1"
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
    os.environ["MKL_NUM_THREADS"] = "1"

    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(one_job, L, c): (L, c) for L, c in todo}
        for fut in as_completed(futs):
            L, c = futs[fut]
            try:
                row = fut.result()
            except Exception as e:
                print(f"FAIL Lam={L} cpu={c}: {e!r}")
                continue
            append_jsonl(OUT_JSONL, row)
            write_csv(OUT_JSONL, OUT_CSV)
            print(
                f"OK  Lam={row['Lam']:.0f} cpu={row['cpu']:3d}  "
                f"w2={row['w2']:+.3f}  peak2={row['peak2']:+.2f}  "
                f"{row['sec']:.1f}s",
                flush=True,
            )


if __name__ == "__main__":
    main()
