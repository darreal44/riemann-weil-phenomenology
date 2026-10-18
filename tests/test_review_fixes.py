"""Regressions for the numerical and replay failures reviewed on 2026-10-18."""
import copy
import json
import sys
from pathlib import Path

import mpmath as mp
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import scan_q_gl2
import scan_s
import quorum_general
import quorum_2x2
import dscan
import scan_gl2
from flint import arb


def test_public_gram_reads_published_cache_only(tmp_path, monkeypatch):
    import pickle
    import types
    path = tmp_path / 'zeros_11a1_weyl.pkl'
    path.write_bytes(pickle.dumps([2.0, 1.0]))
    monkeypatch.setattr(scan_gl2, 'HERE', str(tmp_path))
    private = types.SimpleNamespace(load_zeros=lambda name: __import__('numpy').array([99.0]), zeros_at=lambda *a, **k: None)
    monkeypatch.setitem(sys.modules, 'tools', private)
    assert scan_gl2.zeros('11a1').tolist() == [1.0, 2.0]


def test_public_gram_precision_requests_belong_to_pgc():
    with pytest.raises(ValueError, match='pre-compute-gamma'):
        scan_gl2.zeros('11a1', prec=1e-20)


def test_dscan_reads_frozen_cache_independently_of_cwd(tmp_path, monkeypatch):
    import pickle
    cache = tmp_path / 'code'
    cache.mkdir()
    path = cache / 'zeros_chi3.pkl'
    path.write_bytes(pickle.dumps([8.039737155681467]))
    monkeypatch.setattr(dscan, 'BASE', str(cache))
    monkeypatch.chdir(tmp_path)
    before = path.read_bytes()
    assert hasattr(dscan, 'load_zeros'), 'public dscan must read frozen caches, not harvest'
    assert dscan.load_zeros('chi3') == [8.039737155681467]
    assert path.read_bytes() == before


def test_dscan_missing_cache_requires_private_precompute(tmp_path, monkeypatch):
    monkeypatch.setattr(dscan, 'BASE', str(tmp_path))
    assert hasattr(dscan, 'load_zeros'), 'public dscan must read frozen caches, not harvest'
    with pytest.raises(FileNotFoundError, match='pre-compute-gamma'):
        dscan.load_zeros('chi3')


def test_11a1_coefficients_cover_window_beyond_builtin_table():
    coefficients = scan_q_gl2.ellan("11a1", 62)
    # Independent point-count values; each prime was absent from the old table.
    assert {p: coefficients.get(p) for p in (41, 43, 47, 53, 59, 61)} == {
        41: -8, 43: -6, 47: 8, 53: -6, 59: 5, 61: 12,
    }


def test_11a1_complete_window_does_not_create_false_negative():
    lam, _ = scan_q_gl2.assemble("11a1", 62, 4, 35)
    assert 4.85e-11 < lam < 4.87e-11


@pytest.mark.parametrize("mu", [90, 98])
def test_dirichlet_constant_entry_matches_independent_quadrature(mu, monkeypatch):
    monkeypatch.setenv("RETURN_S", "1")
    matrix = scan_s.assemble("chi3", mu, 2, 45, DEG=20)[3]
    L = mp.log(mu)
    arch = (mp.log(3 / mp.pi) - mp.euler - mp.log(1 - mp.exp(-2 * L))
            + mp.quad(lambda y: (2 * mp.exp(-2*y) - 2*(1-y/L)*mp.exp(-3*y/2))
                      / (1 - mp.exp(-2*y)), [0, L]))
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    expected = arch
    for p in primes:
        n = p
        while n <= mu:
            chi = (0, 1, -1)[n % 3]
            expected -= chi * mp.log(p) / mp.sqrt(n) * 2*(1-mp.log(n)/L)
            n *= p
    assert abs(matrix[0, 0] - expected) < mp.mpf("1e-35")


def witness_data():
    return {"kind": "zeta", "mu": 3, "NB": 2, "witnesses": [
        {"S": [], "w": [float(x).hex() for x in (1, 0, 0)]},
        {"S": [2], "w": [float(x).hex() for x in (1, 0, 0)]},
    ]}


@pytest.mark.parametrize("damage", [
    "empty", "kind", "mu", "NB", "duplicate", "subset", "dimension", "nan", "inf", "zero",
])
def test_verify_rejects_invalid_frozen_witnesses(damage, tmp_path, monkeypatch):
    data = witness_data()
    if damage == "empty": data["witnesses"] = []
    elif damage in ("kind", "mu", "NB"): data[damage] = "wrong"
    elif damage == "duplicate": data["witnesses"].append(copy.deepcopy(data["witnesses"][0]))
    elif damage == "subset": data["witnesses"][1]["S"] = [3]
    elif damage == "dimension": data["witnesses"][0]["w"].pop()
    elif damage in ("nan", "inf"): data["witnesses"][0]["w"][0] = damage
    elif damage == "zero": data["witnesses"][0]["w"] = ["0x0.0p+0"] * 3
    monkeypatch.setattr(quorum_general, "BASE", str(tmp_path))
    path = tmp_path / "witnesses_zeta_mu3.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError):
        quorum_general.run(3, 2, 22, "zeta", "verify")
    assert not (tmp_path / "quorum_cert_zeta_mu3.txt").exists()


def test_verify_replays_without_writing_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(quorum_general, "BASE", str(tmp_path))
    quorum_general.run(3, 2, 22, "zeta", "freeze")
    before = {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in tmp_path.iterdir()}
    quorum_general.run(3, 2, 22, "zeta", "verify")
    after = {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in tmp_path.iterdir()}
    assert after == before


def test_verify_fails_when_witness_does_not_prove_negativity(tmp_path, monkeypatch):
    monkeypatch.setattr(quorum_general, "BASE", str(tmp_path))
    (tmp_path / "witnesses_zeta_mu3.json").write_text(json.dumps(witness_data()), encoding="utf-8")
    with pytest.raises(ValueError, match="certif"):
        quorum_general.run(3, 2, 22, "zeta", "verify")


def test_2x2_rejects_positive_identity_despite_large_tower_coupling():
    # Exact rational counterexample: Q is positive definite, Q+T is I.
    Q = [[arb(1), arb(-2)], [arb(-2), arb(5)]]
    T = [[arb(0), arb(2)], [arb(2), arb(-4)]]
    assert hasattr(quorum_2x2, "compression_certificate"), "2x2 replay is missing"
    result = quorum_2x2.compression_certificate(Q, T, [arb(1), arb(0)])
    assert result["determinant"].contains(4)
    assert result["cross"].is_zero()
    assert not result["indefinite"]


def test_2x2_certifies_actual_negative_determinant():
    Q = [[arb(1), arb(0)], [arb(0), arb(1)]]
    T = [[arb(0), arb(2)], [arb(2), arb(0)]]
    assert hasattr(quorum_2x2, "compression_certificate"), "2x2 replay is missing"
    result = quorum_2x2.compression_certificate(Q, T, [arb(1), arb(0)])
    assert result["determinant"].contains(-12)
    assert result["indefinite"]


def test_2x2_cannot_certify_an_interval_containing_positive_matrices():
    Q = [[arb(1), arb(0)], [arb(0), arb(1)]]
    T = [[arb(0), arb(1, 1)], [arb(1, 1), arb(0)]]
    assert hasattr(quorum_2x2, "compression_certificate"), "2x2 replay is missing"
    assert not quorum_2x2.compression_certificate(Q, T, [arb(1), arb(0)])["indefinite"]
