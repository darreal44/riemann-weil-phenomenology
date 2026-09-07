# Certificates on W_{log 3}

What a “take” is: a lower bound on λ_min(Q̂_L) that is positive, in the
cosine ONB, T infinite, not a finite Galerkin of W_L.

    χ    bound     value    h    PR
    χ₈   β Schur   +0.055   2    #58
    χ₄   β Schur   +0.004   20   #60
    χ₅   S_lo Neu  +0.029   2    #61
    χ₃   S_lo Neu  +0.007   4    #63
    χ₇   S_lo Neu  +0.276   2    #64
    χ₁₇  S_lo Neu  +0.649   2    #65

#59 is not a take: ‖Θ‖≤1, used inside the others.

All six are machine bounds (Gauss + linear algebra + Hilbert π). They
are not hand proofs and not independent of the scripts `ql_schur_*`.
Judges exist as pytest.

They do not stack to (∀χ) or (∀L). The rest of `scan_s` (13 χ) also take
at μ=3 (`notes/ql-class-mu3.md`). Still a finite list. They do stack to:
every (s₀,χ(2)) cell has a positive bound for one q. That is the
content.
