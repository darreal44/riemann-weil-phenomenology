# tau2_local.py — file note

102 lines. No grid.
Connes (1999) Thm 4
on 2-adic shells.
Judge: `python code/tau2_local.py`.

## Functions

    lambda_module(n)     |u|_2 = 2^{-n}
    abs_1_minus_u(n)     |1−u|_2 on 2^n Z₂*
                         None on units (n=0)
    raw_weight(n)        1/|1−u|_2 ; 0 on units
                         n=−1 → 1/2, n=+1 → 1
    twisted_module(n)    raw · √|u|_2
                         n=±1 → 1/√2
    twisted_inverse(n)   raw · √|u^{-1}|_2
                         n=+1 → √2
    mass_at_two(conv)    "module" → 1/√2
                         "inverse" → √2
    bombieri()           (log 2)/√2
    lebesgue_jacobian_at_two()  2/√2 = √2
    twisted_mass(p)      p^{-1/2} (any p)
    shell_weight(n)      (raw, module-twist)
                         used by tau2_pairing

## What it does not contain

h_Λ or ⟨τ₂,h_Λ⟩ —
that is `tau2_pairing.py`.
Fmat, τ(λ), w₂ —
`trace_formula.py`,
`trace_dist.py`,
`weights_2adic.py`,
`peak_2adic.py`.
κ — `kappa_block2.py`.
Sub-shell Fourier —
`subshells.py`,
`subshell_op.py`.

## Where it was cited
but not listed

`notes/2adic-shells.md`
proves the lemmas and
names the functions.
No file-level index
existed before this
note. Pairing run:
`report/tau2-pairing-run.md`.
Convention fight:
`report/connes-pairing.md`,
`report/dstar-identification.md`.
