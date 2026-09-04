"""Geometric depth law, frozen coefficients a=1.69, b=0.82 (§67)."""
import numpy as np

A, B = 1.69, 0.82


def F(mu, zeros, gcut=None):
    zeros = sorted(float(g) for g in zeros)
    L = float(np.log(mu))
    ny = 2 * np.pi / L
    desert = max(zeros[0] - ny, 0.0) if zeros else 0.0
    zs = zeros if gcut is None else [g for g in zeros if g <= gcut]
    excess = 0.0
    for i in range(len(zs) - 1):
        excess += max(zs[i + 1] - zs[i] - ny, 0.0)
    return A * L * desert + B * L * excess


def s_pred(mu1, mu2, zeros, gcut1=None, gcut2=None):
    return (F(mu2, zeros, gcut2) - F(mu1, zeros, gcut1)) / (mu2 - mu1)
