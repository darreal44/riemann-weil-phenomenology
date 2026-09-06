# What µ=80 changes, and what it does not

Certified row (`edge_value`, after sieve):

    χ₃ µ=80 NB=24 dps=50
    λ₀ = 4.18×10⁻⁴⁹
    ℓ  = 111.4
    edge = 108.93
    R  = +2.47
    ℓ/edge = 1.023
    N_eff = 3.00
    τγ₁ = 17.62

## Revisited

- The “assembly wall” / 20th artefact family
  is a hardcoded prime list ending at 37.
  Struck from `le-milieu-des-premiers-v2.md`
  (§ faits, § échec, journal 219) and from
  `lemma-theta-chi3-NB28.md`.
- The edge law 86–103 % now includes this
  window (97.8 % of ℓ in the edge).
- Default µ≥60 is NB=24 dps=50, not 26.

## Not to mix

ℓ(χ₃,38)=139.6 used 66 hats.
ℓ(χ₃,80)=111.4 used 24 hats and N_eff
has only just reached 3. Saturation
ladder at this µ (scan_s):

| NB | λ₀ | ℓ | N_eff |
|---|---|---|---|
| 8 | 3.8×10⁻²³ | 51.6 | 2.66 |
| 12 | 1.1×10⁻³⁰ | 68.7 | 2.82 |
| 16 | 1.7×10⁻³⁷ | 84.5 | 2.91 |
| 20 | 2.6×10⁻⁴³ | 98.3 | 2.96 |
| 24 | 5.6×10⁻⁴⁹ | 111.1 | 3.00 |

ℓ still climbs. A slope s(χ₃) or a
comparison to τγ₁ across µ must freeze
N_eff or take NB ∝ L.

## 3-hat lemma

N_eff=3.00 means the fourth mode is
on. The raised-cosine 2-plane is no
longer the whole bottom. Lemma 2 at
3 hats is a worse proxy here than at
µ=16 (N_eff≈2.2).

## Commands left on the server

Quick marginal at NB=24 (omax=34, 10
zeros): w(γ₁)=5.57, w0=6.38, sub-Nyquist.
Not comparable to w0=10–11.5 at omax~110.
Matched-omax command (server, long, may
underflow):

    python code/marginal_weights.py --workers 1 --inner 8 --force chi3:80:72:80

Saturation check past NB=24 (dps up):

    python code/scan_s.py chi3 80 26 56
    python code/scan_s.py chi3 80 28 64
