#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Dump LMFDB public replica locally, then index and emit pkls.

    python code/lmfdb_dump.py

Replica (read-only, public):
  host=devmirror.lmfdb.xyz db=lmfdb user=lmfdb
Override with env LMFDB_DSN.

Writes gitignored data/lmfdb_mirror.sqlite (indexed) and scanner pkls:
  code/lmfdb_maass_gl2.pkl
  code/lmfdb_dirichlet.pkl
  code/lmfdb_maass_an_N*.pkl  (all levels, sharded)

Full a_n for every rigor form stay in sqlite. Replica: at most
LMFDB_WORKERS connections (default 2). Not Weil.
"""
from __future__ import annotations

import os
import pickle
import sqlite3
import sys
import time
from multiprocessing import Pool

import numpy as np
import psycopg2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
SQLITE = os.path.join(DATA, "lmfdb_mirror.sqlite")
DSN = os.environ.get(
    "LMFDB_DSN",
    "host=devmirror.lmfdb.xyz port=5432 dbname=lmfdb user=lmfdb password=lmfdb",
)
CITE = {
    "source": "LMFDB",
    "url": "https://www.lmfdb.org",
    "replica": "devmirror.lmfdb.xyz",
    "year": 2026,
    "accessed": "2026-09-07",
}
DIRICHLET_MOD_CAP = 1000
AN_SHARDS = ((1, 20), (21, 50), (51, 80), (81, 105))
N_WORKERS = max(1, min(2, int(os.environ.get("LMFDB_WORKERS", "2"))))


def pg():
    conn = psycopg2.connect(DSN, connect_timeout=30)
    return conn


def open_sqlite(wipe: bool = True) -> sqlite3.Connection:
    os.makedirs(DATA, exist_ok=True)
    if wipe and os.path.exists(SQLITE):
        os.remove(SQLITE)
    db = sqlite3.connect(SQLITE)
    db.execute("PRAGMA journal_mode=OFF")
    db.execute("PRAGMA synchronous=OFF")
    db.execute("PRAGMA temp_store=MEMORY")
    db.executescript(
        """
        CREATE TABLE maass_rigor (
          maass_label TEXT PRIMARY KEY,
          level INTEGER,
          weight INTEGER,
          degree INTEGER,
          conrey_index INTEGER,
          character TEXT,
          nspec INTEGER,
          symmetry INTEGER,
          fricke INTEGER,
          R REAL,
          spectral_error REAL
        );
        CREATE TABLE maass_an (
          maass_label TEXT PRIMARY KEY,
          n INTEGER,
          coeffs BLOB
        );
        CREATE TABLE dirichlet (
          label TEXT PRIMARY KEY,
          modulus INTEGER,
          conductor INTEGER,
          orbit INTEGER,
          ord INTEGER,
          degree INTEGER,
          first INTEGER,
          last INTEGER,
          is_even INTEGER,
          is_primitive INTEGER,
          is_real INTEGER
        );
        """
    )
    return db


def dump_maass(pg_conn, db: sqlite3.Connection) -> int:
    cur = pg_conn.cursor()
    cur.execute(
        """
        SELECT maass_label, level, weight, conrey_index, nspec,
               symmetry, fricke_eigenvalue, spectral_parameter, spectral_error
        FROM maass_rigor
        """
    )
    rows = []
    for lab, N, w, a, nspec, sym, fr, R, err in cur:
        rows.append(
            (
                lab,
                int(N),
                int(w),
                2,
                int(a),
                f"{int(N)}.{int(a)}",
                int(nspec),
                int(sym),
                int(fr),
                float(R),
                float(err) if err is not None else None,
            )
        )
    db.executemany(
        "INSERT INTO maass_rigor VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        rows,
    )
    db.commit()
    print(f"maass_rigor {len(rows)}", flush=True)
    return len(rows)


def _fetch_an_slice(bounds: tuple[int, int]) -> list[tuple[str, int, bytes]]:
    lo, hi = bounds
    conn = pg()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT maass_label, coefficients::float4[]
        FROM maass_rigor_coefficients
        WHERE id >= %s AND id < %s
        """,
        (lo, hi),
    )
    out = []
    for lab, coeffs in cur:
        arr = np.asarray(coeffs, dtype=np.float32)
        out.append((lab, int(arr.size), arr.tobytes()))
    conn.close()
    return out


