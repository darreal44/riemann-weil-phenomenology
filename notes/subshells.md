<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# subshells.py / subshell_op.py

Closed form of F as
a sum of shells.

    F_from_shells(hat, xs)
    shell_term(hat, xs, n)
      n≥0 : +½ ĝ(2^n ρ)
      n=−1: −½ ĝ(ρ/2)

subshell_op.py is
the same split as
a matrix (discretized
F^{(n)}). Unitarity:
notes/semilocal-step.
Construction lemma:
notes/2adic-shells.md §3.
report/subshell-ops.md.
