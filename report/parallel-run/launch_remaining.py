#!/usr/bin/env python3
"""Launch remaining phenomenology scans in parallel. One log per job.

    python report/parallel-run/launch_remaining.py

CPU budget ~24 of 32. Does not rerun jsonl rows already present.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
os.makedirs(HERE, exist_ok=True)


def job(name, argv, env=None):
    log = os.path.join(HERE, name + ".log")
    t0 = time.time()
    e = os.environ.copy()
    if env:
        e.update(env)
    with open(log, "w", encoding="utf-8") as out:
        out.write("CMD " + " ".join(argv) + "\n\n")
        out.flush()
        r = subprocess.run(argv, stdout=out, stderr=subprocess.STDOUT, cwd=ROOT, env=e)
    dt = round(time.time() - t0)
    return name, r.returncode, dt, log


def main():
    jobs = [
        ("heavy-tests", [PY, os.path.join(ROOT, "tests", "run_heavy.py"), "-j", "6"]),
        (
            "edge-extra",
            [
                PY, os.path.join(ROOT, "code", "edge_value_scan.py"),
                "--workers", "6",
                "chi3:80:26:56", "chi3:80:28:64", "chi7:16", "chi17:16",
                "chi3:80:32:70",
            ],
        ),
        (
            "mw-extra",
            [
                PY, os.path.join(ROOT, "code", "marginal_weights.py"),
                "--workers", "3", "--inner", "4",
                "chi3:80:26:56", "chi3:80:28:64", "chi4:38:66:80",
                "19a1:22:36:60", "67a1:22:36:60", "37a1:22:36:60",
            ],
        ),
        (
            "scan-s-chi3-80-24",
            [PY, os.path.join(ROOT, "code", "scan_s.py"), "chi3", "80", "24", "50"],
            {"DUMP_MODE": os.path.join(ROOT, "report", "mode_chi3_mu80_NB24.json")},
        ),
        (
            "scan-s-chi3-80-26",
            [PY, os.path.join(ROOT, "code", "scan_s.py"), "chi3", "80", "26", "56"],
            {"DUMP_MODE": os.path.join(ROOT, "report", "mode_chi3_mu80_NB26.json")},
        ),
        (
            "scan-s-chi3-80-28",
            [PY, os.path.join(ROOT, "code", "scan_s.py"), "chi3", "80", "28", "64"],
            {"DUMP_MODE": os.path.join(ROOT, "report", "mode_chi3_mu80_NB28.json")},
        ),
        (
            "scan-s-chi3-80-32",
            [PY, os.path.join(ROOT, "code", "scan_s.py"), "chi3", "80", "32", "70"],
            {"DUMP_MODE": os.path.join(ROOT, "report", "mode_chi3_mu80_NB32.json")},
        ),
        (
            "q-gl2-37a1-mu62",
            [PY, os.path.join(ROOT, "code", "scan_q_gl2.py"), "37a1", "62", "80", "50"],
        ),
        (
            "q-gl2-67a1-mu38",
            [PY, os.path.join(ROOT, "code", "scan_q_gl2.py"), "67a1", "38", "66", "50"],
        ),
        (
            "q-gl2-32a1-mu38",
            [PY, os.path.join(ROOT, "code", "scan_q_gl2.py"), "32a1", "38", "66", "50"],
        ),
        ("gram-gl2-37a1-62", [PY, os.path.join(ROOT, "code", "scan_gl2.py"), "37a1", "62", "80", "50"]),
        ("gram-gl2-37a1-38", [PY, os.path.join(ROOT, "code", "scan_gl2.py"), "37a1", "38", "66", "42"]),
        ("gram-maass1", [PY, os.path.join(ROOT, "code", "scan_gl2.py"), "maass1", "16", "24", "40"]),
        ("gram-maass2", [PY, os.path.join(ROOT, "code", "scan_gl2.py"), "maass2", "16", "24", "40"]),
        ("gram-maass3", [PY, os.path.join(ROOT, "code", "scan_gl2.py"), "maass3", "16", "24", "40"]),
        ("cert-2plane", [PY, os.path.join(HERE, "run_cert_2plane_grid.py")]),
    ]
    # flatten optional env
    flat = []
    for item in jobs:
        if len(item) == 2:
            flat.append((item[0], item[1], None))
        else:
            flat.append(item)

    print(f"launching {len(flat)} jobs from {ROOT}", flush=True)
    t0 = time.time()
    failed = 0
    results = []
    with ThreadPoolExecutor(max_workers=len(flat)) as ex:
        futs = {ex.submit(job, n, a, e): n for n, a, e in flat}
        for fut in as_completed(futs):
            name, rc, dt, log = fut.result()
            tag = "PASS" if rc == 0 else "FAIL"
            print(f"  {tag}  {name:24s} {dt:5d}s  {log}", flush=True)
            results.append((name, rc, dt, log))
            failed += rc != 0
    summary = os.path.join(HERE, "SUMMARY.txt")
    with open(summary, "w", encoding="utf-8") as f:
        f.write(f"done in {round(time.time()-t0)}s ; {failed} failed / {len(flat)}\n")
        for name, rc, dt, log in sorted(results):
            f.write(f"{'PASS' if rc==0 else 'FAIL'} {name} {dt}s {log}\n")
    print(f"done in {round(time.time()-t0)}s ; {failed} failed ; {summary}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
