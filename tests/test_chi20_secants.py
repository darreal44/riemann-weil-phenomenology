# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# chi_-20 secants through mu=50 (notebook 23). Kill-from-above not fired.
SECANTS = {
    (16, 22): 0.534,
    (22, 32): 0.547,
    (32, 38): 0.564,
    (38, 50): 0.590,
}
PRED_4VAR = 0.57


def test_secants_monotone_rising():
    vals = [SECANTS[k] for k in sorted(SECANTS)]
    assert vals == sorted(vals)


def test_last_secant_within_20pct_of_prediction():
    last = SECANTS[(38, 50)]
    assert abs(last / PRED_4VAR - 1) < 0.20
    assert last / PRED_4VAR - 1 < 0.05  # +4% as shipped


def test_rise_is_slow():
    vals = [SECANTS[k] for k in sorted(SECANTS)]
    assert vals[-1] - vals[0] < 0.10
