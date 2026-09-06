# Test isolation: several tests set mpmath's global precision or GL2_* environment variables; reset before each test.
import os, pytest, mpmath as mp

@pytest.fixture(autouse=True)
def _reset_global_state():
    saved = {k: os.environ.get(k) for k in ('GL2_FIX', 'GL2_KMAX', 'GL2_LEGACY')}
    mp.mp.dps = 15
    yield
    mp.mp.dps = 15
    for k, v in saved.items():
        if v is None: os.environ.pop(k, None)
        else: os.environ[k] = v
