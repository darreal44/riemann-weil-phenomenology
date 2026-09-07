# semilocal.py

Point-midpoint matrix
of the semi-local
Fourier on the
ord₂=0 slice.

    Fg(ρ)=½[∑_{n≥0}ĝ(2^n ρ)−ĝ(ρ/2)]
    Fab = cosine transform
          of 1_{[a,b]}
    F_cell = that sum
    build(R,N) = F_ij at
          cell midpoints

Archimedean control:
semilocal=False →
Fg=ĝ. Main prints
unitarity on [0,1].
Midpoint evaluation
aliases lacunary
terms — that is why
semilocal2 exists.
