# Locks for the four parallel hooks of notebook 28.
SIGNED_BOUND = 6.0e-3
UNSIGNED_BOUND = 3.6e-2
CHI3_PLATEAU = 16.94
CHI4_PLATEAU = 17.90
TWOPIE = 17.079
MATCH_MEAN = 0.8075
MATCH_MIN = 0.6458


def test_signed_arb_bound_beats_unsigned():
    assert SIGNED_BOUND < 0.5 * UNSIGNED_BOUND


def test_two_delta_clusters():
    assert abs(CHI3_PLATEAU - TWOPIE) < 0.3
    assert CHI4_PLATEAU - TWOPIE > 0.5


def test_one_to_one_min_cos():
    assert MATCH_MIN > 0.60 and MATCH_MEAN > 0.75
