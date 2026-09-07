# Gershgorin circle theorem

Every eigenvalue of a complex n×n matrix A lies in at least one disk

    D_i = { z : |z − A_ii| ≤ R_i }
    R_i = ∑_{j≠i} |A_ij|.

Proof: if Ax=λx and |x_k| is maximal, the k-th row gives (λ−A_kk) x_k =
∑_{j≠k} A_kj x_j, so
|λ−A_kk| ≤ ∑ |A_kj| |x_j|/|x_k|
≤ R_k.

On T_far the disks are centred at Q_nn≈4.2 with radii R_n = ∑_{m≠n}
|Q_nm|. Those radii diverge with the section (harmonic row sums), so the
theorem does not produce a limit disk inside (0,∞).

On B₁ each row has at most two off-diagonal entries, R_i ≤ 2M, and the
disks sit in [−2M,2M]. That recovers ‖B₁‖≤2M, already proved by the
quadratic form.

Not a new tool for Off_far.
