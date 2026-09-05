# Review of `code/scan_q_gl2.py` (5 September 2026, Claude)

The script's mechanics (quadratures, prime-power filter, bad prime p | N) are sound. Its conventions are not,
and the zero Gram of 11a1 (422 zeros to T = 320, γ₁ = 6.36261 = LMFDB) is the judge.

**Three convention errors in the original.**
1. *Γ arguments.* The critical line of L(s, f) is Re s = 1, so Γ_ℝ(s)Γ_ℝ(s+1) has arguments (1+it)/2 and
   (2+it)/2: s₀ = ½ and 1. The script uses (¼, ¾), the Dirichlet panels at centre ½. Shifting everything to ½
   gives Γ_ℝ(s'+½)Γ_ℝ(s'+3/2) — again (½, 1).
2. *Prime powers.* The explicit formula needs Λ_f(pᵏ) = (αᵏ + βᵏ) log p with α+β = a_p, αβ = p (good p; αβ = 0
   for p | N). The script uses a_{pᵏ} log p. For 11a1: Λ_f(4) = 0 (script 2 log 2), Λ_f(8) = 4 log 2 (script 0),
   Λ_f(9) = −5 log 3 (script −2 log 3).
3. *Conductor constant.* N^{s/2} contributes ½ log N once; split over two panels, each carries ½ log N − log π − γ.
   The script puts log N − log π − γ per panel: an excess of log N (2.40 for 11a1) sitting on the constant
   function. **The positivity "11a1 µ=11 now positive" (λ₀ = +1.22, N_eff = 1.11, k̄ = 0.11: a nearly pure η₀
   mode) is this artefact.** Against the zero Gram, the original's (0,0) entry is 11.3× the truth
   (Frobenius error 44%).

**The corrected variant** (`GL2_FIX=1`: s₀ = (½, 1), Λ_f by power sums, ½ log N per panel, no `cut` term) matches
the zero Gram to **3.7% Frobenius**; least-squares scale factors on the archimedean and prime parts are
α = 0.997, β = 0.989 — the conventions are right to normalization. Entries for modes k ≥ 2 agree to 1–2%
((2,2) 1.025, (5,5) 0.98, (10,10) 0.995; the tail beyond 320 is ≈ 0.008–0.016).

**What remains.** A smooth, mode-dependent residual: (0,0) +0.086, (1,1) +0.148, (2,2) +0.050, (3,3) −0.048,
(5,5) −0.062 — about 5% of the low-mode entries, where two O(1) terms (archimedean −1.15, towers −1.48) cancel.
It decides the sign: corrected Q_pr has λ_min = −0.017 while the zero Gram is PSD (+5×10⁻⁶). Under GRH for 11a1
(zeros on the line far beyond 320) the Weil form is PSD, so the prime side still carries a small error, not yet
identified (not the constant — a constant shifts all diagonals equally; not the scales; not the tail).

**Consequences.** No positivity statement about GL₂ should be made from `scan_q_gl2.py` in either version. The
zero-side Gram results (`scan_gl2.py`, `gl2-gram-slopes.md`) are unaffected. The corrected variant is kept behind
`GL2_FIX=1` as the current best, with this review as its warning label; the 3.7% comparison against the zero Gram
is the test to beat. Guarded by `tests/test_gl2_conventions.py`.
