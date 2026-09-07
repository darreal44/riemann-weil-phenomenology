# Control: the same t-space measure on χ₂₉

μ=6, N=9.

| | χ₂₉ (even, q=29) | maass1 (R=9.53) |
|---|---|---|
| γ₁ | 1.79 | 17.02 |
| G00 | 1.749 | 0.066 |
| scan_s / panel Q λ₀ | 1.744 | — |
| P00 (Λ/√n) | −0.788 | −0.886 |
| needed arch = G+P | 0.960 | −0.821 |
| digamma ∫ W ĥ dt/π | 1.841 | 0.800 |
| panel arch | ≈0.96 | 0.824 |

On χ₂₉ the *panel* of `scan_s` matches G00
to 0.3 %. The t-space digamma integral
does not (off by 0.88). So that integral
is the wrong measure even where we
already have a calibrated Q.

On maass1 the transplanted panel gives
arch=+0.82 against a target −0.82.
The panel at L=log 6 is an O(1)
functional of (q, L, s0). It does not
see R as a desert: χ₂₉ has γ₁≈L and
G00~O(1); maass1 has γ₁≈10 L and
G00~O(10⁻²). A kernel independent
of R cannot track that.

Conclusion: freeze prime-side Q for
Maass. The Gram path (`scan_gl2`) is
the only paired window we have for
these forms. Next useful work is not
another s0.
