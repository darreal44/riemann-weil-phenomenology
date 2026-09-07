# Admissible tests for Weil

The explicit formula needs θ even, real, and enough decay on θ and on ˆθ
so that both sides converge (absolutely or as a principal value).

Typical classes:

- Schwartz
  even functions on ℝ (ˆθ also Schwartz).
- Compact
  support in [−L,L] with θ of bounded variation or C¹ (Paley–Wiener: ˆθ
  entire of exponential type L).
- Li
  tests (specific moments of ξ'/ξ), which are not compactly supported.

W_L in this repo is the second class: even functions whose Fourier
transform lives in a band of width related to L, or equivalently θ
supported in [−L,L]. The cosine ONB {φ_n} is a basis of that space, not
the whole Schwartz class.

A finite combination ∑ v_n φ_n is admissible if the series for A and P
converge — they do, because support is in [−L,L] and the lags are finite
in number for Q_pk. That is why a negative H_n on the identified form
would be a genuine negative test, not an artefact of a non-admissible θ.

What is not automatically admissible: the indicator of [0,Λ] without
smoothing (discontinuities make ˆθ decay too slowly for some writings of
the zero sum). The repo uses continuous piecewise-trigonometric θ, which
is safer.
