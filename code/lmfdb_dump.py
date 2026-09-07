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
  code/lmfdb_lfunc_maass.pkl      (MaassGL2/3/4 zeros + conjugate)
  code/lmfdb_lfunc_dirichlet.pkl  (DIR q<=200 zeros + conjugate)
  code/lmfdb_lfunc_cmf.pkl        (CMF N<=100 k<=12 zeros + conjugate)
  code/lmfdb_mf_newforms.pkl      (holomorphic newform metadata)

python code/lmfdb_dump.py --lfunc
  only the L-function / holomorphic tables (2 replica conns, indexed
  type/url/Lhash/level; no ILIKE). GL2 rigor L-functions are not in
  LMFDB ('L-function not computed'). Table 1 γ go on the rigor pkl.
  Not Weil.
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
DIR_LFUNC_CAP = 200
CMF_LEVEL_CAP = 100
CMF_WEIGHT_CAP = 12
AN_SHARDS = ((1, 20), (21, 50), (51, 80), (81, 105))
N_WORKERS = max(1, min(2, int(os.environ.get("LMFDB_WORKERS", "2"))))
LFUNC_PKL_MAASS = os.path.join(HERE, "lmfdb_lfunc_maass.pkl")
LFUNC_PKL_DIR = os.path.join(HERE, "lmfdb_lfunc_dirichlet.pkl")
LFUNC_PKL_CMF = os.path.join(HERE, "lmfdb_lfunc_cmf.pkl")
MF_PKL = os.path.join(HERE, "lmfdb_mf_newforms.pkl")


def pg():
    conn = psycopg2.connect(DSN, connect_timeout=30)
    cur = conn.cursor()
    cur.execute("SET statement_timeout = '180s'")
    cur.close()
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
    ensure_lfunc_tables(db)
    return db


def ensure_lfunc_tables(db: sqlite3.Connection) -> None:
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS lfunc (
          kind TEXT NOT NULL,
          url TEXT NOT NULL,
          label TEXT,
          conjugate TEXT,
          degree INTEGER,
          conductor REAL,
          central_character TEXT,
          primitive INTEGER,
          self_dual INTEGER,
          z1 REAL,
          nz INTEGER,
          zeros BLOB,
          PRIMARY KEY (kind, url)
        );
        CREATE TABLE IF NOT EXISTS mf_newforms (
          label TEXT PRIMARY KEY,
          level INTEGER,
          weight INTEGER,
          char_orbit_label TEXT,
          conrey_index INTEGER,
          dim INTEGER,
          analytic_rank INTEGER,
          is_self_dual INTEGER,
          char_is_real INTEGER,
          fricke INTEGER
        );
        """
    )
    db.commit()


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


def _pack_zeros(zs) -> tuple[int, bytes]:
    if not zs:
        return 0, b""
    arr = np.asarray(zs, dtype=np.float32)
    return int(arr.size), arr.tobytes()


def _pack_lfunc(kind: str, rows: list) -> list[tuple]:
    out = []
    for url, lab, conj, deg, cond, chi, prim, sd, z1, zs in rows:
        nz, blob = _pack_zeros(zs)
        out.append(
            (
                kind,
                url,
                lab,
                conj,
                int(deg) if deg is not None else None,
                float(cond) if cond is not None else None,
                chi,
                None if prim is None else int(bool(prim)),
                None if sd is None else int(bool(sd)),
                float(z1) if z1 is not None else None,
                nz,
                blob,
            )
        )
    return out


_LFUNC_COLS = """
    i.url, L.label, L.conjugate, L.degree, L.conductor,
    L.central_character, L.primitive, L.self_dual, L.z1,
    CASE WHEN jsonb_typeof(L.positive_zeros)='array'
         THEN ARRAY(SELECT jsonb_array_elements_text(L.positive_zeros)::real)
         ELSE ARRAY[]::real[]
    END
