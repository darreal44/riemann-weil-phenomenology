# ppts_of must accept p^k for every p, not a hardcoded list capped at 67.
# Needed for 37a1 drop-3 at μ ≫ 80 (71, 73, …). No RH.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_q_gl2 import prime_power_prime  # noqa: E402


def test_prime_powers_and_composites():
    cases = {
        2: 2,
        3: 3,
        4: 2,
        8: 2,
        9: 3,
        27: 3,
        32: 2,
        49: 7,
        71: 71,
        73: 73,
        121: 11,
        128: 2,
        243: 3,
        241: 241,
        1: None,
        6: None,
        12: None,
        15: None,
        250: None,
        100: None,
    }
    for n, exp in cases.items():
        assert prime_power_prime(n) == exp, (n, prime_power_prime(n), exp)


def test_every_prime_below_250_is_itself():
    n = 250
    sieve = [False, False] + [True] * (n - 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
        p += 1
    for q in range(2, n):
        if sieve[q]:
            assert prime_power_prime(q) == q, q
