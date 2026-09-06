"""Dimension reduction of prime-side Q.

Usage:
    python3 code/reduce_Q.py chi5 16 24 22
    python3 code/reduce_Q.py chi3 11 8 22

Prints N_eff of the full vector and the 2-hat / 4-hat
blocks (recipe in report/lemma-theta-dimred.md).
zeta is refused here — use the 9x9 builder in the notes.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["RETURN_S"] = "1"

from scan_s import assemble
import numpy as np


def block(S, r):
    M = np.array([[float(S[i, j]) for j in range(r)] for i in range(r)], float)
    ev, U = np.linalg.eigh(M)
    v = U[:, 0]
    if v[0] < 0:
        v = -v
    p2 = v * v
    neff = 1.0 / float(np.sum(p2 * p2))
    return ev[0], v, neff


def main():
    name = sys.argv[1]
    mu = float(sys.argv[2])
    NB = int(sys.argv[3])
    dps = int(sys.argv[4])
    lam, ell, dt, S = assemble(name, mu, NB, dps)
    N = NB + 1
    print(f"full  dim={N}  lam0={lam:.4e}  ell0={ell[0]:.2f}")
    for r, tag in ((2, "2-hat"), (min(4, N), "4-hat")):
        l, v, ne = block(S, r)
        ratio = abs(v[0] / v[1]) if abs(v[1]) > 1e-18 else float("inf")
        print(
            f"{tag:6s} lam0={l:.4e}  v0/|v1|={ratio:.3f}  "
            f"N_eff={ne:.2f}  v={np.round(v, 3).tolist()}"
        )


if __name__ == "__main__":
    main()
