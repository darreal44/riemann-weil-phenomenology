# Euclidean alignment is not Q-alignment (notebook 62).
RAY_RATIO = 5.3e17
KHAT_G1 = 4.66e-4
VHAT_G1 = 1.07e-19


def test_rayleigh_not_near_lambda_min():
    assert RAY_RATIO > 1e10


def test_khat_not_a_quasi_kernel():
    assert KHAT_G1 / VHAT_G1 > 1e12