"""


def _fetch_maass(conn) -> list[tuple]:
    cur = conn.cursor()
    out = []
    for kind in ("MaassGL2", "MaassGL3", "MaassGL4"):
        cur.execute(
            f"""
            SELECT {_LFUNC_COLS}
            FROM lfunc_instances i
            LEFT JOIN lfunc_lfunctions L ON L."Lhash" = i."Lhash"
            WHERE i.type = %s
            """,
            (kind,),
        )
        packed = _pack_lfunc(kind, cur.fetchall())
        print(f"  {kind} n={len(packed)}", flush=True)
        out.extend(packed)
    return out


def _fetch_dir_slice(conn, lo: int, hi: int) -> list[tuple]:
    cur = conn.cursor()
    meta_cols = """
        i.url, L.label, L.conjugate, L.degree, L.conductor,
        L.central_character, L.primitive, L.self_dual, L.z1
    """
    meta = []
    step = 20
    for start in range(lo, hi + 1, step):
        stop = min(start + step - 1, hi)
        parts = []
        for n in range(start, stop + 1):
            parts.append(
                f"""
                SELECT {meta_cols}
                FROM lfunc_instances i
                JOIN lfunc_lfunctions L ON L."Lhash" = i."Lhash"
                WHERE i.url >= 'Character/Dirichlet/{n}/'
                  AND i.url <  'Character/Dirichlet/{n}/' || chr(127)
                """
            )
        cur.execute(" UNION ALL ".join(parts))
        meta.extend(cur.fetchall())
        print(f"  DIR meta q={start}..{stop} n={len(meta)}", flush=True)
    zeros_by_url = {}
    chunk = 80
    urls = [r[0] for r in meta]
    for i in range(0, len(urls), chunk):
        part = urls[i : i + chunk]
        cur.execute(
            """
            SELECT i.url,
                   CASE WHEN jsonb_typeof(L.positive_zeros)='array'
                        THEN ARRAY(
                          SELECT jsonb_array_elements_text(L.positive_zeros)::real
                        )
                        ELSE ARRAY[]::real[]
                   END
            FROM lfunc_instances i
            JOIN lfunc_lfunctions L ON L."Lhash" = i."Lhash"
            WHERE i.url = ANY(%s)
            """,
            (part,),
        )
        for url, zs in cur.fetchall():
            zeros_by_url[url] = zs
        print(f"  DIR zeros {min(i+chunk, len(urls))}/{len(urls)}", flush=True)
    packed_src = [row + (zeros_by_url.get(row[0], []),) for row in meta]
    out = _pack_lfunc("DIR", packed_src)
    print(f"  DIR q={lo}..{hi} n={len(out)}", flush=True)
    return out


def _fetch_mf(conn) -> list[tuple]:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT label, level, weight, char_orbit_label, conrey_index, dim,
               analytic_rank, is_self_dual, char_is_real, fricke_eigenval
        FROM mf_newforms
        WHERE level <= %s AND weight <= %s
        """,
        (CMF_LEVEL_CAP, CMF_WEIGHT_CAP),
    )
    rows = []
    for r in cur.fetchall():
        rows.append(
            (
                r[0],
                int(r[1]),
                int(r[2]),
                r[3],
                int(r[4]) if r[4] is not None else None,
                int(r[5]),
                int(r[6]) if r[6] is not None else None,
                None if r[7] is None else int(bool(r[7])),
                None if r[8] is None else int(bool(r[8])),
                int(r[9]) if r[9] is not None else None,
            )
        )
    print(f"  mf_newforms N<={CMF_LEVEL_CAP} k<={CMF_WEIGHT_CAP} n={len(rows)}", flush=True)
    return rows


