<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: Gauss-3 table, and a 3-piece bound that still misses 0.22

Preregistered (`report/prereg-av-I01-compare.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Hand objects
named in `A-v-01.md`. Not RH.

## g = 2 e^{−3y/2} − θ_v

θ_v is the six-term mix of elementary
lags θ_nm, n,m≤2. Analytic g', g''
from the differentiated table.

g(0)=0, g<0 on (0,1], g(1)=−0.223.
g'(0)=−2.962. Unique min at
y_min=0.4098, g_min=−0.529.
g''>0 on [0, y_inf), y_inf=0.7715;
g''<0 after. So g is convex, then
concave.

## Gauss-3 table (nodes ½±√(3/5)/2, ½)

| y | θ_v | a(y) | weight | contrib |
|---|---|---|---|---|
| 0.112702 | 1.96354 | −1.28621 | 5/18 | −0.35728 |
| 0.500000 | 1.45848 | −0.63296 | 8/18 | −0.28131 |
| 0.887298 | 0.81763 | −0.22345 | 5/18 | −0.06207 |

Sum **−0.700661**. True I_{[0,1]} (48-node
Gauss) −0.700799. This is origin’s
finite arithmetic check, not an
inequality.

## Two comparisons, both miss ~0.22

Chord of θ, (0,2)→(1, 0.669):
I=−0.485, **upper** bound, gap 0.215
the wrong way for Q_lo.

3-piece of g (convex ⇒ g ≥ tangent
at 0; g ≥ g_min past the min; concave
tail ⇒ g ≥ chord):
I_lo=−0.924, **lower** bound, gap 0.224.
Q_lo= CST + I_lo + I_{[1,L]}^{lo} − P
= **−0.218** < 0. Does not close the
±0.003 A-window. The tangent at 0 is
the loose piece (g'' large, ~9).

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. One-line chords and
a 3-piece tangent/floor/chord fail
by the same 0.22 in opposite
directions. A later switch at
y_sw=g_min/g'(0) misses 0.088
(`notes/av-I01-switch.md`). Gauss-3
is the arithmetic check. One v,
finite μ. Not RH.

Judge: `tests/test_av_I01_compare.py`.
