<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Zeros of 11.0.1.1.1

LMFDB API: HTTP 500.
Gram needs a file.

1. Open
   https://www.lmfdb.org/ModularForm/GL2/Q/Maass/
   N=11, R≈2.033 (label
   11.0.1.1.1).
2. Copy positive
   zeros to a text
   file (one per
   line is enough).
3.
   python code/import_maass_zeros.py 11.0.1.1.1 zeros.txt
   python code/scan_gl2.py 11.0.1.1.1 22 36 50
   python code/scan_gl2.py 11.0.1.1.1 38 66 42

PSD-honest Gram:
several γ inside
the hat band
ω_N=2π N / log μ.
With g1 unknown
until the paste,
start at μ=22. If
INDEF (desert),
raise μ, do not
blame Q.

Q at μ=8 is
already −0.78
without zeros.
Gram will not
repair that
kernel.
