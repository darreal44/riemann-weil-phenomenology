# Discrete Landau: kernel count and π²

`notes/discrete-landau.tex`. D_max and ker≥ from `code/dmax.py`.
ell from `report/edge-value-scan.jsonl` (last-wins).

The evaluation map on hats of frequency < ω has
kernel dimension ≥ n(ω) − N_Γ(ω), any nodes.
π² D_max is the one-set Slepian bound on D_max Nyquist
cells. 11 D_max is the measured mean rung.

| window | D_max | ker≥ | ell | ell/D | π² D | 11 D | (ell − π² D)/D |
|---|---|---|---|---|---|---|---|
| zeta:11 | 9.892 | 11 | 106.99 | 10.82 | 97.63 | 108.81 | +0.95 |
| zeta:16 | 15.000 | 16 | 139.71 | 9.31 | 148.04 | 165.00 | −0.56 |
| chi3:16 | 4.958 | 6 | 55.58 | 11.21 | 48.93 | 54.54 | +1.34 |
| chi3:38 | 12.325 | 14 | 139.58 | 11.32 | 121.64 | 135.57 | +1.46 |
| chi4:16 | 3.514 | 5 | 39.68 | 11.29 | 34.68 | 38.66 | +1.42 |
| chi4:38 | 9.158 | 11 | 106.81 | 11.66 | 90.38 | 100.73 | +1.80 |
| chi5:16 | 3.075 | 5 | 33.84 | 11.00 | 30.35 | 33.83 | +1.14 |
| chi5:38 | 7.577 | 9 | 88.30 | 11.65 | 74.78 | 83.34 | +1.79 |
| chi8:16 | 1.769 | 3 | 19.84 | 11.22 | 17.46 | 19.45 | +1.35 |
| chi13:16 | 1.191 | 3 | 10.87 | 9.13 | 11.76 | 13.10 | −0.74 |
| chi29:38 | 1.078 | 3 | 11.87 | 11.02 | 10.64 | 11.86 | +1.15 |
| chi31:38 | 0.896 | 2 | 8.49 | 9.47 | 8.84 | 9.85 | −0.40 |

zeta:16 is sub-Nyquist at the edge (D_max grows with N, ell saturates).
chi13 / chi31 have D_max ≈ 1: one rung, not the mean.

On the resolved degree-1 windows the remainder is +1.0 to +1.8 nats
per mode (10–18% above π²). Degree 2 sits on π² (11a1: 8.7–9.4).
