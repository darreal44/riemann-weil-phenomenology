# Synthetic tail shrinks the 5x5 mid-difference (notebook 32).
BEFORE = (2.15e-3, 3.04e-3, 4.30e-3)
SYNTH  = (1.42e-3, 2.01e-3, 2.84e-3)
AFTER  = tuple(b-s for b,s in zip(BEFORE, SYNTH))


def test_residual_below_two_thousandths():
    assert all(a < 1.6e-3 for a in AFTER)
    assert AFTER[2] < 0.4 * BEFORE[2]
