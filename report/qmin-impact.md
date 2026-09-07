# Impact of qmin_far

rho_far = Off_far / qmin_far.
qmin_far = min_{N <= n < M} Q_nn.

chi3 Off_far = 2.110 fixed. Need rho<0.41
hence qmin > 2.110/0.41 = 5.15.

Measured:
    N=24  qmin=3.97  rho_far=0.534
    N=32  qmin=4.19  rho_far=0.503
    N=80  Q_nn(80)=5.03  rho_far=0.415

Still 0.12 short of 5.15. S_lo still negative.
Q_nn grows slowly (~log n); rho_N climbs with N.
Not a flip by deepening N.

At N=32, Q_nn on [32,40) oscillates (T2):
chi3 trough 4.192, peak 5.007. The min, not
the mean, prices rho_far.

qmin is the diagonal of Q. Not an independent
knob. The cran remains Off_far < 0.41 qmin.

Not RH.
