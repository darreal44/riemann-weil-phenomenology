# What replaces Bochner

Bochner asks for a PD extension of the truncated kernel to R. Drop the
extension.

On W_L the quadratic form is the Toeplitz operator with symbol the
Fourier transform of the kernel restricted to [-L,L]. Positivity of that
operator is Q_L≥0. That is the object. A replacement is a *sufficient*
bound for this Toeplitz form, not a PD function on R.

Concrete sufficient pieces already in the lab:

    archimedean block exact or Gauss on a (finite hats). prime tail
    majorised by |χ(p)|≤1 and Neumann T (Schur). mid-band lag |θ|≤√2 by
    three coverings (#89), one L. Hilbert ‖[1/(n+m)]‖≤π on the Hankel
    remainder.

Together they are the windowed bound. They replace Bochner as a method.
They do not replace the theorem “g extends to a PD function ⇒ Q≥0 on all
of L²(R)”, which is stronger than W_L and false for the cutoff.

Name: Toeplitz-on-W_L + Schur + fold. Not Krein (no explicit measure).
Not Pólya frequency (convex decreasing tail failed as a proof). Not
Riesz–Fejér (trig polynomials on the circle are the finite hats, already
used).
