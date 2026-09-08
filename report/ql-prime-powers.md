# Prime powers in Q_window

Q = A − ∑_{n<μ} Λ(n) χ(n) n^{-1/2} θ(log n).
The old loop was primes only. T4 = 2² was missing.

μ=3 atoms: (2,). Still equals Q_nm.
μ=5 atoms: (2, 4, 3).

χ₃, L=log 5, primes-only vs +T4:

    HEAD  λmin(H) old    λmin(H) new   s_exact new   S_lo new
       3  −3.4e-5        +4.6e-5       +8e-6        −0.59
       4  −1.6e-4        +1.4e-5       +8e-6        −1.19

H is no longer indefinite. S_lo is worse: t_atoms includes
|w4| and ρ climbs to ~0.90. The certificate does not take
W_log5. The journal death of H4(χ₃) at μ=5 was truncation.
Not RH.
