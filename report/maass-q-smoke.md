# scan_q_maass smoke (maass1, R=9.53)

    python code/scan_q_maass.py maass1 6 12 25
    python code/scan_q_maass.py maass1 11 24 30
    python code/scan_q_maass.py maass1 16 24 30

    μ    cap  n_pts  λ₀      N_eff
    6     6     4   −0.87    2.42
   11    11     8   −1.27    2.72
   16    16    10   −1.39    1.14

INDEF and drifting
down. μ ≪ e^R is
not a window where
this experimental
kernel is claimed
to be PSD. Path
works (Zenodo JSON
→ assemble). Not a
certificate. Not
scan_gl2 Gram.

Larger μ (≳ R or
≳ first Maass
zero ~17) is a
server job, same
command with
mu=22 / 38.
