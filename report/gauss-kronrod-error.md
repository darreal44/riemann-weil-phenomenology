# Gauss–Kronrod error estimate

For the common G7–K15 pair the embedded difference is treated as

    |∫f − K15| ≈ |G7 − K15| (sometimes scaled by a heuristic (200
    |G−K|)^{1.5} as in QUADPACK).

That estimates the error on the true ∫a, not on ∫(a−a_lo). On this
witness |G7−K15| on [0,1] would be far below WINDOW (a is smooth). It
would not have pointed at y_min.

The supporting error has a closed cap (leftover h²/2) and an exact score
(I_true−I_lo). Neither is a Kronrod difference.

#87 already used the right estimator. No G7–K15 run.
