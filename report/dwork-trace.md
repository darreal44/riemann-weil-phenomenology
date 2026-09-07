# Dwork’s trace formula

Not Weil’s explicit formula. Characteristic p.

Setup: X smooth (or a hypersurface) over F_q, q=p^a. Dwork lifts the
defining equation to a p-adic ring and builds an operator α (a
composition of a “Frobenius” ψ and a multiplication by an entire
function coming from a splitting function for exp) acting on a space of
p-adic power series (or overconvergent functions) B.

The trace formula is of Lefschetz type:

    #X(F_{q^k}) = q^{k dim} Tr(α^k | B) minus correction terms on faces
    (depending on the version)

Equivalently the zeta function is a ratio of Fredholm determinants

    Z(X,T) = det(1 − T α | …) / det(1 − T α | …)

Nuclear operators on p-adic Banach spaces have a Fredholm det that is
entire in T (Serre). An entire function satisfying a growth bound that
forces it to be a polynomial gives rationality of Z (Dwork 1960). That
is the first Weil conjecture, without cohomology groups of finite
dimension.

Monsky– Washnitzer rewrites Tr(α^k) as an alternating trace on de Rham
of a weak completion. Same numbers, geometric complex.

Relation to this repo: none as an identity. Q(f) pairs a test function
on R against primes and Γ. Dwork pairs Frobenius against a p-adic
function space. The shared word “trace” is Lefschetz versus Weil
explicit. Different fields, different operators.

RH over F_q is Deligne (weights), not this determinant.
