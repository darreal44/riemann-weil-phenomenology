# 2-adic mass, now (5 September 2026)

## Grid

At Λ = 16 the integrated mass at λ = 2 still climbs with the cell:
0.14, 0.26, 0.35, 0.44, 0.59 for h = 1/80 … 1/160. A quadratic
extrapolation in h lands at 1.4–1.6. A Hann taper does not flatten.
The peak width is ~ Λ^{-2} = 0.004; the smallest h used is 0.006.
The peak is not resolved. mass(λ=½) is worse.

Locked targets stay 1/√2 = 0.7071 (our twist) and (log 2)/√2 = 0.4901
(Bombieri). The grid has gone through 0.49 and has not stopped.
A finer Fmat at Λ=16 is the same Gibbs series. Do not run it.

## Analytic replacement

Connes (1999) Thm 4: the 2-adic piece is the local integral
∫'_{Q₂*} h(u^{-1}) / |1−u|_2 d*u, not a discrete τ_Λ on a real
slice. On shells:

- |u|_2 = 2 (ord −1): |1−u|_2 = 2, shell measure 1 → weight 1/2
  before the λ^{1/2} twist → 1/√2 after.
- |u|_2 = 1/2 (ord +1): |1−u|_2 = 1 → weight 1 → 1/√2 after twist.

That is the pre-registration. It does not use a cell size. The
disagreement is only the identification of our slice measure d*λ
with that d*u. Closing the mass is a change of measure on paper,
not a larger cpu.

Next: write the pairing of that local integral against the same test
functions that τ_curve uses (indicator of [0,Λ] in the additive
coordinate, pushed to λ), and read off one number. Code sketch in
`code/tau2_local.py` to follow; no server.
