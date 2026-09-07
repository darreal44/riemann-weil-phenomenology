# Convergence of the error

Observed I_true−I_lo and the leftover cap:

    stage            gap      Σ leftover h³/6
    N=1 well         0.047
    N=2              0.024
    N=4 well         0.0053
    N=4 + rise       0.00315
    + tailq          0.00279  0.00151
    N=8 well+rise    0.000405 0.000186

The score and the cap stay in a factor ~2 (the ½w). Both should drop as
O(h²) while leftover is O(1), then O(h³) once leftover=O(h). N=8 is the
test of that bend. The estimator can be rerun without claiming Weil: if
Σ cap does not fall by at least 2, the rate has not set in.

Circular use of the gap as a step size is forbidden in the hand bound
(`error-estimators.md`). The cap from g_pp is the only legal driver for
an adaptive h.

Not (∀ L).
