# (log 2, log 3]: identity orbit, two logarithms, interior primes.
# Mechanism A (CC remainder) stays a measured negative; B is Thm 4.
# The step is not taken. No RH.
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from log2_log3_step import (  # noqa: E402
    HS_LOG_COEFF,
    SONIN_CUTOFF,
    finite_part_hs,
    finite_part_trace,
    identity_orbit,
    identity_orbit_slice,
    interior_primes,
    ki_n_above_one,
    log_prime,
    step_is_taken,
)

ROOT = os.path.join(os.path.dirname(__file__), "..")
NOTE = os.path.join(ROOT, "notes", "log2-log3-step.md")


def test_identity_orbit_vanishes_at_sonin_cutoff():
    assert SONIN_CUTOFF == 1.0
    assert log_prime(1.0) == 0.0
    assert identity_orbit(1.0, 1.0) == 0.0
    assert identity_orbit(7.0, 1.0) == 0.0
    assert identity_orbit_slice(1.0, 1.0) == 0.0


def test_identity_orbit_is_two_h1_log_Lam():
    assert abs(identity_orbit(1.0, math.e) - 2.0) < 1e-15
    assert abs(identity_orbit(0.5, math.e) - 1.0) < 1e-15
    assert abs(identity_orbit(1.0, math.exp(3.0)) - 6.0) < 1e-12
    # slice convention is twice Connes (both cutoffs)
    assert abs(identity_orbit_slice(1.0, math.e) - 4.0) < 1e-15
    assert abs(
        finite_part_trace(10.0, 1.0, math.e) - (10.0 - 2.0)
    ) < 1e-15


def test_two_logarithms_are_not_the_same_argument():
    # identity orbit doubles when Λ doubles; HS finite part does not
    # see Λ at all — only 1/h.
    ratio = identity_orbit(1.0, 4.0) / identity_orbit(1.0, 2.0)
    assert abs(ratio - 2.0) < 1e-12
    pf_a = finite_part_hs(3.257, 40.0)
    pf_b = finite_part_hs(3.257, 40.0)  # same 1/h, whatever R
    assert pf_a == pf_b
    # the HS coefficient is not the Λ-slope 2 (nor the slice slope 4)
    assert abs(HS_LOG_COEFF - 0.65) < 1e-15
    assert abs(HS_LOG_COEFF - 2.0) > 1.0
    assert abs(HS_LOG_COEFF - 4.0) > 1.0
    hs_src = open(
        os.path.join(ROOT, "code", "finite_part_HS.py"), encoding="utf-8"
    ).read()
    assert "C_LOG = 0.65" in hs_src


def test_interior_primes_are_empty_at_log2_and_only_two_at_log3():
    assert interior_primes(2.0) == []
    assert interior_primes(3.0) == [2]
    assert interior_primes(math.exp(math.log(2) + 0.01)) == [2]
    assert interior_primes(4.0) == [2, 3]
    assert 5 not in interior_primes(5.0)


def test_mu3_certificate_lists_only_prime_two():
    src = open(
        os.path.join(ROOT, "code", "positivite_certifiee_mu3.py"),
        encoding="utf-8",
    ).read()
    assert "primes = [2]" in src
    assert "Larb = arb(3).log()" in src


def test_KI_one_above_unity_at_log2_two_past_1_02():
    n2, ev2 = ki_n_above_one(math.log(2), omega=8e-3)
    assert n2 == 1
    assert ev2[0] > 1.04 and ev2[1] < 0.85
    n3, ev3 = ki_n_above_one(1.02, omega=8e-3)
    assert n3 >= 2
    assert ev3[1] > 1.0


def test_mechanism_A_judges_still_shipped():
    """K_I, D∘Q sign, and δ_S remain the judges of mechanism A."""
    tests = os.path.join(ROOT, "tests")
    ki = open(os.path.join(tests, "test_KI_spectrum.py"), encoding="utf-8").read()
    dq = open(os.path.join(tests, "test_semilocal_dq_sign.py"), encoding="utf-8").read()
    rem = open(os.path.join(tests, "test_semilocal_remainder.py"), encoding="utf-8").read()
    assert "test_KI_log2_one_above_unity" in ki
    assert "essentially_negative" in dq
    assert "essentially_positive_at_log3" in dq
    assert "log_divergent_at_one" in rem
    assert "spikes_at_two" in rem


def test_step_is_not_taken():
    assert step_is_taken() is False
    text = open(NOTE, encoding="utf-8").read()
    assert "not taken" in text
    assert "mechanism of another nature" in text
    assert "identity_orbit" in text
    assert "Sonin" in text
    assert "Theorem 4" in text
    assert "RH; not this note" in text
    # do not claim the Paley–Wiener step
    assert "open; not taken" in text
    assert "the step is taken" not in text.lower()
