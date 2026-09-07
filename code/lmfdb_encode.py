#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""One catalog for GL2 Maass rigor, quorum χ, and GL3, for tools.

    from lmfdb_encode import by_label_gl2, by_chi, by_origin, load_zeros, load_an, load_lfunc
    rec = by_label_gl2()["1.0.1.1.1"]
    rec["R"], rec["zeros"], rec["lfunc"]["z1"]
    load_zeros("maass1")
    load_lfunc("11.0.1.1.1")                 # L-search columns, reconstructed
    load_lfunc("chi3")                       # lab name
    load_lfunc("Character/Dirichlet/3/2")    # LMFDB Origin (this is the χ)
    load_an("11.0.1.1.1")                    # 1000 a_n from replica

L-search columns on rec["lfunc"] (same names as LMFDB /L/ table):
  alpha, A, d, N, chi, mu, nu, w, prim, arith, rational,
  self_dual, arg_eps, r, z1, origin

Origin is LMFDB instance_urls[0]. For a Dirichlet L-function it
names the character: Character/Dirichlet/{q}/{n} (Conrey). χ on
the L-row is the central character (Conrey q.n). Lab names
(chi3, chim8) are aliases; Origin is the identity. Conrey 3.2
is also the Maass short label 3.0.1.2.1 — use Origin, not 3.2,
to mean the character.

GL2 rigor L-functions are not stored in lfunc_search (0 rows at
N=1 and N=11, degree 2, w=0). Completeness: 15659 *dynamic* GL2
Maass L. Columns are rebuilt from maass_rigor; A is the LMFDB
analytic conductor (verified on GL3 CSV). z1 from Booker–Then
Table 1 when we have zeros. Not Weil.

    python code/lmfdb_encode.py --reconcile
