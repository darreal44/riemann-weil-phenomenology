# Residue sum is not the other proof

∫_{[0,L]} a, close a
stadium of height r
around the segment.

**r < π.** No pole
inside. Residue
theorem:

    ∮_stadium a = 0
    ⇒  ∫_{[0,L]} a = −∫_{caps+sides}

That identity is
real. It is not a
sum of residues
(there are none).
It rewrites the
integral as an
integral on the
stadium, where one
already bounds |a|
(#52). Evaluating
the sides is the
same work as
Gauss+Cauchy, not
less.

**r > π.** Now ±πi
are inside.

    ∫_{[0,L]} a
      = 2πi (Res_πi + Res_{−πi})
        − ∫_{height π+ε}

|Res a| ~ 10^4 at
k=±1, so the
height-π+ε integral
must cancel 10^4
to leave A~O(1).
The path passes
near the poles
unless one indents,
and the next pair
±2πi sits at 2π.
Unstable as a
hand bound, and
it needs a majorant
on a contour that
is *closer* to a
pole than r=2 was.

So the “other
proof” is the
vanishing-contour
identity at r<π,
which is already
the setting of
#52/#53. Crossing
π to pick up
residues makes
the bound worse,
not better.
