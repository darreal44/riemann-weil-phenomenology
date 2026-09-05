# Arb certificate: Q(mu=3) positive definite on V_31 without zeros (notebook 106). ~70 s.
import os, subprocess, sys
def test_q_mu3_certified_positive():
    r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', 'code', 'positivite_certifiee_mu3.py')], capture_output=True, text=True, timeout=900)
    assert r.returncode == 0, r.stderr[-1500:]
    assert 'CERTIFIE : Q(mu=3) definie positive' in r.stdout, r.stdout[-800:]
