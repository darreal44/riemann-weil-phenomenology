"""H11 on unit e1: Arch by quad of the regular integrand, P by elementary theta.
No scan_s matrix, no zeros.

    python3 code/H11_independent.py
"""
import os, sys
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kronecker import chi_tab

CHARS = {
    "chi5": (5, 5, 0),
    "chi3": (-3, 3, 1),
    "chi4": (-4, 4, 1),
    "chi8": (8, 8, 0),
    "chi13": (13, 13, 0),
}


def theta_f1(y, L):
    if y >= L:
        return mp.mpf(0)
    w = 2 * mp.pi / L
    return (mp.mpf(2) / 3) * (1 - y / L) * (2 + mp.cos(w * y)) + mp.sin(w * y) / mp.pi


def Arch_f1(L, q, s0):
    F0 = 2
    CST = mp.log(q / mp.pi) - mp.euler - mp.log(1 - mp.e ** (-2 * L))

    def g(y):
        if y == 0:
            return mp.mpf(0)
        K = 2 * mp.e ** (-2 * s0 * y) / (1 - mp.e ** (-2 * y))
        EC = mp.e ** (-(2 - 2 * s0) * y)
        return K * (F0 * EC - theta_f1(y, L))

    I = mp.quad(g, [mp.mpf(0), L])
    return F0 / 2 * CST + I / 2


def P_f1(mu, d, q):
    L = mp.log(mu)
    tab = chi_tab(d, q)
    cap = int(mu)
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    acc = mp.mpf(0)
    for n in range(2, cap + 1):
        y2, p = n, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if not (p and y2 == 1 and tab[n % q] != 0):
            continue
        w = tab[n % q] * mp.log(p) / mp.sqrt(n)
        acc += w * theta_f1(mp.log(n), L)
    return acc


def H11(name, mu=16, dps=40):
    mp.mp.dps = dps
    d, q, a = CHARS[name]
    L = mp.log(mu)
    s0 = mp.mpf(1) / 4 + mp.mpf(a) / 2
    A = Arch_f1(L, q, s0)
    P = P_f1(mu, d, q)
    return A, P, A - P


if __name__ == "__main__":
    mp.mp.dps = 40
    ref = dict(chi5=9.31467e-5, chi3=2.17859e-4, chi8=1.7067e-3, chi13=0.211858, chi4=1.17863e-3)
    for name in CHARS:
        A, P, H = H11(name)
        print(
            f"[{name} mu=16 H11-indep] Arch={mp.nstr(A,6)} P={mp.nstr(P,6)} "
            f"H11={mp.nstr(H,6)}  vs 2plane {ref[name]:.6e}  rel={float(H)/ref[name]-1:+.2e}"
        )
