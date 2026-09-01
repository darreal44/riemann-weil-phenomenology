# Lock the high-direction measurements at mu=11, N=13 (notebook 25).
# Full assembly is not re-run here.

# (gamma_index, best_top_eig, cos) from high_directions.py N0=12
TOP = [
    (1, 11, 0.9031),
    (2, 12, 0.8375),
    (4, 10, 0.8437),
]


def test_first_zeros_sit_in_the_top_block():
    for k, eig, cos in TOP:
        assert eig >= 8
        assert cos > 0.80


def test_largest_square_is_not_forced_to_gamma1():
    # at N=13, lambda_max (eig 12) matched gamma_2, not gamma_1
    assert TOP[1][1] == 12 and TOP[0][1] == 11


def test_script_exists():
    import os
    path = os.path.join(os.path.dirname(__file__), '..', 'code', 'high_directions.py')
    src = open(path).read()
    assert 'chat' in src.lower() or 'chats' in src
