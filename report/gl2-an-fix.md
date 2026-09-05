# 11a1 a_n fix

Old A11: a16=+4, a29=+6. Hecke / LMFDB / gp: a16=−4, a29=0,
a32=+8. gp 31..38 matches Hecke exactly.

Default path is now Hecke from a_p, not A11 and not gp.
μ=38 cap=38: λ0=+0.594 (N=25). The −9.28 was the Windows
gp `ellan` path.

    python code/scan_q_gl2.py 11a1 38 24 40

Expect `n_an=38` and λ0≈+0.59. `GL2_USE_GP=1` only to
compare parsers.
