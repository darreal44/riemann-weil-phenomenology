<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# semilocal2.py

Same operator as
semilocal.py, cell
*averages* via Si
instead of midpoint.

    avg_Fab(a,b,c,d,s)
      = (1/(d−c)) ∫_c^d F_ab(s ρ) dρ
      = [Si(2π b s x)−Si(2π a s x)]
        / (π s (d−c))

    build_exact(N):
      P1 F P1 on [0,1],
      same dyadic sum as
      Fmat (½(−s=½+∑ 2^n)).

Kills aliasing of
lacunary shells.
Fmat in
trace_formula.py is
this average, not
the midpoint.
Main: asymmetry and
∑λ² at N=200,400.
