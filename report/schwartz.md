# Schwartz space and W_L

S(ℝ): C^∞ functions with sup |x^k f^{(m)}(x)| < ∞ for all k,m. Fourier
transform is an automorphism of S. Even Schwartz functions are
admissible for the explicit formula in every standard writing (absolute
convergence on both sides).

W_L is smaller in one direction and larger in another:

- Smaller:
  compact support in [−L,L] ⇒ not in S unless θ≡0 (a compactly supported
  C^∞ function is Schwartz, but a PW function that is only C^0 or
  piecewise trigonometric is not).
- Larger
  as a test class for positivity: one must prove Q≥0 on all of S *and*
  on all W_L to get Weil. Usually one picks one dense class.

The cosine ONB on [−L,L] does not live in S (jumps in high derivatives
at ±L if one extends by 0). That is allowed for Guinand–Weil under the
BV / Paley–Wiener hypotheses of `admissible-tests.md`. It is not a
Schwartz basis.

Smoothing a φ_n to put it in S changes Q by an arbitrarily small amount
if Q is continuous on S in the right topology. That approximation
argument is the bridge from a negative H_n to a negative Schwartz test —
if one ever has a negative identified section. Not used yet.
