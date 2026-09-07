# Truncation error on I_{[0,1]}

Two different truncations.

**After y_min.** #82–#83 replace g by floor + t_inf + chord on
[y_min,1]. That is a shape truncation, not a series cut. The origin was
the dominant miss; this tail was already the smaller piece. A better
quadratic mesh on [0,y_min] does not automatically shrink the tail
error. To see its size one would integrate g−g_lo on [y_min,1] alone
(not tabulated as a split in the JSON).

**Gauss of A.** The true I in #79 is a 3-node table plus the shipped
integrand. Panels 16/32/64 on H already agree to 10⁻⁸ (#67). That
truncation is closed for the machine value I_true=−0.700799. The open
error is the hand majorant, not the quadrature of the true g.

Do not confuse with truncation of the cosine ONB (H_n versus Q̂) or of
the prime tail (Neumann T). Those are other remainders
(`spectral-convergence-Hn.md`, #73).
