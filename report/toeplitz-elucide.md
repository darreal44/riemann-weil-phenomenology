# Toeplitz operators, elucidated for this lab

A matrix is Toeplitz when a_{n,m} depends only on n−m. T_ψ on H² is the
model: ‖T_ψ‖=‖ψ‖_∞, spectrum = range(ψ) plus winding holes.

Off of Q is *not* that matrix. Along a fixed lag the entries oscillate
(std 0.20 on |k|=1). The closest object is a *modulated* codiagonal B₁
(weights Q_{n,n+1}), whose section norm is 0.396.

The theorems that name Toeplitz (Szegő, Widom, Hartman–Wintner) need a
symbol ψ independent of n. They do not apply to B₁ as written. A bound
on ‖B₁‖ is a weighted-shift bound: ‖B₁‖ ≤ 2 max |Q_{n,n+1}| on the
section (and that max is already the scale of s₁).

Do not import a Hardy-space course. The lab object is B₁.

Not RH.
