# Dimension reduction for Q

Q lives on the hat basis of [0, L], dim N+1.
The ground state does not.

## What the spectrum already said

Participation ratio of v²:

    N_eff  =  1 / ∑_k (v_k²)² ,     k̄ = ∑ k v_k².

| L | window | dim | N_eff | k̄ | keep |
|---|---|---|---|---|---|
| ζ | µ=8–16 | 9–13 | 3.1–3.4 | 0.9 | 4 hats |
| χ₅, χ₃, χ₄ | µ=16 | 9–25 | 2.13–2.14 | 0.5 | 2 hats |
| 11a1 | µ=11 | 9 | 1.91 | 0.39 | 2 hats |

Raising the hat cutoff does not raise N_eff
off ζ. The reduction is structural, not a
truncation artefact.

## Four reductions, in order of use

**1. Spectral truncation of Q.**
Keep the first r eigenvectors of Q.
On ζ, r=4 captures λ to 10⁻¹² (the rest
is decades of the same bump). Off ζ, r=2
is the whole story. This is POD of the
quadratic form: the Rayleigh quotient is
already the energy.

**2. Two physical axes.**
v_arch = ground state of the archimedean
block A, v_towers = ground state of the
prime block T. They are 81° apart. The
2×2 of Q in that plane gives the first
two signs and λ ∼ 10⁻³. It is the right
*coordinate system*, not the right
*dimension*: rungs n=2,3 still sit in
the orthogonal complement and take the
remaining decades on ζ.

**3. Constraint {ε=0}.**
ε = v₀ + √2 ∑ vₙ is evaluation at t=0.
The bump is the mid-window vector closest
to this hyperplane. Reducing onto {ε=0}
then taking the ground state of Q there
is the Dirichlet reduction. C_bump is the
cost of the leftover defect. This is not
equivalent to inverting Q on the Riesz
vector w (that is an edge spike, C_Riesz
smaller by ×2).

**4. Slepian of the desert.**
χ_{[0,γ₁]} P_{L/2} χ_{[0,γ₁]} is rank-one
at leading order and lives in the same
function class. It is the wrong 1-D
reduction for Θ_v: same class, different
function (no y e^y wall, no towers).
Use it as a comparison, not as a basis.

## What not to use here

- Random projections: N_eff is already 2–4.
- Kernel PCA on zeros: the object is Q, not
  the Gram of γ's.
- Autoencoders: four numbers, no training
  set.
- Nyström on Q entries: the matrix is 9×9
  to 25×25 and already dense and cheap.

## Practical recipe

    assemble Q at dim 9, dps 22;
    on ζ keep hats n=0..3;
    off ζ keep n=0,1;
    if the question is C or the wall,
        do not reduce below the dim where
        ε_Q has dropped (four hats on ζ);
    if the question is v₀/|v₁| or the bulk
        curvature, two hats suffice off ζ
        and four on ζ.

The 2-axis plane is for interpretation.
The 4-hat block is for numbers on ζ.
Nothing larger has paid rent at these
windows.
