<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Two Grams after p^k

Same identity as report/Q-equals-Gram.md and
report/Qnm-is-not-Weil.md, restated after Q_window
grew prime powers.

## Identity

On an even test with supp ˆf ⊂ [−L,L],

    Q(f) = ∑_ρ f(ρ).

Prime-side writing (no γ):

    Q(f) = A_∞(f) − ∑_{n : log n ≤ L} Λ(n) χ(n) n^{−1/2} ˆf(log n)
           + pole if χ = 1.

Zero-side writing under RH: Gram G(f) = ∑_γ f(1/2+iγ).
Hence Q = G on that window  ⇔  no off-line ρ (and no pole
left). That is Weil, not a lab lemma.

## What the matrices are now

    Q_window   A_∞ (D₂, E_C, CST) minus every p^k < μ.
               Cosine or sine hats. No γ.
    Q_nm       ancestor: only the atom 2, L = log 3.
    G_h        sum of v(γ)v(γ)ᵀ from a harvest. Assumes
               the line.

p^k is in Q_window (2026-09-08). The μ=5 “death” of H was
the missing 2² atom, not an off-line zero.
ql-arch-weil: CST+Gauss matches the digamma writing on W_L.

## What they are not

Q_4^cos is not Q|W_L. Route B ×400 stayed inside V_12^cos.
Route 2 PSWF gave Q < 0 on a 4-plane that is not shown
to be type L — a different section, not Q ≠ Weil.

G_h is not Q_h. scan_s vs scan_gl2 conventions differ
by a hat factor; both λ0 > 0 is compatible with RH,
not an identification (37a1 already).

|Q−G| < λ_min(G) on a dense class would be RH. We do
not have that bound (the old |Q−Gram| programme).

## Status

Identification of *writings*: closed (p^k in, arch
checked). Identification of *matrices Q_h = G_h*:
open, and equivalent to RH on the window.
step_is_taken() unchanged. Not W_L. Not RH.
