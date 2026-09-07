# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Three coverings of #72. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from ql_theta_overlap import (  # noqa: E402
    L5,
    Y_TAKE,
    covering_covers_integrand,
    covering_x,
    f_from_h,
    h_constant,
    in_strict_band,
    inner_T,
    interval_len,
    majorant_of_h,
    pair_inners,
    partition,
    partition_covers_half,
    run,
    step_is_taken,
    theta_of_h,
)
from ql_schur_tail import theta_hat  # noqa: E402
from ql_theta_sqrt2 import SQRT2, mass_majorant  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-ql-theta-overlap.md")
NOTE = os.path.join(ROOT, "notes", "ql-theta-overlap.md")
SRC = os.path.join(ROOT, "code", "ql_theta_overlap.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "three covering" in text or "AC" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "covering_x" in src and "partition" in src
    assert "AC_plus" in src and "AM2" in src and "M1" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_take_point_is_in_strict_band():
    assert in_strict_band(Y_TAKE, L5)
    assert 1.0 / 3.0 < Y_TAKE / L5 < 0.5


def test_partition_and_covering_on_grid():
    L = L5
    for t in (1.0 / 3.0, 0.4, Y_TAKE / L, 0.48):
        y = t * L
        assert partition_covers_half(y, L)
        assert covering_covers_integrand(y, L)
        tot = sum(interval_len(covering_x(y, L)[k]) for k in covering_x(y, L))
        assert abs(tot - (L - y)) < 1e-12


def test_three_pairs_sum_to_inner_and_cs():
    L, y = L5, Y_TAKE
    h = h_constant(L)
    f = f_from_h(h, L)
    I = inner_T(f, y, L)
    pairs = pair_inners(f, y, L)
    assert abs(sum(pairs.values()) - I) < 1e-9
    th = theta_of_h(h, y, L)
    assert abs(th - theta_hat(0, 0, y, L)) < 1e-9
    assert th <= majorant_of_h(h, y, L) + 1e-9
    assert th <= SQRT2 + 1e-12


def test_mass_majorant_is_the_shipped_simplex():
    assert abs(mass_majorant(0.5, 0.25, 0.0, 0.25) - SQRT2) < 1e-15
    p = partition(Y_TAKE, L5)
    assert p["A"][1] <= p["M1"][0] + 1e-12 or interval_len(p["M1"]) == 0.0
    assert p["M2"][0] >= p["M1"][1] - 1e-12
    assert p["C"][0] == p["M2"][1] or abs(p["C"][0] - Y_TAKE) < 1e-15


def test_run_survives():
    data = run()
    assert data["verdict"] == "SURVIVE"
    assert data["part_ok"] and data["cov_ok"]
    assert all(c["ok"] for c in data["checks"])
    assert data["step_taken"] is False


def test_note_does_not_claim_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "SURVIVE" in text
    assert "LICENSE.md" in text
    assert "covering lemma" in text.lower() or "(∀ L)" in text
