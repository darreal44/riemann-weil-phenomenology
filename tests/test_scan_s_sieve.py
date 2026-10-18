# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Regression: scan_s sieve must include primes 37+ (accidental quorum at mu=38).
# Usage: python3 -m pytest tests/test_scan_s_sieve.py -q
import os, sys, inspect
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))
import scan_s


def test_sieve_contains_window_38_primes():
    # Numerical checks replace the old assertion that prime literals occur in
    # the source. A generated sieve has no such literals.
    from test_review_fixes import test_dirichlet_constant_entry_matches_independent_quadrature
    from pytest import MonkeyPatch
    for mu in (38, 74):
        with MonkeyPatch.context() as patch:
            test_dirichlet_constant_entry_matches_independent_quadrature(mu, patch)


def test_assemble_sorts_eigenvalues():
    src = inspect.getsource(scan_s.assemble)
    assert 'sorted' in src
