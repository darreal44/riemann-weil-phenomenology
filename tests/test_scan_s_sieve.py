# Regression: scan_s sieve must include primes 37+ (accidental quorum at mu=38).
# Usage: python3 -m pytest tests/test_scan_s_sieve.py -q
import os, sys, inspect
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))
import scan_s


def test_sieve_contains_window_38_primes():
    src = inspect.getsource(scan_s.assemble)
    for p in (29, 31, 37):
        assert str(p) in src, f'sieve missing {p} — accidental quorum'


def test_assemble_sorts_eigenvalues():
    src = inspect.getsource(scan_s.assemble)
    assert 'sorted' in src
