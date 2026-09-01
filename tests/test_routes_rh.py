# Three RH routes (notebook 54). Qpr-only lambda_min at mu=11.
LAM = {5: 7.817e-15, 9: 8.908e-22, 13: 9.397e-28, 17: 3.658e-33}


def test_all_positive():
    assert all(v > 0 for v in LAM.values())


def test_ell_grows_no_positive_floor():
    ell = [__import__('math').log(1 / v) for v in LAM.values()]
    assert ell[-1] > ell[0] + 30
