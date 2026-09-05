#!/usr/bin/env python3
"""⟨τ₂, h_Λ⟩ for h induced by the additive indicator 1_{[0,Λ]}.

On the slice, ϑ(λ)g(r) = λ^{-1/2} g(r/λ). For g = 1_{[0,Λ]},

    ⟨g, ϑ(λ) g⟩_{L^2(dr)}
        = λ^{-1/2} meas([0,Λ] ∩ [0, λΛ])
        = Λ λ^{-1/2} min(1, λ)
        =: h_Λ(λ).

Connes pairing on the shells, twisted weights w(λ) = λ^{0} × |1-u|_2^{-1}
already twisted in tau2_local (mass p^{-1/2} at λ = p^{±1}, here p=2):

    ⟨τ₂, h_Λ⟩ = Σ_n w_n h_Λ(2^{-n}).

    python3 code/tau2_pairing.py
"""
from __future__ import annotations

import math

def h_Lam(lam: float, Lam: float) -> float:
    if lam <= 0:
        return 0.0
    return Lam * lam ** -0.5 * min(1.0, lam)


def w_shell(n: int) -> float:
    """Twisted Connes mass on shell n, vol(Z2*)=1."""
    lam = 2.0 ** (-n)
    if n > 0:
        raw = 1.0
    elif n < 0:
        raw = 1.0 / lam
    else:
        return 0.0
    return raw * math.sqrt(lam)


def pairing(Lam: float, nmin: int = -8, nmax: int = 8) -> dict:
    terms = []
    tot = 0.0
    for n in range(nmin, nmax + 1):
        lam = 2.0 ** (-n)
        w = w_shell(n)
        h = h_Lam(lam, Lam)
        contrib = w * h
        tot += contrib
        terms.append((n, lam, w, h, contrib))
    return {"Lam": Lam, "value": tot, "terms": terms}


def main():
    print(f"{'Λ':>6} {'⟨τ2,hΛ⟩':>12} {'Λ/2':>10} {'ratio':>8}")
    for Lam in (1.0, 2.0, 4.0, 8.0, 16.0):
        p = pairing(Lam)
        print(f"{Lam:6.1f} {p['value']:12.4f} {0.5*Lam:10.4f} {p['value']/(0.5*Lam):8.4f}")
    print("\nshells at Λ=4")
    print(f"{'n':>4} {'λ':>8} {'w':>8} {'h':>10} {'w h':>10}")
    for n, lam, w, h, c in pairing(4.0)["terms"]:
        if w == 0 and abs(n) > 0:
            continue
        print(f"{n:4d} {lam:8.4f} {w:8.4f} {h:10.4f} {c:10.4f}")


if __name__ == "__main__":
    main()