"""
from __future__ import annotations

import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GL2_PKL = os.path.join(HERE, "lmfdb_maass_gl2.pkl")
GL3_PKL = os.path.join(HERE, "lmfdb_maass_gl3.pkl")
CHI_PKL = os.path.join(HERE, "lmfdb_quorum_chi.pkl")
CATALOG_PKL = os.path.join(HERE, "lmfdb_catalog.pkl")
CITE = {
    "source": "LMFDB",
    "url": "https://www.lmfdb.org",
    "year": 2026,
    "accessed": "2026-09-07",
    "gl2": "https://www.lmfdb.org/ModularForm/GL2/Q/Maass/",
    "gl3": "https://www.lmfdb.org/L/",
    "dirichlet": "https://www.lmfdb.org/Character/Dirichlet/",
}


def encode() -> None:
    sys.path.insert(0, HERE)
    import lmfdb_maass_catalog as gl2
    import lmfdb_maass_gl3_catalog as gl3

    rows2 = []
    for r in gl2.load_csv():
        rows2.append(
            {
                "label": r["label"],
                "N": r["N"],
                "weight": r["weight"],
                "degree": r.get("degree", 2),
                "character": r["character"],
                "R": r["R"],
                "symmetry": r["symmetry"],
                "fricke": r["fricke"],
            }
        )
    blob2 = {"cite": CITE, "kind": "gl2_maass_rigor", "n": len(rows2), "rows": rows2}
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob2, f, protocol=4)
    print(f"gl2 n={len(rows2)} -> {GL2_PKL} ({os.path.getsize(GL2_PKL)} bytes)", flush=True)

    rows3 = []
    for r in gl3.load_csv():
        rows3.append(
            {
                "label": r["label"],
                "N": r["N"],
                "degree": r.get("degree", 3),
                "mu": r["mu"],
                "z1": r["z1"],
                "origin": r["origin"],
                "self_dual": r["self_dual"],
                "primitive": r["primitive"],
            }
        )
    blob3 = {"cite": CITE, "kind": "gl3_lfunc_search", "n": len(rows3), "rows": rows3}
    with open(GL3_PKL, "wb") as f:
        pickle.dump(blob3, f, protocol=4)
    print(f"gl3 n={len(rows3)} -> {GL3_PKL} ({os.path.getsize(GL3_PKL)} bytes)", flush=True)


# LMFDB /L/ table: Label, α, A, d, N, χ, μ, ν, w, prim, arith, ℚ,
# self-dual, Arg(ε), r, First zero, Origin.
LFUNC_COLUMNS = (
    "label", "alpha", "A", "d", "N", "chi", "mu", "nu", "w",
    "prim", "arith", "rational", "self_dual", "arg_eps", "r", "z1", "origin",
)
ARBITRAGE = [
    {
        "topic": "GL2 rigor L-functions not in lfunc_search",
        "lfunc_search": "0 rows for degree=2, motivic_weight=0, conductor 1 and 11",
        "lfunc_lfunctions": "origin ModularForm/GL2/Q/Maass/ empty; type=MaassGL2 is two N=101 leftovers",
        "lmfdb_completeness": "15659 dynamically computed GL2 Maass L (not stored)",
        "lmfdb_page_11.0.1.1.1": "L-function not computed",
        "action": "reconstruct L-search columns from maass_rigor; z1 from Booker–Then Table 1 when present",
    },
    {
        "topic": "analytic conductor A and alpha",
        "formula": "A = N exp(2 Re L_inf'(1/2)/L_inf(1/2)), alpha = A^(1/d), L_inf = product Gamma_R(s+mu)",
        "verified_on": "GL3 first CSV row A=0.048865567236632115, alpha=0.3655956178456336",
    },
    {
        "topic": "Arg(epsilon)",
        "action": "self-dual: root_angle 0 if Fricke=+1 else 1/2 (units of 2π). Not stored by LMFDB for these forms.",
    },
    {
        "topic": "Origin names the object, and for DIR the χ",
        "lmfdb": "L-search Origin = instance_urls[0]",
        "dirichlet": "Character/Dirichlet/{q}/{n} (Conrey). chi3 is this URL, not the nickname.",
        "gl2_maass": "ModularForm/GL2/Q/Maass/{N.k.a.m.d}",
        "collision": "Conrey 3.2 vs Maass short 3.2 = 3.0.1.2.1. Tools look up Origin.",
    },
]


def analytic_conductor_gammaR(N: int, mus: list[tuple[float, float]]) -> float:
    """LMFDB A for Gamma_R factors. mus are (real, imag) shifts."""
    import mpmath as mp

    def dlog_gr(z):
        return -mp.log(mp.pi) / 2 + mp.digamma(z / 2) / 2

    s = mp.mpf("0.5")
    tot = sum(dlog_gr(s + a + 1j * b) for a, b in mus)
    return float(N * mp.exp(2 * mp.re(tot)))


def lfunc_from_rigor(r: dict, zeros) -> dict:
    """L-search row rebuilt from maass_rigor. stored_in_lmfdb is False."""
    even = int(r.get("symmetry") or 0) > 0
    R = float(r["R"])
    N = int(r["N"])
    if even:
        mu = [(0.0, R), (0.0, -R)]
    else:
        mu = [(1.0, R), (1.0, -R)]
    A = analytic_conductor_gammaR(N, mu)
    z1 = float(zeros[0]) if zeros is not None and getattr(zeros, "size", len(zeros)) else None
    fr = r.get("fricke")
    arg_eps = None if fr is None else (0.0 if int(fr) > 0 else 0.5)
    src = "reconstructed from maass_rigor"
    if z1 is not None:
        src += "; z1 from booker-then-table1"
    return {
        "label": None,
        "alpha": A ** 0.5,
        "A": A,
        "d": 2,
        "N": N,
        "chi": r["character"],
        "mu": mu,
        "nu": [],
        "w": 0,
        "prim": True,
        "arith": False,
        "rational": False,
        "self_dual": True,
        "arg_eps": arg_eps,
        "r": 0 if z1 is not None else None,
        "z1": z1,
        "origin": f"ModularForm/GL2/Q/Maass/{r['label']}",
        "stored_in_lmfdb": False,
        "source": src,
    }


def attach_zeros_lfunc(rows: list[dict]) -> None:
    """Table 1 γ + reconstructed L-search columns on every rigor row."""
    from maass_table1 import ALIAS

    have: dict[str, tuple[str, np.ndarray]] = {}
    for name, lab in ALIAS.items():
        path = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
        if not os.path.exists(path):
            continue
        z = np.array(
            sorted(float(x) for x in pickle.load(open(path, "rb"))),
            dtype=np.float64,
        )
        have[lab] = ("booker-then-table1", z)
    for r in rows:
        lab = r["label"]
        if lab in have:
            src, z = have[lab]
            r["zeros"] = z
            r["zeros_source"] = src
        else:
            r["zeros"] = np.zeros(0, dtype=np.float64)
            r["zeros_source"] = None
        r["lfunc"] = lfunc_from_rigor(r, r["zeros"])
        r["origin"] = r["lfunc"]["origin"]
        r["lfunc_note"] = r["lfunc"]["source"]


def reconcile_gl2() -> None:
    global _ORIGIN
    with open(GL2_PKL, "rb") as f:
        blob = pickle.load(f)
    attach_zeros_lfunc(blob["rows"])
    blob["kind"] = "gl2_maass_rigor"
    blob["lfunc_columns"] = ",".join(LFUNC_COLUMNS)
    blob["arbitrage"] = ARBITRAGE
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    _ORIGIN = None
    n_z = sum(1 for r in blob["rows"] if r["zeros"].size)
    print(
        f"reconcile {GL2_PKL} n={blob['n']} with_zeros={n_z} "
        f"{os.path.getsize(GL2_PKL)} bytes",
        flush=True,
    )


def load_gl2() -> list[dict]:
    with open(GL2_PKL, "rb") as f:
        return pickle.load(f)["rows"]


def load_gl3() -> list[dict]:
    with open(GL3_PKL, "rb") as f:
        return pickle.load(f)["rows"]


def by_label_gl2() -> dict[str, dict]:
    return {r["label"]: r for r in load_gl2()}


def _zeros_of(rec: dict | None):
    if rec is None:
        return np.zeros(0, dtype=np.float64)
    z = rec.get("zeros")
    if z is None:
        return np.zeros(0, dtype=np.float64)
    return np.asarray(z, dtype=np.float64)


def load_zeros(label: str):
    """γ > 0. Origin URL, quorum chi3/zeta, or Maass label.

    Character/Dirichlet/3/2 is χ₃. Bare 3.2 is the Maass short label.
    """
    from maass_table1 import is_maass_name, resolve

    s = label.strip()
    if s.startswith("Character/Dirichlet/") or s.startswith("ModularForm/"):
        return _zeros_of(by_origin().get(s))
    if s == "zeta" or s.startswith("chi") or s.startswith("chim"):
        rec = by_chi().get(s)
        if rec is not None:
            return _zeros_of(rec)
        path = os.path.join(HERE, f"zeros_{s}_weyl.pkl")
        if os.path.exists(path):
            return np.array(
                sorted(float(x) for x in pickle.load(open(path, "rb"))),
                dtype=np.float64,
            )
        return np.zeros(0, dtype=np.float64)
    rec = by_label_gl2()[resolve(s) if is_maass_name(s) else s]
    return _zeros_of(rec)


def load_lfunc(label: str) -> dict:
    """L-search columns. Origin URL, chi3/zeta, or Maass label."""
    from maass_table1 import resolve

    s = label.strip()
    if s.startswith("Character/Dirichlet/") or s.startswith("ModularForm/"):
        rec = by_origin().get(s)
        if rec is None:
            raise KeyError(s)
        if rec.get("lfunc") is not None:
            return rec["lfunc"]
        return {
            "label": rec.get("label"),
            "d": rec.get("degree"),
            "N": rec.get("N"),
            "chi": rec.get("central_character") or rec.get("chi"),
            "mu": rec.get("mu"),
            "z1": rec.get("z1"),
            "origin": rec.get("origin"),
            "self_dual": rec.get("self_dual"),
            "prim": rec.get("primitive"),
            "stored_in_lmfdb": True,
        }
    if s == "zeta" or s.startswith("chi") or s.startswith("chim"):
        return by_chi()[s]["lfunc"]
    rec = by_label_gl2()[resolve(s)]
    lf = rec.get("lfunc")
    if lf is None:
        return lfunc_from_rigor(rec, rec.get("zeros"))
    return lf


def _chi_zeros(name: str) -> np.ndarray:
    for suffix in ("_weyl.pkl", "_150.pkl", ".pkl"):
        path = os.path.join(HERE, f"zeros_{name}{suffix}")
        if os.path.exists(path) and os.path.getsize(path) > 64:
            raw = pickle.load(open(path, "rb"))
            try:
                z = np.array(sorted(float(x) for x in raw), dtype=np.float64)
            except TypeError:
                continue
            if z.size:
                return z
    return np.zeros(0, dtype=np.float64)


def _match_real_primitive(q: int, even: bool):
    for r in load_dirichlet():
        if (
            r["modulus"] == q
            and r["is_primitive"]
            and r["is_real"]
            and bool(r["is_even"]) == even
        ):
            return r
    return None


def _quorum_char_map() -> dict:
    """Union of scan_s / harvest_weyl / ql_class_mu3 Kronecker names, plus zeta."""
    import harvest_weyl
    import ql_class_mu3
    import scan_s

    names = {}
    for src in (scan_s.CHARS, harvest_weyl.CHARS, ql_class_mu3.MORE):
        names.update(src)
    names["zeta"] = dict(q=1, d=1, a=0)
    return names


def build_quorum_chi() -> list[dict]:
    """Every quorum character, keyed by LMFDB Origin Character/Dirichlet/q/n."""
    names = _quorum_char_map()
    dir_l = {r["url"]: r for r in load_lfunc_dirichlet()}
    rows = []
    for name, cf in sorted(names.items(), key=lambda kv: (kv[1]["q"], kv[0])):
        q, d, a = int(cf["q"]), int(cf["d"]), int(cf["a"])
        even = a == 0
        zeros = _chi_zeros(name)
        zeros_source = "weyl-harvest" if zeros.size else None
        orbit = None if name == "zeta" else _match_real_primitive(q, even)
        conrey = None
        url = None
        stored = None
        if name == "zeta":
            conrey = "1.1"
            url = "Character/Dirichlet/1/1"
            stored = dir_l.get(url)
        elif orbit is not None:
            n_conrey = int(orbit["first"])
            conrey = f"{q}.{n_conrey}"
            url = f"Character/Dirichlet/{q}/{n_conrey}"
            stored = dir_l.get(url)
            if stored is None and orbit.get("last") is not None:
                n2 = int(orbit["last"])
                url2 = f"Character/Dirichlet/{q}/{n2}"
                stored = dir_l.get(url2)
                if stored is not None:
                    url = url2
                    conrey = f"{q}.{n2}"
        if zeros.size == 0 and stored is not None:
            sz = stored.get("zeros")
            if sz is not None and getattr(sz, "size", 0):
                zeros = np.asarray(sz, dtype=np.float64)
                zeros_source = "lmfdb-dir-lfunc"
        mu = [(0.0, 0.0)] if even else [(1.0, 0.0)]
        Ncond = int(orbit["conductor"]) if orbit else q
        A = analytic_conductor_gammaR(Ncond, mu)
        z1 = float(zeros[0]) if zeros.size else None
        if z1 is None and stored is not None and stored.get("z1"):
            z1 = float(stored["z1"])
        lf = {
            "label": None if stored is None else stored.get("label"),
            "alpha": A,
            "A": A,
            "d": 1,
            "N": Ncond,
            "chi": conrey,
            "mu": mu,
            "nu": [],
            "w": 0,
            "prim": True,
            "arith": True,
            "rational": True,
            "self_dual": True,
            "arg_eps": 0.0,
            "r": 0 if z1 is not None else None,
            "z1": z1,
            "origin": url,
            "stored_in_lmfdb": stored is not None,
            "conjugate": None if stored is None else stored.get("conjugate"),
            "source": (
                "quorum chi + LMFDB DIR" if stored is not None else "quorum chi reconstructed"
            ),
        }
        rows.append(
            {
                "name": name,
                "origin": url,
                "q": q,
                "d_kronecker": d,
                "parity": a,
                "even": even,
                "conrey": conrey,
                "orbit": None if orbit is None else orbit["label"],
                "zeros": zeros,
                "zeros_source": zeros_source,
                "lfunc": lf,
            }
        )
    return rows


def write_quorum_chi() -> list[dict]:
    global _CHI, _ORIGIN
    rows = build_quorum_chi()
    blob = {
        "cite": CITE,
        "kind": "quorum_dirichlet_chi",
        "n": len(rows),
        "rows": rows,
        "lfunc_columns": ",".join(LFUNC_COLUMNS),
    }
    with open(CHI_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    _CHI = rows
    _ORIGIN = None
    n_st = sum(1 for r in rows if r["lfunc"]["stored_in_lmfdb"])
    print(
        f"wrote {CHI_PKL} n={len(rows)} stored={n_st} "
        f"{os.path.getsize(CHI_PKL)} bytes",
        flush=True,
    )
    for r in rows:
        z1 = r["lfunc"]["z1"]
        z1s = f"{z1:.6f}" if z1 is not None else "-"
        print(
            f"  {r['name']:8s} Origin={r['origin']} χ={r['conrey']} "
            f"z1={z1s} src={r['zeros_source']}",
            flush=True,
        )
    return rows


_CHI = None
_ORIGIN = None


def load_chi_rows() -> list[dict]:
    global _CHI
    if _CHI is None:
        if not os.path.exists(CHI_PKL):
            _CHI = write_quorum_chi()
        else:
            _CHI = pickle.load(open(CHI_PKL, "rb"))["rows"]
    return _CHI


def by_chi() -> dict[str, dict]:
    """Lab name (chi3, zeta) → row. Origin lookup is by_origin / load_chi."""
    return {r["name"]: r for r in load_chi_rows()}


def load_chi(name: str) -> dict:
    """Lab name or LMFDB Origin Character/Dirichlet/q/n."""
    s = name.strip()
    if s.startswith("Character/Dirichlet/"):
        rec = by_origin().get(s)
        if rec is None or rec.get("name") is None:
            raise KeyError(s)
        return rec
    rec = by_chi().get(s)
    if rec is None:
        raise KeyError(s)
    return rec


def by_origin() -> dict[str, dict]:
    """LMFDB Origin URL → chi / GL2 / GL3 row."""
    global _ORIGIN
    if _ORIGIN is None:
        out: dict[str, dict] = {}
        for r in load_chi_rows():
            if r.get("origin"):
                out[r["origin"]] = r
        for r in load_gl2():
            o = r.get("origin") or (r.get("lfunc") or {}).get("origin")
            if o:
                out[o] = r
        if os.path.exists(GL3_PKL):
            for r in load_gl3():
                o = r.get("origin")
                if o:
                    out[o] = r
        _ORIGIN = out
    return _ORIGIN


def write_catalog() -> None:
    """Indexed catalog: gl2 + gl3 + quorum chi, keyed by Origin."""
    gl2 = load_gl2()
    gl3 = load_gl3() if os.path.exists(GL3_PKL) else []
    chi = load_chi_rows()
    origin: dict[str, dict] = {}
    chi_ix = {r["name"]: i for i, r in enumerate(chi)}
    for i, r in enumerate(chi):
        if r.get("origin"):
            origin[r["origin"]] = {"kind": "chi", "i": i, "name": r["name"]}
            chi_ix[r["origin"]] = i
    gl2_ix = {r["label"]: i for i, r in enumerate(gl2)}
    for i, r in enumerate(gl2):
        o = r.get("origin") or (r.get("lfunc") or {}).get("origin")
        if o:
            origin[o] = {"kind": "gl2", "i": i, "label": r["label"]}
            gl2_ix[o] = i
    gl3_ix = {r["label"]: i for i, r in enumerate(gl3)}
    for i, r in enumerate(gl3):
        o = r.get("origin")
        if o:
            origin[o] = {"kind": "gl3", "i": i, "label": r.get("label")}
            gl3_ix[o] = i
    blob = {
        "cite": CITE,
        "kind": "lmfdb_catalog",
        "index": {
            "gl2": gl2_ix,
            "chi": chi_ix,
            "gl3": gl3_ix,
            "origin": origin,
        },
        "gl2": gl2,
        "chi": chi,
        "gl3": gl3,
        "lfunc_columns": ",".join(LFUNC_COLUMNS),
        "arbitrage": ARBITRAGE,
    }
    with open(CATALOG_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    print(
        f"wrote {CATALOG_PKL} gl2={len(gl2)} chi={len(chi)} gl3={len(gl3)} "
        f"origin={len(origin)} {os.path.getsize(CATALOG_PKL)} bytes",
        flush=True,
    )


def load_catalog() -> dict:
    if not os.path.exists(CATALOG_PKL):
        write_catalog()
    with open(CATALOG_PKL, "rb") as f:
        return pickle.load(f)


def load_dirichlet() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_dirichlet.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_lfunc_maass() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_lfunc_maass.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_lfunc_dirichlet() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_lfunc_dirichlet.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_lfunc_cmf() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_lfunc_cmf.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_mf_newforms() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_mf_newforms.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


_AN = None
_AN_HP_DB = None
HP_DPS = 70


def _sqlite_path() -> str:
    return os.path.join(ROOT, "data", "lmfdb_mirror.sqlite")


def load_an(label: str | None = None):
    """Rigor a_n as float64. Prefers sqlite maass_an_prec, else float32 shards."""
    global _AN
    if _AN is None:
        _AN = {}
        sqlite = _sqlite_path()
        import sqlite3

        if os.path.exists(sqlite):
            db = sqlite3.connect(sqlite)
            tables = {
                r[0]
                for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")
            }
            if "maass_an_prec" in tables:
                for lab, blob in db.execute("SELECT maass_label, f64 FROM maass_an_prec"):
                    _AN[lab] = np.frombuffer(blob, dtype=np.float64).copy()
            if not _AN and "maass_an" in tables:
                for lab, blob in db.execute("SELECT maass_label, coeffs FROM maass_an"):
                    _AN[lab] = np.frombuffer(blob, dtype=np.float32).astype(np.float64)
            db.close()
        if not _AN:
            import glob

            for path in sorted(glob.glob(os.path.join(HERE, "lmfdb_maass_an_N*.pkl"))):
                blob = pickle.load(open(path, "rb"))
                for lab, vec in blob["an"].items():
                    _AN[lab] = np.asarray(vec, dtype=np.float64)
    if label is None:
        return _AN
    return _AN[label]


def load_an_hp(label: str):
    """Rigor a_n as mpmath.mpf at 70 decimal digits (replica numeric)."""
    import sqlite3

    from maass_table1 import resolve
    from mpmath import mp, mpf

    mp.dps = HP_DPS
    lab = resolve(label)
    db = sqlite3.connect(_sqlite_path())
    row = db.execute(
        "SELECT hp FROM maass_an_prec WHERE maass_label=?", (lab,)
    ).fetchone()
    db.close()
    if not row:
        raise KeyError(f"no high-prec a_n for {lab}; run python code/maass_zeros_an.py --fetch")
    return [mpf(s) for s in row[0].split(",")]


if __name__ == "__main__":
    if "--reconcile" in sys.argv:
        reconcile_gl2()
        write_quorum_chi()
        write_catalog()
    else:
        encode()
        reconcile_gl2()
        write_quorum_chi()
        write_catalog()
