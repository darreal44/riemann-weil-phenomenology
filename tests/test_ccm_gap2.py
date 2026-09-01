# E(gaussian) is not the ground state (notebook 60).
COS_K_V = 0.00107


def test_naive_arithmetic_image_misses_ground_state():
    assert COS_K_V < 0.05
