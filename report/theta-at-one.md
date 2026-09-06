# θ_v and θ_v' at y=1

L = 4 ln 2,  ω = 2π/L = π/(2 ln 2)
≈ 2.26618 (129.84°).

    sin ω  =  0.767808
    cos ω  = −0.640680
    sin 2ω = −0.983839
    cos 2ω = −0.179058
    (L−1)/L = 0.639326

## The six kernels at y=1

    θ₀₀ = 2(L−1)/L           =  1.27865
    θ₀₁ = −√2 sinω / π       = −0.34563
    θ₀₂ = −sin(2ω)/(√2 π)    =  0.22144
    θ₁₁ = 2(u cosω − sinω/(2π))
                             = −1.06361
    θ₁₂ = 2(sinω − 2 sin2ω)/(3π)
                             =  0.58049
    θ₂₂ = 2(u cos2ω − sin2ω/(4π))
                             = −0.07237

u = (L−1)/L. All elementary.

## The witness

    θ_v(1) = ∑ v_n v_m θ_nm(1)
           = 0.669132
    g(1)   = 2 e^{−3/2} − θ_v(1)
           = −0.222872

    θ_v'(1) = −1.220350
    g'(1)   = −3 e^{−3/2} − θ_v'(1)
            =  0.550959

θ_v' is the same table
differentiated (cosines
in place of sines,
plus the −2/L from θ₀₀).
These two numbers are
the last inputs to the
endpoint majorant of
|a''| (`app-endpoints.md`).

No simplification of ω
to a quadrantal angle:
π/(2 ln 2) is transcendental
and not a known multiple
of π. The four values
sinω, cosω, sin2ω, cos2ω
are the whole table of
logs one still needs,
together with e^{3/2} and
ln 2.
