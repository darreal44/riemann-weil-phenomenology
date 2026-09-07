# Well-count versus threshold, μ=16

Gram of in-band hats
(`dmax.gram_ells`). Cut
t against D_max.

    χ      D_max   #{ℓ>2}   #{ℓ>½}   #{ℓ>0.1}
    χ₁₃    1.19    1        2        2
    χ₈     1.77    2        2        3
    χ₅     3.08    3        4        5

#{ℓ>2} = round(D_max) on
these three windows
(`test_landau_matching`
already asserts that for
χ₁₃). #{ℓ>½} is larger
by one on χ₁₃ and χ₅.
The extra wells live in
(½, 2]: one mode, not a
band of width log N.

N=30 hats, c ∼ N, log c
≈ 3.4. A Landau–Widom
plunge of width O(log c)
*could* hold a handful
of transitional
eigenvalues; here it
holds one. That is the
whole gap between the
proved kernel lower
bound K ≥ D_max and the
observed well-count at
the conventional cut 2.

Lowering the cut to ½
picks that extra mode
up and the equality
#{ℓ>t}=round(D_max)
fails. There is no
threshold-free identity
in this table. Not RH.
