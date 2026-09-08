# The χ₃ sliver was the 2-plane

Same majorant as `ql_schur_neumann` (Neumann on T_near +
s1_off_q_upper on the far tail). Only HEAD changes.

χ₃, N_NEAR=32, M_C=48:

    HEAD   λmin(H)   s_diag    S_lo     ρ
       2   0.01850   0.00756  -0.00818  0.584
       3   0.01264   0.00940  +0.00418  0.563
       4   0.01123   0.00951  +0.00707  0.560
       8   0.00998   0.00967  +0.00923  0.548
      12   0.00981   0.00969  +0.00950  0.541

The sign flip is HEAD=2 → 3: hat n=2 leaves T and enters H.
HEAD=4…12 adds ~0.005 then saturates. Courant: λmin(H) falls.

HEAD=4, same cut, four characters all S_lo>0:

    χ₅  +0.03983
    χ₈  +0.24109
    χ₄  +0.06689
    χ₃  +0.00707

Off_far was not the obstruction. The 2-plane was.

Not a take of (∀χ) at every L. Not W_L for L>log 3.
step_is_taken() stays False: this is one window, one
majorant, one finite H. Not RH.
