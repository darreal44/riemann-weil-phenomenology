<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# scan_q_maass_mp.py

Does not speed up
one assemble
(mpmath on one
matrix). Maps
(name, μ) onto
processes.

    python code/scan_q_maass_mp.py maass1 22,38 36 40 --workers 2
    python code/scan_q_maass_mp.py maass1,maass3 22,38 36 40 --workers 8

Server: 8 workers
is enough (4 jobs
for two forms ×
two μ). 16 does
not help a 4-job
grid.

Smoke at μ=6–16
already INDEF.
This grid is the
optional “is the
kernel born?”
test, not a
campaign.
