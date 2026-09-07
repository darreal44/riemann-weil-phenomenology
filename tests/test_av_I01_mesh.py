# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# I_{[0,1]} N=4 quadratic mesh. Gap from shipped a and a_lo. Not Weil.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from av_I01_compare import g, g_p, gauss_on  # noqa: E402
from av_I01_mesh import (  # noqa: E402
    N_MESH,
    WINDOW,
    a_lo,
    g_lo,
    mesh_I01,
    mesh_points,
    q_piece,
    run,
    step_is_taken,
)
from av_I01_quad import gppp_negative_on_well  # noqa: E402
from av_I01_switch import true_I01  # noqa: E402
from av_gauss import a_integrand  # noqa: E402
from av_gpp import g_pp  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
PREREG = os.path.join(ROOT, "report", "prereg-av-I01-mesh.md")
NOTE = os.path.join(ROOT, "notes", "av-I01-mesh.md")
SRC = os.path.join(ROOT, "code", "av_I01_mesh.py")


def test_preregistration_locked():
    text = open(PREREG, encoding="utf-8").read()
    assert "Locked before the run" in text
    assert "Not Weil" in text
    assert "Not RH" in text
    assert "N=4" in text
    assert "0.047" in text


def test_driver():
    src = open(SRC, encoding="utf-8").read()
    assert "g_lo" in src and "a_lo" in src
    assert "N_MESH" in src
    assert "from scan_s import assemble" not in src
    assert step_is_taken() is False


def test_mesh_is_not_n1():
    pts = mesh_points()
    assert pts["n_mesh"] == 4
    assert len(pts["nodes"]) == 5
    assert abs(pts["nodes"][0]) < 1e-15
    assert abs(pts["nodes"][-1] - pts["ymin"]) < 1e-12
    assert gppp_negative_on_well(pts) is True
    # Each m_i is g'' at the right end, and decreases.
    for i in range(N_MESH):
        assert abs(pts["m_at"][i] - g_pp(pts["nodes"][i + 1])) < 1e-12
    assert pts["m_at"][0] > pts["m_at"][-1] > 0.0
    # First piece matches g's jet at 0, not the single-m of #83.
    y = 0.5 * pts["nodes"][1]
    assert abs(g_lo(y, pts) - q_piece(y, 0, pts)) < 1e-12
    assert abs(g_lo(y, pts) - (pts["gp0"] * y + 0.5 * pts["m_at"][0] * y * y)) < 1e-12
    # Interior node uses g, g' of the shipped g, not the previous q.
    y2 = 0.5 * (pts["nodes"][1] + pts["nodes"][2])
    expect = (
        g(pts["nodes"][1])
        + g_p(pts["nodes"][1]) * (y2 - pts["nodes"][1])
        + 0.5 * pts["m_at"][1] * (y2 - pts["nodes"][1]) ** 2
    )
    assert abs(g_lo(y2, pts) - expect) < 1e-12


def test_g_lo_lies_below_shipped_g():
    pts = mesh_points()
    ys = [k / 200.0 for k in range(1, 201)]
    for y in ys:
        assert g_lo(y, pts) <= g(y) + 1e-8, (y, g_lo(y, pts), g(y))


def test_gap_from_shipped_comparison_and_integrand():
    pts = mesh_points()
    i_true = true_I01()
    i_lo, pieces = mesh_I01(pts)
    i_true_again = gauss_on(lambda y: a_integrand(max(y, 1e-15)), 1e-15, 1.0)
    i_lo_again = 0.0
    nodes = pts["nodes"]
    i_lo_again += gauss_on(lambda y: a_lo(max(y, 1e-15), pts), 1e-15, nodes[1])
    for i in range(1, N_MESH):
        i_lo_again += gauss_on(lambda y: a_lo(y, pts), nodes[i], nodes[i + 1])
    i_lo_again += gauss_on(lambda y: a_lo(y, pts), nodes[-1], pts["ymeet"])
    i_lo_again += gauss_on(lambda y: a_lo(y, pts), pts["ymeet"], pts["yinf"])
    i_lo_again += gauss_on(lambda y: a_lo(y, pts), pts["yinf"], 1.0)
    assert abs(i_true - i_true_again) < 1e-12
    assert abs(i_lo - i_lo_again) < 1e-10
    gap = i_true - i_lo
    data = run()
    assert abs(data["I_true"] - i_true) < 1e-12
    assert abs(data["I_lo"] - i_lo) < 1e-12
    assert abs(data["gap"] - gap) < 1e-12
    assert data["closes_window"] is False
    assert data["gppp_negative"] is True
    assert gap >= WINDOW
    assert gap < 0.047
    assert data["verdict"] == "SURVIVE"
    assert data["step_taken"] is False
    assert len(pieces) == N_MESH + 3


def test_note_does_not_claim_weil_or_rh():
    text = open(NOTE, encoding="utf-8").read().replace("\n", " ")
    assert "Not RH" in text
    assert "Not Weil" in text or "not Weil" in text
    assert "SURVIVE" in text
    assert "still open" in text
    assert "LICENSE.md" in text
    assert "(∀ L)" in text or "covering" in text.lower()
