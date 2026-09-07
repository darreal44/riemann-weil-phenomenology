# Error estimators

On the true integral, a Kronrod extension of a Gauss panel gives
|I_n−I_{2n+1}| as an estimator. Useless here: I_true is known.

On g_lo, the estimator that matches the proof is the leftover itself:

    E_i = leftover_i h_i² / 2 = (g''(y_i)−m_i) h_i² / 2

pointwise cap, or leftover_i h_i³ / 6 integrated against 1 on the slab
(weight ½w is an extra O(1) factor). That is computable from shipped
g_pp without a finer run. Summing E_i over the eight N=4 slabs should
recover the order of the 0.0028 gap (`local-curvature.md`).

A posteriori estimator = I_true−I_lo is available because this is one
witness with a machine I_true. It cannot be used inside the hand bound
(circular). It is only the score.

Not Weil.
