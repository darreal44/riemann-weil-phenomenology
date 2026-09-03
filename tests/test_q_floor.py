C_LOG3 = 5.65e-8
LAM43 = 5.73e-8

def test_mu3_floor_nearby():
    assert abs(LAM43 / C_LOG3 - 1) < 0.05
