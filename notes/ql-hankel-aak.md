<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Finite AAK of the Hilbert–Hankel tail

`python code/ql_hankel_aak.py`

The tail piece bounded by π in `ql_schur_tail.py` is
the Hankel matrix 1/(n+m) on n,m ≥ h.
AAK on a *section* is the SVD of that finite matrix.
Not the infinite operator, not a take of W_L, not atoms.

Prediction. σ_max < π, increasing in N, decreasing in h.
Replacing π by σ_max(128) saves O(0.1) on the ½π term.
t_atoms at μ=5.5 is 1.76 (#76). AAK does not cancel that.

Not RH. Not (∀ L).
