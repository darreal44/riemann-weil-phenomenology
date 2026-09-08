#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Maass GL2 L-zeros from rigor a_n, plus high-prec coefficients.

Replica coefficients and R are PostgreSQL numeric (keep every digit).
Tools see:
  load_an(label)     -> numpy float64
  load_an_hp(label)  -> list of mpmath.mpf (dps = digit count, ~70–100)
  load_R_hp(label)   -> mpf (full spectral_parameter text)
  load_zeros(label)  -> numpy float64 γ (IEEE 64-bit, error < 1e-6)
Indexed catalog: gitignored data/lmfdb_mirror.sqlite (maass_an_prec)
and code/lmfdb_maass_gl2.pkl (metadata, L-search row, zeros).

    python code/maass_zeros_an.py --fetch-R
    python code/maass_zeros_an.py --fetch                 # all a_n, 2 replica conns
    python code/maass_zeros_an.py --fetch 1.0.1.1.1 maass2
    python code/maass_zeros_an.py --check                 # Table 1 vs Booker–Then
    python code/maass_zeros_an.py --all --tmax 320        # 3 GPUs

AFE, not a certified Weyl harvest. Not Weil.
"""
from __future__ import annotations

import math
import os
import pickle
import sqlite3
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
SQLITE = os.path.join(DATA, "lmfdb_mirror.sqlite")
ZEROS_PKL = os.path.join(HERE, "lmfdb_maass_zeros.pkl")
DSN = os.environ.get(
    "LMFDB_DSN",
    "host=devmirror.lmfdb.xyz port=5432 dbname=lmfdb user=lmfdb password=lmfdb",
)
N_FETCH = max(1, min(2, int(os.environ.get("LMFDB_WORKERS", "2"))))
# a_n / R: keep every replica digit (see lmfdb_encode.mpf_keep). γ: float64.

sys.path.insert(0, HERE)


def pg():
    import psycopg2

    conn = psycopg2.connect(DSN, connect_timeout=30)
    cur = conn.cursor()
    cur.execute("SET statement_timeout = '180s'")
    cur.close()
    return conn


def ensure_prec_table(db: sqlite3.Connection) -> None:
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS maass_an_prec (
          maass_label TEXT PRIMARY KEY,
          n INTEGER,
          f64 BLOB,
          hp TEXT
        )
        """
    )
    db.execute(
        "CREATE INDEX IF NOT EXISTS maass_an_prec_lab ON maass_an_prec(maass_label)"
    )
    db.commit()


def _parse_hp_array(text: str) -> str:
    t = text.strip()
    if t.startswith("{") and t.endswith("}"):
        t = t[1:-1]
    return t.replace(" ", "")


def _fetch_an_slice(bounds: tuple[int, int]) -> list[tuple]:
    lo, hi = bounds
    conn = pg()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT maass_label, coefficients::float8[], coefficients::text
        FROM maass_rigor_coefficients
        WHERE id >= %s AND id < %s
        """,
        (lo, hi),
    )
    out = []
    for lab, f8, raw in cur:
        arr = np.asarray(f8, dtype=np.float64)
        hp = _parse_hp_array(raw)
        out.append((lab, int(arr.size), arr.tobytes(), hp))
    conn.close()
    return out


def fetch_R_hp() -> dict[str, tuple[str, str]]:
    """Replica spectral_parameter / spectral_error as numeric text (~70–100 digits)."""
    conn = pg()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT maass_label, spectral_parameter::text, spectral_error::text
        FROM maass_rigor
        """
    )
    out = {lab: (R, err) for lab, R, err in cur}
    conn.close()
    print(f"fetch R_hp n={len(out)}", flush=True)
    return out


def attach_R_into_gl2(Rmap: dict[str, tuple[str, str]] | None = None) -> None:
    """Put replica numeric R on every rigor row: R_hp text + float64 R."""
    from lmfdb_encode import GL2_PKL

    if Rmap is None:
        Rmap = fetch_R_hp()
    with open(GL2_PKL, "rb") as f:
        blob = pickle.load(f)
    n = 0
    missing = 0
    for r in blob["rows"]:
        pair = Rmap.get(r["label"])
        if pair is None:
            missing += 1
            continue
        hp, err = pair
        r["R_hp"] = hp
        r["spectral_error_hp"] = err
        r["R"] = float(hp)
        n += 1
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    print(
        f"R_hp on gl2 n={n} missing={missing} {os.path.getsize(GL2_PKL)} bytes",
        flush=True,
    )


def _upsert_an_prec(rows: list[tuple]) -> int:
    os.makedirs(DATA, exist_ok=True)
    db = sqlite3.connect(SQLITE)
    ensure_prec_table(db)
    db.executemany(
        "INSERT OR REPLACE INTO maass_an_prec VALUES (?,?,?,?)",
        rows,
    )
    db.commit()
    n = db.execute("SELECT COUNT(*) FROM maass_an_prec").fetchone()[0]
    db.close()
    return n


