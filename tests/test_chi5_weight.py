# chi5 silence / (s_inf w); notebook 90-91
R11, R16, R22 = 0.25, 0.235, 0.215
R30_INTERIOR = (0.199, 0.197, 0.196, 0.198)  # p=11,13,17,19 at mu=30
TARGET = 0.19


def test_ratio_falls_toward_target():
    assert R11 > R16 > R22 > TARGET


def test_mu30_interior_hits_019():
    assert all(abs(r - TARGET) < 0.012 for r in R30_INTERIOR)
    assert abs(sum(R30_INTERIOR)/4 - TARGET) < 0.01

C22, C30 = 0.00420, 0.00255
RMS_GAUSS22, RMS_LIN22 = 0.13, 0.48


def test_chi5_kappa_gaussian_beats_linear():
    assert RMS_GAUSS22 < RMS_LIN22 / 2


def test_chi5_c_falls_with_mu():
    assert C30 < C22

C3_22, C3_30 = 0.00646, 0.00381

def test_chi3_c_also_falls():
    assert C3_30 < C3_22

N_INDEF_CHI5_30 = 9
N_INDEF_CHI3_30 = 9

def test_single_prime_2x2_all_yes():
    assert N_INDEF_CHI5_30 == 9 and N_INDEF_CHI3_30 == 9
