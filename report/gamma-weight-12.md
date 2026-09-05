# Γ for weight k (Delta)

Holomorphic newform, weight k, level N:

    Λ(s) = N^{s/2} (2π)^{-s} Γ(s) L(f,s) = ε Λ(k−s).

Γ_C(s) = Γ_R(s) Γ_R(s+k−1).

scan_s encodes Γ_R(s+μ) by s0 = 1/4 + μ/2.

| k | μ | s0 |
|---|---|-----|
| 2 (11a1) | 0, 1 | 1/4, 3/4 |
| 12 (Δ) | 0, 11 | 1/4, 23/4 |

Prime weight on the 1/2-line convention:
a_n n^{-(k-1)/2} log p / √n = a_n log p / n^{k/2}.
For Δ: τ(n) log p / n^6.

Do not copy scan_q_gl2 with s0=1/4+3/4. That is k=2.
`code/scan_q_delta.py` uses (1/4, 23/4) and τ(n).
