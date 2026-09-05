# Prime-side Q for GL(2)

How to find the archimedean term: L(E,s) is completed by
Γ_C(s) = 2(2π)^{-s} Γ(s) = Γ_R(s) Γ_R(s+1). Each Γ_R is one
`scan_s` panel (s0=1/4 even, s0=3/4 odd). Add both, subtract
the primes once, with weight a_n log p / n (line Re=1).

Smoke 11a1 μ=11 N=25:

| panel | λ0 |
|-------|----|
| one s0 (old) | −2.6 / −3.5 |
| Γ_R(s)+Γ_R(s+1) | **+1.217** |

Positive. λ1/λ0≈2: no deep singlet at this short window.
`python code/scan_q_gl2.py 11a1 11 24 40` then 22 / 38.
