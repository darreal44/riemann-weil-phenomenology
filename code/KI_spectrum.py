"""Spectrum of CC K_I vs length L. Qeps from cc_arch.

    python3 code/KI_spectrum.py
"""
import os, sys, io, contextlib
import numpy as np
from scipy.linalg import toeplitz, eigvalsh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import cc_arch as cc


def eigs_at(L, omega=4e-3, vals=None):
    n = int(L / omega) + 1
    if vals is None or len(vals) < n:
        vals = np.array([cc.Qeps(np.exp(k * omega)) for k in range(n)])
    T = toeplitz(vals[:n]) * omega / (2 * cc.eps1)
    ev = np.sort(eigvalsh(T))[::-1]
    return ev, vals


if __name__ == "__main__":
    omega = 4e-3
    ev2, vals = eigs_at(np.log(2), omega)
    ev3, _ = eigs_at(np.log(3), omega, vals=np.array(
        list(vals) + [cc.Qeps(np.exp(k * omega)) for k in range(len(vals), int(np.log(3)/omega)+1)]
    ))
    # crossing of λ2
    lo, hi = 0.85, 1.12
    cache = list(vals)
    def ev1_2(L):
        n = int(L / omega) + 1
        while len(cache) < n:
            cache.append(cc.Qeps(np.exp(len(cache) * omega)))
        T = toeplitz(np.array(cache[:n])) * omega / (2 * cc.eps1)
        ev = np.sort(eigvalsh(T))[::-1]
        return ev
    for _ in range(12):
        mid = 0.5 * (lo + hi)
        if ev1_2(mid)[1] > 1:
            hi = mid
        else:
            lo = mid
    xc = 0.5 * (lo + hi)
    print(f"K_I log2: {np.round(ev2[:3],5)}  n>1={(ev2>1).sum()}")
    print(f"K_I log3: {np.round(ev3[:3],5)}  n>1={(ev3>1).sum()}")
    print(f"lambda2 crosses 1 at L={xc:.4f}")