def dump_an(db: sqlite3.Connection) -> int:
    conn = pg()
    cur = conn.cursor()
    cur.execute("SELECT MIN(id), MAX(id) + 1 FROM maass_rigor_coefficients")
    lo, hi = cur.fetchone()
    conn.close()
    n = int(hi - lo)
    workers = min(N_WORKERS, max(1, n // 400))
    step = (n + workers - 1) // workers
    bounds = [(lo + i * step, min(lo + (i + 1) * step, hi)) for i in range(workers)]
    print(f"a_n slices={len(bounds)} workers={workers} id=[{lo},{hi})", flush=True)
    t0 = time.time()
    with Pool(workers) as pool:
        parts = pool.map(_fetch_an_slice, bounds)
    rows = [item for part in parts for item in part]
    db.executemany("INSERT INTO maass_an VALUES (?,?,?)", rows)
    db.commit()
    print(f"maass_an {len(rows)}  {time.time()-t0:.1f}s", flush=True)
    return len(rows)


def _fetch_chi_slice(bounds: tuple[int, int]) -> list[tuple]:
    lo, hi = bounds
    conn = pg()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT label, modulus, conductor, orbit, "order", degree,
               first, last, is_even, is_primitive, is_real
        FROM char_dirichlet
        WHERE modulus >= %s AND modulus < %s
        """,
        (lo, hi),
    )
    out = []
    for row in cur.fetchall():
        out.append(
            (
                row[0],
                int(row[1]),
                int(row[2]),
                int(row[3]),
                int(row[4]),
                int(row[5]),
                int(row[6]),
                int(row[7]),
                1 if row[8] else 0,
                1 if row[9] else 0,
                1 if row[10] else 0,
            )
        )
    conn.close()
    return out


def dump_dirichlet(db: sqlite3.Connection, cap: int) -> int:
    workers = min(N_WORKERS, max(1, cap // 50))
    step = (cap + workers) // workers
    bounds = [(i * step, min((i + 1) * step, cap + 1)) for i in range(workers)]
    print(f"chi slices={len(bounds)} workers={workers} modulus<= {cap}", flush=True)
    t0 = time.time()
    with Pool(workers) as pool:
        parts = pool.map(_fetch_chi_slice, bounds)
    rows = [item for part in parts for item in part]
    db.executemany(
        "INSERT OR REPLACE INTO dirichlet VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        rows,
    )
    db.commit()
    print(f"dirichlet modulus<={cap} n={len(rows)}  {time.time()-t0:.1f}s", flush=True)
    return len(rows)


def index_sqlite(db: sqlite3.Connection) -> None:
    db.executescript(
        """
        CREATE INDEX IF NOT EXISTS maass_level ON maass_rigor(level);
        CREATE INDEX IF NOT EXISTS maass_chi ON maass_rigor(character);
        CREATE INDEX IF NOT EXISTS dir_mod ON dirichlet(modulus);
        CREATE INDEX IF NOT EXISTS dir_cond ON dirichlet(conductor);
        CREATE INDEX IF NOT EXISTS dir_prim ON dirichlet(is_primitive, modulus);
        ANALYZE;
        """
    )
    db.commit()
    print("sqlite indexes ready", flush=True)


def emit_pkls(db: sqlite3.Connection) -> None:
    sys.path.insert(0, HERE)
    from lmfdb_encode import CITE as CSV_CITE
    from lmfdb_encode import GL2_PKL, GL3_PKL

    cite = dict(CSV_CITE)
    cite.update(CITE)

    gl2 = []
    for r in db.execute("SELECT * FROM maass_rigor ORDER BY level, R"):
        (
            lab, N, w, deg, a, chi, nspec, sym, fr, R, err,
        ) = r
        gl2.append(
            {
                "label": lab,
                "N": N,
                "weight": w,
                "degree": deg,
                "conrey_index": a,
                "character": chi,
                "nspec": nspec,
                "R": R,
                "spectral_error": err,
                "symmetry": sym,
                "fricke": fr,
            }
        )
    blob = {"cite": cite, "kind": "gl2_maass_rigor", "n": len(gl2), "rows": gl2}
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    print(f"wrote {GL2_PKL} n={len(gl2)} {os.path.getsize(GL2_PKL)} bytes", flush=True)

    chi_rows = []
    for r in db.execute(
        "SELECT * FROM dirichlet ORDER BY modulus, first"
    ):
        chi_rows.append(
            {
                "label": r[0],
                "modulus": r[1],
                "conductor": r[2],
                "orbit": r[3],
                "order": r[4],
                "degree": r[5],
                "first": r[6],
                "last": r[7],
                "is_even": bool(r[8]),
                "is_primitive": bool(r[9]),
                "is_real": bool(r[10]),
            }
        )
    dpath = os.path.join(HERE, "lmfdb_dirichlet.pkl")
    with open(dpath, "wb") as f:
        pickle.dump(
            {
                "cite": cite,
                "kind": "char_dirichlet",
                "modulus_cap": DIRICHLET_MOD_CAP,
                "n": len(chi_rows),
                "rows": chi_rows,
            },
            f,
            protocol=4,
        )
    print(f"wrote {dpath} n={len(chi_rows)} {os.path.getsize(dpath)} bytes", flush=True)

    for lo, hi in AN_SHARDS:
        an = {}
        for lab, _n, blob in db.execute(
            """
            SELECT a.maass_label, a.n, a.coeffs
            FROM maass_an a
            JOIN maass_rigor r ON r.maass_label = a.maass_label
            WHERE r.level >= ? AND r.level <= ?
            """,
            (lo, hi),
        ):
            an[lab] = np.frombuffer(blob, dtype=np.float32).copy()
        apath = os.path.join(HERE, f"lmfdb_maass_an_N{lo:03d}_{hi:03d}.pkl")
        with open(apath, "wb") as f:
            pickle.dump(
                {
                    "cite": cite,
                    "kind": "maass_rigor_coefficients",
                    "level_lo": lo,
                    "level_hi": hi,
                    "n": len(an),
                    "an": an,
                },
                f,
                protocol=4,
            )
        print(f"wrote {apath} n={len(an)} {os.path.getsize(apath)} bytes", flush=True)

    # keep existing gl3 pkl if present; dump does not replace it
    if os.path.exists(GL3_PKL):
        print(f"keep {GL3_PKL}", flush=True)


def main() -> int:
    t0 = time.time()
    emit_only = "--emit-only" in sys.argv
    if emit_only:
        if not os.path.exists(SQLITE):
            sys.exit(f"missing {SQLITE}")
        db = sqlite3.connect(SQLITE)
        emit_pkls(db)
        db.close()
        print(f"emit-only {time.time()-t0:.1f}s", flush=True)
        return 0
    print(f"dump -> {SQLITE} workers={N_WORKERS}", flush=True)
    db = open_sqlite(wipe=True)
    conn = pg()
    dump_maass(conn, db)
    conn.close()
    dump_an(db)
    dump_dirichlet(db, DIRICHLET_MOD_CAP)
    index_sqlite(db)
    emit_pkls(db)
    db.close()
    print(f"done {time.time()-t0:.1f}s sqlite={os.path.getsize(SQLITE)} bytes", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
