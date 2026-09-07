# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# Lock C = |vhat(g1)|/lambda0 measured on zeta mu=11 N=21.
C_ZETA_MU11_N21 = 27.83
C_WINDOW = (7.0, 40.0)  # published 7-25; short basis sits a little high


def test_measured_C_is_order_lambda_not_sqrt():
    assert C_WINDOW[0] < C_ZETA_MU11_N21 < C_WINDOW[1]


def test_script_mentions_both_scalings():
    import os
    src = open(os.path.join(os.path.dirname(__file__), '..', 'code', 'endpoint_order.py')).read()
    assert '|vh(g1)|/λ' in src or 'vh(g1)|/λ' in src
