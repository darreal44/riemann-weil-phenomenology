# Functional equation of L(s,χ)

Primitive χ mod q, parity a=0 or 1:

    Λ(s,χ) = (q/π)^{(s+a)/2} Γ((s+a)/2) L(s,χ)

    Λ(s,χ) = ε(χ) Λ(1−s, χ̄)

ε is the root number (|ε|=1; for quadratic χ, ε=1 or i^κ according to q
mod 4).

The equation pairs s with 1−s and χ with χ̄ (here χ̄=χ). It is why the
two pole ladders s₀ and 1−s₀ appear in W_∞: Γ((s+a)/2) at s=½+it is
Γ(s₀+it/2) in a normalisation, and the reflected factor is Γ((1−s+a)/2)
~ Γ(1−s₀−…).

Zeros of Λ are symmetric about Re=1/2 *as a set* without RH: if ρ is a
zero, so is 1−ρ. RH is that they all have Re=1/2 (so the partner is the
conjugate, not a new point off the line).

Completed ξ for ζ is the same pattern with q=1, a=0, and an extra s(s−1)
that cancels the poles at 0 and 1.

This repo never used ε or Λ(1−s). Q is the explicit formula for Λ'/Λ,
which already assumes the functional equation to write the archimedean
side as Γ'/Γ. Identifying W_∞ *is* using the functional equation. Not a
new campaign.
