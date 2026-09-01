# Secant-convergence analysis for chi-20 (notebook 37).
SECANTS = (0.535, 0.547, 0.563, 0.591, 0.582)
SINF_BAND = (0.57, 0.62)
SHAT_3 = 0.44


def test_one_drop_smaller_than_prior_rises():
    diffs = [SECANTS[i+1]-SECANTS[i] for i in range(len(SECANTS)-1)]
    assert diffs[-1] < 0
    assert abs(diffs[-1]) < min(diffs[:-1])


def test_sinf_band_excludes_three_var():
    assert SHAT_3 < SINF_BAND[0]
    assert SINF_BAND[0] < 0.60 < SINF_BAND[1]
