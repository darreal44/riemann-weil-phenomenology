# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Test isolation: several tests set mpmath's global precision or GL2_* environment variables; reset before each test.
import os, pytest, mpmath as mp

@pytest.fixture(autouse=True)
def _reset_global_state():
    keys = ('GL2_FIX', 'GL2_KMAX', 'GL2_LEGACY', 'GL2_NCUT', 'GL2_USE_GP',
            'RETURN_S', 'DUMP_MODE')
    saved = {k: os.environ.get(k) for k in keys}
    mp.mp.dps = 15
    yield
    mp.mp.dps = 15
    for k, v in saved.items():
        if v is None: os.environ.pop(k, None)
        else: os.environ[k] = v
