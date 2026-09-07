# Krein’s extension, as a proof

Statement (Krein,
1940s). Let φ be
continuous on
[−A,A], even.
TFAE:

    (i)  φ is PD
         on [−A,A]:
         ∫∫ φ(x−y) f(x)¯f(y) dx dy ≥ 0
         for all f
         supported
         in an
         interval
         of length
         ≤ A/2,
         delays
         |x−y|≤A.
    (ii) φ extends
         to a
         continuous
         PD function
         on ℝ.
    (iii) the
         trigonometric
         moment
         problem on
         the circle
         (or the
         line, after
         Cayley)
         with
         moments
         indexed by
         delays ≤A
         has a
         positive
         measure
         solution.

Proof idea, not
a new argument.
(i)⇒(iii): the
Toeplitz forms
with gaps ≤A are
positive; they
are the moments
ˆμ(n) or ∫ e^{itτ} dμ
for |τ|≤A.
Solvability of
that truncated
moment problem
gives μ≥0.
(iii)⇒(ii): ˆμ
is a PD
extension to ℝ.
(ii)⇒(i):
restriction of
a PD function
is PD on the
interval.

Uniqueness fails
in general
(indeterminate
moment problem).
Any one
extension
suffices for
Bochner on ℝ.

On W_L: A=L=
log 3, φ = G
restricted to
[−L,L] (continuous
part + the atom
at log 2, which
is a jump of
the primitive,
still a
distribution of
order 0). (i) is
exactly
Q̂_L ≥ 0, because
Q(f) is that
double integral
against G for
f∈W_L. So Krein
says:

    Q̂_L ≥ 0
      ⇔
    G|_{[-L,L]}
    admits a PD
    extension to ℝ.

That is a
rewriting of the
class step, not
a proof of it.
A proof would be
an explicit μ
(or an explicit
convex Pólya
tail plus a
handle on the
atom) that
matches G on
[−L,L].

The cutoff
extension is the
one #57 tested
and rejected as
PD. Krein
guarantees
nothing about
that particular
extension.
