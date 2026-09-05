# GL2 Q levers: cap and L-cutoff

Env:

    GL2_CAP_MUL=2     # cap = μ × mul  (default 1)
    GL2_NCUT=1        # 2 = one log(1−e^{−2L}) per Γ_R
                      # 1 = once, 0 = drop both

## μ=11 and 22 (here, table a_n)

| μ | ncut | cap_mul | λ0 |
|---|------|---------|-----|
| 11 | 2 | 1 | +1.217 |
| 11 | 2 | 2 | +1.201 |
| 11 | 1 | 1 | +1.209 |
| 11 | 0 | 1 | +1.201 |
| 22 | 2 | 1 | +0.822 |
| 22 | 1 | 1 | +0.820 |
| 22 | 0 | 1 | +0.818 |

Neither lever moves λ0 by more than 3 %. The μ=38 sign
flip is not “missing n∈(μ,2μ)” and not “one extra cutoff.”

## μ=38 (needs gp)

```bash
GL2_CAP_MUL=1 GL2_NCUT=2 python code/scan_q_gl2.py 11a1 38 66 42
GL2_CAP_MUL=3 GL2_NCUT=2 python code/scan_q_gl2.py 11a1 38 66 42
GL2_CAP_MUL=1 GL2_NCUT=0 python code/scan_q_gl2.py 11a1 38 66 42
```

If all three stay near −9, the panel itself is wrong at
that L, not the two knobs.
