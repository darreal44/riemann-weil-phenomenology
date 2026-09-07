<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Table 1 Maass: LMFDB labels, not lexicographic dumps

Not a take. Not Weil.

`zeros_maass{1..5}_weyl.pkl` are Booker–Then Table 1 (arXiv:1703.08863).
The Zenodo/LMFDB file order at level 1 is lexicographic:

    1.0.1.1.1, 1.0.1.10.1, 1.0.1.100.1, …

so `--nforms 3` aliased maass2/maass3 to the 10th and 100th forms
(R=19.48 and 45.95). Only maass1 was the same form on both sides.

Scanners now share `code/maass_table1.py`:

    maass1  1.0.1.1.1   R=9.5337   γ1=17.025
    maass2  1.0.1.2.1   R=12.173   γ1=5.106
    maass3  1.0.1.3.1   R=13.780   γ1=2.898  (odd, symmetry=0)
    maass4  1.0.1.4.1   R=14.359   γ1=3.765
    maass5  1.0.1.5.1   R=16.138   γ1=4.070

LMFDB encoding `N.k.a.m.d`: level, weight, Conrey character `N.a`
(two numbers), spectral index `m`, copy `d`. Prefix
`<level>.<weight>.<q.n>` is `1.0.1.1` for χ=1.1. Short box-label
`N.m` (when k=0, a=1, d=1): `1.2` → `1.0.1.2.1`, character **1.1**,
not 2.1. At level 2, `2.1` → `2.0.1.1.1`, character **2.1**. Degree 2
on the GL2 dump (the CSV had no degree column).

`scan_gl2.py 1.2` and `scan_q_maass 1.2` resolve to `1.0.1.2.1`.
LMFDB `symmetry=0` is odd (s0=3/4). CSV gitignored; scanners load
`code/lmfdb_maass_gl2.pkl` (35416 rows, levels 1–105).
All rigor `a_n` (1000 coeffs) live in `lmfdb_maass_an_N*.pkl` and in
gitignored `data/lmfdb_mirror.sqlite`. Dirichlet orbits with modulus
≤ 1000: `lmfdb_dirichlet.pkl`. Replica dumps use at most 2 connections
on indexed `type` / `url` / `Lhash` / `level` (no `ILIKE` on
`lfunc_lfunctions`). L-function zeros and conjugate orbits:
One GL2 catalog: `lmfdb_maass_gl2.pkl`. Each row has the L-search
columns (`α, A, d, N, χ, μ, ν, w, prim, arith, ℚ, self-dual,
Arg(ε), r, z1, origin`) on `rec["lfunc"]`. LMFDB does not *store*
GL2 rigor L-functions (`lfunc_search` is empty at N=1 and N=11 for
degree 2, w=0; the form page says “L-function not computed”;
completeness lists 15659 *dynamic* GL2 Maass L). Those columns are
rebuilt from `maass_rigor`. `A` is LMFDB’s analytic conductor
(checked on the GL3 CSV). Table 1 γ and `z1` come from
Booker–Then (`load_zeros("maass1")`). `11.0.1.1.1` has `a_n` and a
reconstructed L-row with no `z1`.

Origin is LMFDB’s instance name (`instance_urls[0]`). For a
Dirichlet L-function it *is* the character:
`Character/Dirichlet/{q}/{n}` (Conrey). Quorum χ (union of
`scan_s`, `harvest_weyl`, `ql_class_mu3`, plus zeta) live in
`lmfdb_quorum_chi.pkl`; the indexed catalog
`lmfdb_catalog.pkl` keys GL2 / χ / GL3 by that Origin. So
`load_lfunc("chi3")` and `load_lfunc("Character/Dirichlet/3/2")`
are the same row; χ on the L-row is Conrey `3.2`. Bare `3.2` is
the Maass short label `3.0.1.2.1` — do not use it for the
character. GL3/DIR/CMF stay in `lmfdb_lfunc_*.pkl`.
`python code/lmfdb_encode.py --reconcile`.
Every shipped `maass_an_*.json` matches the pkl on N, R, symmetry,
Fricke (`tests/test_lmfdb_zenodo.py`).

At μ=6, NB=12, all five Grams are isolated (ℓ from 35.8 down to 17.9).
Q00 of the textbook pair stays O(1) (maass1: 1.71 vs G00=0.066). Same
form, still not one kernel. Do not harvest a depth from Q.

Cite: LMFDB Collaboration 2026, `notes/lmfdb.bib`. Zenodo 15490636.
`python code/maass_table1_pair.py`
`report/maass-table1-pair.json`.
