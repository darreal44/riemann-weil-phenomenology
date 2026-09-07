<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Double-limit cutoff of truncated Hankel: N and M/N

Not Hartman. Not a take.

8i fitted \(e_\sigma \approx 0.658/\log(M/N)+0.707\) at **fixed** \(N=32\).
The intercept \(0.707\neq 0\) left open whether \(b(N)\to 0\) as \(N\to\infty\).
This sitting varies \(N\in\{16,32,64,128\}\) and \(M/N\in\{4,8,16,32\}\),
with \(M\le 2048\). Same \(H=\tfrac12/(n+m)\), \(\tau=0\) (8i: oscillation
never wins). No GL CSV.

Matched ratio, \(e_\sigma=\pi/2-\|H\|_2\):

    M/N     N=16    N=32    N=64    N=128   spread
    4       1.232   1.234   1.236   1.236   0.005
    8       1.085   1.088   1.089   1.090   0.005
    16      0.956   0.959   0.960   0.961   0.005

At fixed \(M/N\), \(e_\sigma\) is independent of \(N\) to \(0.005\). Raising
the floor \(N\) at fixed ratio does nothing. The mass that builds \(\pi/2\)
is the *span* of scales, not the infrared cut.

Per-\(N\) intercepts of \(e_\sigma = a/\log(M/N)+b(N)\):

    N      a      b      R²
    16   1.038  0.530  0.926
    32   0.966  0.572  0.945
    64   0.860  0.635  0.959
    128  0.742  0.709  0.977

\(b(N)\) *rises*, it does not go to 0. The rise is a fit artefact: larger
\(N\) has a smaller max \(M/N\) under the cap \(M=2048\). The matched-ratio
table is the statement.

No infinite Weyl sequence. Does not exhibit \(1.081\). Does not license
\(s_1\le 0.8\). Not taken. Not RH. One L.
`python code/ql_hankel_weyl_N.py`
`report/ql-hankel-weyl-N.json`.
