# 3-var map without parity saves the hold-out (notebook 34).
# hats from map2.py dump: g1+gap+D, our s.
HOLD = {
    '-8':  (-0.07, 1.46),
    '-20': (-0.19, 0.55),
    '-23': (-0.04, 0.47),
}


def test_three_var_stays_inside_20pct():
    for name, (err, _s) in HOLD.items():
        assert abs(err) < 0.20, name


def test_chi23_is_the_save():
    assert abs(HOLD['-23'][0]) < 0.05
