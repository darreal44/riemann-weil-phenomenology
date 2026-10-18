import pickle
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
import scan_q_gl2 as gl2
import scan_gl2 as zeros


@pytest.mark.parametrize('stdout', ['', '1 1\n2 nan\n', '1 1\n2 -2\n'])
def test_gp_rejects_incomplete_or_invalid_output(monkeypatch, stdout):
    monkeypatch.setenv('GL2_USE_GP', '1')
    monkeypatch.setattr(gl2.shutil, 'which', lambda _: 'gp')
    monkeypatch.setattr(gl2.subprocess, 'run', lambda *a, **k: SimpleNamespace(returncode=0, stdout=stdout))
    with pytest.raises(ValueError):
        gl2.ellan('11a1', 5)


@pytest.mark.parametrize('an', [{1: 1, 2: -2, 3: -1}, {1: 1, 2: -2, 3: -1, 4: float('nan'), 5: 1}])
def test_explicit_coefficients_checked_before_assembly(an):
    with pytest.raises(ValueError):
        gl2.assemble('11a1', 5, 2, 25, an=an)


def test_gp_keeps_exact_large_integer(monkeypatch):
    monkeypatch.setenv('GL2_USE_GP', '1')
    monkeypatch.setattr(gl2.shutil, 'which', lambda _: 'gp')
    monkeypatch.setattr(gl2.subprocess, 'run', lambda *a, **k: SimpleNamespace(returncode=0, stdout='1 1\n2 9007199254740993\n'))
    assert gl2.ellan('11a1', 2)[2] == 9007199254740993


@pytest.mark.parametrize('values,T', [([1., 2.], 3.), ([1., float('nan')], 1.), ([], 1.)])
def test_zero_cache_cannot_silently_underfill(monkeypatch, tmp_path, values, T):
    monkeypatch.setattr(zeros, 'HERE', str(tmp_path))
    (tmp_path / 'zeros_test_weyl.pkl').write_bytes(pickle.dumps(values))
    with pytest.raises(ValueError):
        zeros.zeros('test', T=T)


def test_zero_snapshot_reports_noncertified_status():
    z, metadata = zeros.zeros('11a1', T=100, with_metadata=True)
    assert z[-1] >= 100
    assert metadata['completeness_certified'] is False
    assert metadata['sha256'] and metadata['requested_height'] == 100


def test_coefficients_outside_window_cannot_change_the_form():
    narrow = gl2.assemble('11a1', 5, 2, 25, an=gl2.an_points('11a1', 5))[0]
    wide = gl2.assemble('11a1', 5, 2, 25, an=gl2.an_points('11a1', 10))[0]
    assert wide == narrow
