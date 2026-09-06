# Robustness of ell ≈ a τγ₁ + b

11 windows, prime-side −ln λ₀.

## In-sample

    ell = 6.10 τγ₁ − 19.3     rms 10.3

χ₃ µ=80 residual +23. χ₂₉ predicted
0.6 against 11.9 (intercept eats the
origin). Residuals are not noise:
wide-desert χ₃/χ₅ sit below the
line, narrow-desert χ₂₉/χ₃₁ above
once the intercept is negative.

## Jackknife

| drop | a | b | LOO pred vs ell |
|---|---|---|---|
| χ₅ 16 | 6.10 | −18.3 | 38 vs 27 |
| χ₃ 16 | 6.24 | −19.2 | 50 vs 35 |
| χ₃ 80 | **4.53** | **−8.4** | **72 vs 111** |
| χ₂₉ 38 | 6.53 | −24.7 | −3 vs 12 |
| others | 6.05–6.46 | −18 to −21 | |

a = 6.06 ± 0.51, except the χ₃-80
drop, which moves a by 1.5. LOO rms
= 15.1, worse than in-sample 10.3.
The line is not stable.

## Subsamples

    drop χ₃-80     a=4.53  b=−8.4   rms 5.1   pred 80 = 72 (true 111)
    ell < 50       a=3.99  b=−5.8   rms 3.7
    no intercept   a=4.40           rms 13.2
    no intercept, ell<50
                   a=3.32           rms 4.3

The slope halves when the one deep
window is removed. a is not a
universal C₀.

## ell / τγ₁

2.29 (χ₃₁) … 4.05 (χ₅ µ=38) … 6.31
(χ₃ µ=80). Mean 3.60, std 1.12.
Not a constant.

## T_cut → m>2ν

hats=6,8,12,20 changes the list of
“long” gaps and moves (a, c_m) from
(6.3, 10) to (4.1, 12). The second
term is a T_cut artefact.

## Verdict

The model ell = a τγ₁ + b is a
correlation (in-sample r is visible)
and not a robust law. Three failures:

1. one leverage point (χ₃ µ=80,
   N_eff=3);
2. negative intercept, so small
   deserts are mis-signed;
3. the dimensionless ratio
   ell/(τγ₁) spans a factor three.

Use τγ₁ as the *leading scale*, not
as a fitted C₀. Lemma 2 remains
c_L ≥ C exp(−C₀ τγ₁) with C₀ of
order one — an inequality, not this
regression.
