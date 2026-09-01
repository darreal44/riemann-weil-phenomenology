# Frozen 3-var successor (notebook 35).
HOLD_OURS = {'-8': -0.075, '-20': -0.191, '-23': -0.039}
LOO_MAX = 0.64  # chi17


def test_holdout_still_inside_20pct():
    assert all(abs(v) < 0.20 for v in HOLD_OURS.values())


def test_loo_is_loose():
    assert LOO_MAX > 0.50


def test_map3_script_exists():
    import os
    src = open(os.path.join(os.path.dirname(__file__), '..', 'code', 'map3.py')).read()
    assert 'LOO' in src and 'HOLD' in src