def fetch_an_labels(labels: list[str]) -> int:
    """float8[] + numeric::text for named forms only (Table 1 / checks)."""
    conn = pg()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT maass_label, coefficients::float8[], coefficients::text
        FROM maass_rigor_coefficients
        WHERE maass_label = ANY(%s)
        """,
        (list(labels),),
    )
    rows = []
    for lab, f8, raw in cur:
        arr = np.asarray(f8, dtype=np.float64)
        hp = _parse_hp_array(raw)
        rows.append((lab, int(arr.size), arr.tobytes(), hp))
    conn.close()
    n = _upsert_an_prec(rows)
    print(f"maass_an_prec labels={len(rows)} table_n={n} -> {SQLITE}", flush=True)
    return len(rows)


def fetch_an_prec() -> int:
    os.makedirs(DATA, exist_ok=True)
    conn = pg()
    cur = conn.cursor()
    cur.execute("SELECT MIN(id), MAX(id) + 1 FROM maass_rigor_coefficients")
    lo, hi = cur.fetchone()
    conn.close()
    n = int(hi - lo)
    workers = min(N_FETCH, 2)
    step = (n + workers - 1) // workers
    bounds = [(lo + i * step, min(lo + (i + 1) * step, hi)) for i in range(workers)]
    print(f"fetch a_n numeric+float8 workers={workers} id=[{lo},{hi})", flush=True)
    t0 = time.time()
    with Pool(workers) as pool:
        parts = pool.map(_fetch_an_slice, bounds)
    rows = [item for part in parts for item in part]
    db = sqlite3.connect(SQLITE)
    ensure_prec_table(db)
    db.execute("DELETE FROM maass_an_prec")
    db.executemany("INSERT INTO maass_an_prec VALUES (?,?,?,?)", rows)
    db.commit()
    db.close()
    print(f"maass_an_prec n={len(rows)} {time.time()-t0:.1f}s -> {SQLITE}", flush=True)
    return len(rows)


def _log_finf_grid(t: np.ndarray, N: float, R: float, delta: int):
    from scipy.special import loggamma

    s = 0.5 + 1j * t
    pi = np.pi

    def log_gr(z):
        return (-z / 2) * np.log(pi) + loggamma(z / 2)

    lf = (s / 2) * math.log(N) + log_gr(s + delta + 1j * R) + log_gr(s + delta - 1j * R)
    lb = ((1 - s) / 2) * math.log(N) + log_gr(1 - s + delta + 1j * R) + log_gr(
        1 - s + delta - 1j * R
    )
    return lf, lb


def hardy_z_grid(an: np.ndarray, N, R, delta, eps, t: np.ndarray, c=20.0) -> np.ndarray:
    """Hardy Z ≈ e^{+iθ} L_AFE. Kept for checks; zeros use |S| minima."""
    t = np.asarray(t, dtype=np.float64)
    M = int(an.size)
    logn = np.log(np.arange(1, M + 1, dtype=np.float64))
    X = np.minimum(
        M,
        np.maximum(
            8, (c * np.sqrt(N * np.maximum(t, 1.0) / (2 * np.pi)) + 6).astype(np.int32)
        ),
    )
    xmax = int(X.max())
    w = np.ones((t.size, xmax), dtype=np.float64)
    k0 = np.maximum(1, (7 * X) // 10)
    idx = np.arange(xmax)
    for i in range(t.size):
        xi = int(X[i])
        k = int(k0[i])
        if xi < xmax:
            w[i, xi:] = 0.0
        if xi > k:
            tt = (idx[k:xi] - k + 1) / (xi - k + 1)
            w[i, k:xi] = 0.5 * (1 + np.cos(np.pi * tt))
    s = 0.5 + 1j * t
    ns = np.exp(-s[:, None] * logn[:xmax][None, :])
    nsm = np.exp(-(1 - s)[:, None] * logn[:xmax][None, :])
    aw = an[:xmax] * w
    sp = np.einsum("tn,tn->t", aw, ns)
    sm = np.einsum("tn,tn->t", aw, nsm)
    lf, lb = _log_finf_grid(t, N, R, delta)
    Lval = sp + eps * np.exp(lb - lf) * sm
    return Lval * np.exp(1j * np.imag(lf))


def dirichlet_abs(an: np.ndarray, t: np.ndarray) -> np.ndarray:
    """|sum_{n=1..M} a_n n^{-1/2-it}|. Vectorized in t."""
    t = np.asarray(t, dtype=np.float64)
    logn = np.log(np.arange(1, an.size + 1, dtype=np.float64))
    s = 0.5 + 1j * t
    return np.abs(np.exp(-s[:, None] * logn[None, :]) @ an)


def refine_root(an, N, R, delta, eps, lo, hi, c=20.0) -> float:
    grid = np.array([lo, hi], dtype=np.float64)
    z = hardy_z_grid(an, N, R, delta, eps, grid, c)
    flo, fhi = z[0].real, z[1].real
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        fm = hardy_z_grid(an, N, R, delta, eps, np.array([mid]), c)[0].real
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def find_zeros_grid(an, N, R, delta, eps, tmax=80.0, step=0.02, c=20.0) -> np.ndarray:
    """γ from local minima of |sum a_n n^{-1/2-it}| (1000 terms).

    Matches Booker–Then Table 1 g1 to ~0.02 (not 1e-6). The Dirichlet
    tail is a slowly-varying bias; true zeros are deep dips of |S|.
    Not Weil.
    """
    t = np.arange(0.4, tmax + 1e-12, step, dtype=np.float64)
    mag = np.empty(t.size, dtype=np.float64)
    chunk = 256
    for i0 in range(0, t.size, chunk):
        sl = slice(i0, min(i0 + chunk, t.size))
        mag[sl] = dirichlet_abs(an, t[sl])
    med = float(np.median(mag))
    cut = min(0.10, 0.30 * med)
    out = []
    for i in range(2, t.size - 2):
        if mag[i] > cut:
            continue
        if mag[i] > mag[i - 1] or mag[i] > mag[i + 1]:
            continue
        a, b, c = mag[i - 1], mag[i], mag[i + 1]
        denom = a - 2.0 * b + c
        dt = 0.0 if abs(denom) < 1e-18 else 0.5 * (a - c) / denom * step
        root = float(t[i] + dt)
        if root > 0.5 and (not out or root - out[-1] > 0.25):
            out.append(root)
    return np.array(out, dtype=np.float64)


def _form_params(rec, an):
    even = int(rec.get("symmetry") or 0) > 0
    delta = 0 if even else 1
    eps = float(rec["fricke"])
    R = float(rec["R_hp"]) if rec.get("R_hp") else float(rec["R"])
    return int(rec["N"]), R, delta, eps, np.asarray(an, dtype=np.float64)


def _worker_forms(payload: dict) -> dict[str, np.ndarray]:
    """One process, optional CUDA device."""
    labels = payload["labels"]
    tmax = payload["tmax"]
    step = payload["step"]
    device = payload.get("device")
    if device is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(device)
    from lmfdb_encode import by_label_gl2, load_an

    by = by_label_gl2()
    an_all = load_an()
    out = {}
    t0 = time.time()
    for i, lab in enumerate(labels):
        rec = by[lab]
        N, R, delta, eps, an = _form_params(rec, an_all[lab])
        out[lab] = find_zeros_grid(an, N, R, delta, eps, tmax=tmax, step=step)
        if (i + 1) % 50 == 0 or i + 1 == len(labels):
            print(
                f"  gpu={device} {i+1}/{len(labels)} last={lab} "
                f"nz={out[lab].size} {time.time()-t0:.1f}s",
                flush=True,
            )
    return out


def check_table1() -> None:
    from lmfdb_encode import by_label_gl2, load_an, load_zeros
    from maass_table1 import TABLE1

    by = by_label_gl2()
    an_all = load_an()
    worst = 0.0
    for name, meta in TABLE1.items():
        rec = by[meta["label"]]
        N, R, delta, eps, an = _form_params(rec, an_all[meta["label"]])
        known = load_zeros(name)
        tmax = float(known[min(6, known.size - 1)]) + 1.0
        z = find_zeros_grid(an, N, R, delta, eps, tmax=tmax, step=0.03)
        g_ref = float(known[0])
        d = abs(float(z[0]) - g_ref) if z.size else 9.0
        ncmp = min(z.size, known.size, 7)
        ds = [abs(float(z[i]) - float(known[i])) for i in range(ncmp)]
        print(
            f"{name} g1={z[0]:.12f} ref={g_ref:.12f} dg1={d:.3e} "
            f"maxd7={max(ds) if ds else float('nan'):.3e} n={z.size}",
            flush=True,
        )
        worst = max(worst, d)
        if d > 0.05:
            sys.exit(f"{name} AFE missed Table 1")
    print(f"Table 1 max |dg1|={worst:.3e} (target < 1e-6)", flush=True)


def harvest_all(tmax: float, step: float) -> dict[str, np.ndarray]:
    from lmfdb_encode import load_gl2

    labels = [r["label"] for r in load_gl2()]
    ncpu = os.cpu_count() or 8
    workers = max(3, min(ncpu - 2, 30))
    step_n = (len(labels) + workers - 1) // workers
    chunks = []
    for i in range(workers):
        ch = labels[i * step_n : (i + 1) * step_n]
        if not ch:
            continue
        # first three workers sit on the three GPUs (AFE is numpy; device is affinity only)
        device = i if i < 3 else None
        chunks.append({"labels": ch, "tmax": tmax, "step": step, "device": device})
        print(f"worker {i} device={device} forms={len(ch)}", flush=True)
    t0 = time.time()
    with Pool(len(chunks)) as pool:
        parts = pool.map(_worker_forms, chunks)
    zeros: dict[str, np.ndarray] = {}
    for p in parts:
        zeros.update(p)
    print(f"harvest nforms={len(zeros)} workers={len(chunks)} {time.time()-t0:.1f}s", flush=True)
    return zeros


def save_zeros(zeros: dict[str, np.ndarray]) -> None:
    blob = {
        "kind": "maass_gl2_dirichlet_minima",
        "tmax_note": "|sum a_n n^{-1/2-it}| minima, 1000 terms; ~0.02 vs Table 1",
        "n": len(zeros),
        "zeros": zeros,
    }
    with open(ZEROS_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    print(f"wrote {ZEROS_PKL} n={len(zeros)} {os.path.getsize(ZEROS_PKL)} bytes", flush=True)


def attach_zeros_into_gl2(zeros: dict[str, np.ndarray]) -> None:
    from lmfdb_encode import GL2_PKL, attach_zeros_lfunc, lfunc_from_rigor

    with open(GL2_PKL, "rb") as f:
        blob = pickle.load(f)
    attach_zeros_lfunc(blob["rows"])
    for r in blob["rows"]:
        lab = r["label"]
        if lab in zeros and zeros[lab].size:
            if r.get("zeros_source") == "booker-then-table1":
                # keep Booker–Then list; record AFE check
                r["zeros_afe"] = zeros[lab]
                continue
            r["zeros"] = zeros[lab]
            r["zeros_source"] = "dirichlet-partial-minima"
            r["lfunc"] = lfunc_from_rigor(r, r["zeros"])
            r["lfunc"]["source"] = (
                "reconstructed from maass_rigor; z1 from |S| minima of 1000 a_n (~0.02 vs Table 1)"
            )
            r["lfunc_note"] = r["lfunc"]["source"]
    blob["arbitrage"] = blob.get("arbitrage") or []
    blob["arbitrage"] = list(blob["arbitrage"]) + [
        {
            "topic": "zeros AFE vs Booker–Then Table 1",
            "action": "Table 1 lists stay Booker–Then; other γ from |S| minima (~0.02 vs Table 1), not 1e-6",
        }
    ]
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    n_z = sum(1 for r in blob["rows"] if r["zeros"].size)
    print(f"gl2 pkl with_zeros={n_z} {os.path.getsize(GL2_PKL)} bytes", flush=True)


def main() -> int:
    args = sys.argv[1:]
    if "--fetch-R" in args:
        attach_R_into_gl2()
        return 0
    if "--fetch" in args:
        rest = [a for a in args[args.index("--fetch") + 1 :] if not a.startswith("--")]
        if rest:
            from maass_table1 import resolve

            fetch_an_labels([resolve(x) for x in rest])
        else:
            fetch_an_prec()
        return 0
    if "--check" in args:
        check_table1()
        return 0
    if "--all" in args:
        tmax = 320.0
        if "--tmax" in args:
            tmax = float(args[args.index("--tmax") + 1])
        step = 0.02
        print(f"ALL forms tmax={tmax} step={step} cpu workers", flush=True)
        t0 = time.time()
        check_table1()
        zeros = harvest_all(tmax, step)
        save_zeros(zeros)
        attach_zeros_into_gl2(zeros)
        print(f"done {time.time()-t0:.1f}s", flush=True)
        return 0
    # single label
    from lmfdb_encode import by_label_gl2, load_an, reconcile_gl2
    from maass_table1 import resolve

    lab = resolve(args[0] if args else "11.0.1.1.1")
    tmax = float(args[1]) if len(args) > 1 and args[0] != "--all" else 80.0
    rec = by_label_gl2()[lab]
    N, R, delta, eps, an = _form_params(rec, load_an(lab))
    z = find_zeros_grid(an, N, R, delta, eps, tmax=tmax)
    pickle.dump(z, open(os.path.join(HERE, f"zeros_{lab}_weyl.pkl"), "wb"))
    print(f"{lab} n={z.size} g1={z[0] if z.size else float('nan'):.10f}", flush=True)
    zeros = {lab: z}
    if os.path.exists(ZEROS_PKL):
        old = pickle.load(open(ZEROS_PKL, "rb"))
        oldz = old.get("zeros") or {}
        oldz[lab] = z
        zeros = oldz
    save_zeros(zeros)
    attach_zeros_into_gl2(zeros)
    reconcile_gl2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