def _fetch_cmf(conn) -> list[tuple]:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT label FROM mf_newforms
        WHERE level <= %s AND weight <= %s
        """,
        (CMF_LEVEL_CAP, CMF_WEIGHT_CAP),
    )
    urls = [
        "ModularForm/GL2/Q/holomorphic/" + lab.replace(".", "/")
        for (lab,) in cur.fetchall()
    ]
    out = []
    chunk = 400
    for i in range(0, len(urls), chunk):
        part = urls[i : i + chunk]
        cur.execute(
            f"""
            SELECT {_LFUNC_COLS}
            FROM lfunc_instances i
            JOIN lfunc_lfunctions L ON L."Lhash" = i."Lhash"
            WHERE i.url = ANY(%s)
            """,
            (part,),
        )
        out.extend(_pack_lfunc("CMF", cur.fetchall()))
    print(f"  CMF join n={len(out)}", flush=True)
    return out


def _lfunc_bundle(name: str) -> dict:
    """One replica connection. Two bundles run as the two workers."""
    t0 = time.time()
    conn = pg()
    try:
        mid = DIR_LFUNC_CAP // 2
        if name == "A":
            rows = _fetch_maass(conn)
            rows.extend(_fetch_dir_slice(conn, 1, mid))
            blob = {"lfunc": rows, "mf": []}
        else:
            mf = _fetch_mf(conn)
            rows = _fetch_cmf(conn)
            rows.extend(_fetch_dir_slice(conn, mid + 1, DIR_LFUNC_CAP))
            blob = {"lfunc": rows, "mf": mf}
    finally:
        conn.close()
    print(f"bundle {name} {time.time()-t0:.1f}s", flush=True)
    return blob


def dump_lfunc(db: sqlite3.Connection) -> tuple[int, int]:
    ensure_lfunc_tables(db)
    db.execute("DELETE FROM lfunc")
    db.execute("DELETE FROM mf_newforms")
    db.commit()
    workers = min(2, N_WORKERS)
    names = ("A", "B") if workers > 1 else ("A",)
    print(f"lfunc workers={workers} bundles={names}", flush=True)
    t0 = time.time()
    if workers > 1:
        with Pool(workers) as pool:
            parts = pool.map(_lfunc_bundle, ["A", "B"])
    else:
        # single conn: run both bundles sequentially
        parts = [_lfunc_bundle("A")]
        conn = pg()
        try:
            mf = _fetch_mf(conn)
            rows = _fetch_cmf(conn)
            rows.extend(_fetch_dir_slice(conn, DIR_LFUNC_CAP // 2 + 1, DIR_LFUNC_CAP))
        finally:
            conn.close()
        parts.append({"lfunc": rows, "mf": mf})
    lfunc_rows = [item for part in parts for item in part["lfunc"]]
    mf_rows = [item for part in parts for item in part["mf"]]
    db.executemany(
        "INSERT OR REPLACE INTO lfunc VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        lfunc_rows,
    )
    if mf_rows:
        db.executemany(
            "INSERT OR REPLACE INTO mf_newforms VALUES (?,?,?,?,?,?,?,?,?,?)",
            mf_rows,
        )
    db.commit()
    print(
        f"lfunc n={len(lfunc_rows)} mf={len(mf_rows)}  {time.time()-t0:.1f}s",
        flush=True,
    )
    return len(lfunc_rows), len(mf_rows)


def index_sqlite(db: sqlite3.Connection) -> None:
    db.executescript(
        """
        CREATE INDEX IF NOT EXISTS maass_level ON maass_rigor(level);
        CREATE INDEX IF NOT EXISTS maass_chi ON maass_rigor(character);
        CREATE INDEX IF NOT EXISTS dir_mod ON dirichlet(modulus);
        CREATE INDEX IF NOT EXISTS dir_cond ON dirichlet(conductor);
        CREATE INDEX IF NOT EXISTS dir_prim ON dirichlet(is_primitive, modulus);
        CREATE INDEX IF NOT EXISTS lfunc_kind ON lfunc(kind);
        CREATE INDEX IF NOT EXISTS lfunc_chi ON lfunc(central_character);
        CREATE INDEX IF NOT EXISTS mf_level ON mf_newforms(level, weight);
        ANALYZE;
        """
    )
    db.commit()
    print("sqlite indexes ready", flush=True)


def emit_pkls(db: sqlite3.Connection) -> None:
    sys.path.insert(0, HERE)
    from lmfdb_encode import CITE as CSV_CITE
    from lmfdb_encode import GL2_PKL, GL3_PKL, attach_zeros_lfunc

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
    attach_zeros_lfunc(gl2)
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

    emit_lfunc_pkls(db, cite)


def _row_lfunc(kind, url, lab, conj, deg, cond, chi, prim, sd, z1, nz, blob):
    zeros = np.frombuffer(blob, dtype=np.float32).copy() if blob else np.zeros(0, np.float32)
    return {
        "type": kind,
        "url": url,
        "label": lab,
        "conjugate": conj,
        "degree": deg,
        "conductor": cond,
        "central_character": chi,
        "primitive": None if prim is None else bool(prim),
        "self_dual": None if sd is None else bool(sd),
        "z1": z1,
        "zeros": zeros,
    }


def emit_lfunc_pkls(db: sqlite3.Connection, cite: dict | None = None) -> None:
    got = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='lfunc'"
    ).fetchone()
    if not got:
        print("no lfunc table", flush=True)
        return
    if cite is None:
        sys.path.insert(0, HERE)
        from lmfdb_encode import CITE as CSV_CITE

        cite = dict(CSV_CITE)
        cite.update(CITE)
    by_kind: dict[str, list] = {}
    for r in db.execute("SELECT * FROM lfunc"):
        rec = _row_lfunc(*r)
        by_kind.setdefault(rec["type"], []).append(rec)

    maass = []
    for k in ("MaassGL2", "MaassGL3", "MaassGL4"):
        maass.extend(by_kind.get(k, []))
    with open(LFUNC_PKL_MAASS, "wb") as f:
        pickle.dump(
            {
                "cite": cite,
                "kind": "lfunc_maass",
                "n": len(maass),
                "n_gl2": len(by_kind.get("MaassGL2", [])),
                "n_gl3": len(by_kind.get("MaassGL3", [])),
                "n_gl4": len(by_kind.get("MaassGL4", [])),
                "rows": maass,
            },
            f,
            protocol=4,
        )
    print(
        f"wrote {LFUNC_PKL_MAASS} n={len(maass)} "
        f"{os.path.getsize(LFUNC_PKL_MAASS)} bytes",
        flush=True,
    )

    drows = by_kind.get("DIR", [])
    with open(LFUNC_PKL_DIR, "wb") as f:
        pickle.dump(
            {
                "cite": cite,
                "kind": "lfunc_dirichlet",
                "modulus_cap": DIR_LFUNC_CAP,
                "n": len(drows),
                "rows": drows,
            },
            f,
            protocol=4,
        )
    print(
        f"wrote {LFUNC_PKL_DIR} n={len(drows)} {os.path.getsize(LFUNC_PKL_DIR)} bytes",
        flush=True,
    )

    crows = by_kind.get("CMF", [])
    with open(LFUNC_PKL_CMF, "wb") as f:
        pickle.dump(
            {
                "cite": cite,
                "kind": "lfunc_cmf",
                "level_cap": CMF_LEVEL_CAP,
                "weight_cap": CMF_WEIGHT_CAP,
                "n": len(crows),
                "rows": crows,
            },
            f,
            protocol=4,
        )
    print(
        f"wrote {LFUNC_PKL_CMF} n={len(crows)} {os.path.getsize(LFUNC_PKL_CMF)} bytes",
        flush=True,
    )

    mf = []
    for r in db.execute("SELECT * FROM mf_newforms ORDER BY level, weight, label"):
        mf.append(
            {
                "label": r[0],
                "level": r[1],
                "weight": r[2],
                "char_orbit_label": r[3],
                "conrey_index": r[4],
                "dim": r[5],
                "analytic_rank": r[6],
                "is_self_dual": None if r[7] is None else bool(r[7]),
                "char_is_real": None if r[8] is None else bool(r[8]),
                "fricke": r[9],
            }
        )
    with open(MF_PKL, "wb") as f:
        pickle.dump(
            {
                "cite": cite,
                "kind": "mf_newforms",
                "level_cap": CMF_LEVEL_CAP,
                "weight_cap": CMF_WEIGHT_CAP,
                "n": len(mf),
                "rows": mf,
            },
            f,
            protocol=4,
        )
    print(f"wrote {MF_PKL} n={len(mf)} {os.path.getsize(MF_PKL)} bytes", flush=True)


def main() -> int:
    t0 = time.time()
    emit_only = "--emit-only" in sys.argv
    lfunc_only = "--lfunc" in sys.argv
    if emit_only:
        if not os.path.exists(SQLITE):
            sys.exit(f"missing {SQLITE}")
        db = sqlite3.connect(SQLITE)
        emit_pkls(db)
        db.close()
        print(f"emit-only {time.time()-t0:.1f}s", flush=True)
        return 0
    if lfunc_only:
        if not os.path.exists(SQLITE):
            sys.exit(f"missing {SQLITE}")
        print(f"lfunc -> {SQLITE} workers={N_WORKERS}", flush=True)
        db = sqlite3.connect(SQLITE)
        db.execute("PRAGMA journal_mode=OFF")
        db.execute("PRAGMA synchronous=OFF")
        dump_lfunc(db)
        index_sqlite(db)
        sys.path.insert(0, HERE)
        from lmfdb_encode import CITE as CSV_CITE

        cite = dict(CSV_CITE)
        cite.update(CITE)
        emit_lfunc_pkls(db, cite)
        db.close()
        print(
            f"lfunc-only {time.time()-t0:.1f}s sqlite={os.path.getsize(SQLITE)} bytes",
            flush=True,
        )
        return 0
    print(f"dump -> {SQLITE} workers={N_WORKERS}", flush=True)
    db = open_sqlite(wipe=True)
    conn = pg()
    dump_maass(conn, db)
    conn.close()
    dump_an(db)
    dump_dirichlet(db, DIRICHLET_MOD_CAP)
    dump_lfunc(db)
    index_sqlite(db)
    emit_pkls(db)
    db.close()
    print(f"done {time.time()-t0:.1f}s sqlite={os.path.getsize(SQLITE)} bytes", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
