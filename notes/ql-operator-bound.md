# Bochner multiplier of Q̂_L on W_{log 3}

Preregistered (`report/prereg-ql-operator-bound.md`):
the sufficient operator bound named in
`operator-bound-WL.md`. Fourier of the cutoff
kernel, g(0)=0 kept. Not Galerkin. No N.
Not RH.

## Execution

`python code/ql_operator_bound.py`.
`report/ql-operator-bound.json`.

On W_L, θ(0)=2 and θ is the Fourier cosine
of a mass ρ≥0. The cutoff kernel of Q_L
gives, without splitting 1/y,

    Q(f) = ∫ ρ(t) m_Q(t) dt
    m_Q(t) = C_A^lo/2 + k(t) − w₂ cos(t log 2)
    C_A^lo = log(q/π) + ψ(s₀) + ∑ μ^{-2(s₀+k)}/(s₀+k)
    α_line = 2 inf_t m_Q(t)

α_line ≥ 0 would take the class (even the
larger Bochner class). The cosine family
f_ω(x)=cos(ω x) on the window is in W_L
for every ω; a negative value would kill
the class.

| χ | χ(2) | α_line | t_inf | Q_cos min | A(const) |
|---|---|---|---|---|---|
| χ₅ | −1 | **−0.418** | 0 | +0.0457 | **−0.159** |
| χ₈ | 0 | **−0.929** | 0 | +0.246 | +0.311 |
| χ₄ | 0 | **−0.575** | 0 | +0.0716 | +0.154 |
| χ₃ | −1 | **−0.205** | 3.70 | +0.0118 | **−0.134** |

Integer hats match `scan_s` diagonals at
μ=3 (S₀₀, S₁₁). Worst cosine sits between
hats (ω* ∈ (1.85, 2.75), ω₁=2π/L≈5.72).
χ₃ at the canonical t=π/log 2 already has
m_Q = −0.0612 < 0 (tail 9×10⁻⁵). χ₅/χ₈/χ₄
are negative at t=0 with series tail 10⁻¹¹⁷.

Bernstein vs Â: A(constant)<0 on χ₅ and
χ₃, so those functions are in W_L and C_*
is infinite. Same kill as `Cstar-dead.md`,
now a shipped A(constant). Young stays dead.

## Verdict: SURVIVE

The sufficient bound does not take
W_{log 3}. No cosine kills it. Sandwich

    α_line ≤ c_L^* ≤ min(Q_cos, λ_min(V_N))

on χ₅ is −0.418 ≤ c_L^* ≤ 0.0435 (ladder
N=33). Class not taken. Not RH.

Judge: `tests/test_ql_operator_bound.py`.

## Status

| Claim | Status |
|---|---|
| Bochner α_line ≥ 0 (takes W_L) | **false** (this note) |
| some windowed cosine has Q≤0 | **false** |
| C_* finite for χ(2)=−1 | **false** (A(const)<0) |
| Galerkin takes the class | false (`pw-log3.md`) |
| c_L^* ≥ 0 on W_{log 3} | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
