# The two module-level assertion scripts of 31 August were never collected by pytest
# (pytest.ini enumerated files; they also define no test_* function). They pass when run,
# but nothing enforced that. Wrapped here so the suite actually guards them (notebook 82).
import os, subprocess, sys
import pytest
pytest.importorskip('flint', reason="Arb certificates need python-flint: pip install python-flint")
HERE = os.path.dirname(os.path.abspath(__file__))

def _run(name):
    r = subprocess.run([sys.executable, os.path.join(HERE, name)], capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, (name, r.stdout[-2000:], r.stderr[-2000:])
    return r.stdout

def test_cert_mu11_script():
    assert 'OK' in _run('test_cert_mu11.py')

def test_theta_endpoints_script():
    out = _run('test_theta_endpoints.py')
    assert 'OK' in out and 'test pole : OK' in out
