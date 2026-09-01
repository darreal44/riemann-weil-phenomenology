# Quorum by mechanism (notebook §69). Q_S = Q + T_M with T_M the towers of the MISSING primes.
# Lemma (unconditional, linear algebra): for any unit v and u = P_perp(T_M v)/||.||,
#   Q_S is indefinite as soon as (v^T Q v + v^T T_M v) * (u^T Q_S u) < ||P_perp T_M v||^2
# (2x2 principal minor negative + Cauchy interlacing). v need not be an exact eigenvector.
# At mu=11: v = frozen bottom vector, eps = v^T Q v = 3.5832e-48 (certified), and
#   B1 (silence)   delta_p = v^T T_p v  : 0.058, 4.8e-4, 1.2e-9, 7.4e-17   (p=2,3,5,7)
#   B2 (coupling)  kappa_p = ||P_perp T_p v|| : 0.73, 0.77, 0.051, 6.2e-5
# All 15 proper sub-products of the voting primes {2,3,5,7} are certified indefinite by
# 2x2 certificates built on the SAME v (T_11 = 0 identically: Theta(L) = 0 at the window edge).
# Worst margin: M={7}: kappa^2 - a d = 3.8e-9 (kappa^2 = 3.8e-9, a d = 1.4e-16).
# Structure of the every-scale statement: [depth eps(mu) small] x [coupling kappa_M(mu) bounded
# below] x [silence delta_p small]  =>  quorum. Q and T_p in Arb balls (dps 90), ~160 s.
# The executed code is the notebook §69 cell; this header records the certificate protocol.
