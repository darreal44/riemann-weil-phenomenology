"""Full 2x2 H on {e1,e2} without the hat matrix.

Arch: quad of the regular integrand K*(F0 EC - theta_e,f).
P: elementary th_nm at log n. No zeros.

    python3 code/H_2plane_independent.py
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


def th(n, m, y, L):
    om = lambda k: 2 * mp.pi * k / L
    if n == 0 and m == 0:
        return 2 * (L - y) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * mp.sin(om(j) * y) / (mp.sqrt(2) * mp.pi * j)
    if n == m:
        return 2 * ((L - y) * mp.cos(om(n) * y) / L - mp.sin(om(n) * y) / (2 * mp.pi * n))
    return 2 * (n * mp.sin(om(n) * y) - m * mp.sin(om(m) * y)) / (mp.pi * (m * m - n * n))


def frame():
    s3, s15 = mp.sqrt(3), mp.sqrt(15)
    e1 = [mp.sqrt(2) / s3, -1 / s3, mp.mpf(0)]
    e2 = [-mp.sqrt(2) / s15, -2 / s15, 3 / s15]
    return e1, e2


def theta_vec(e, f, y, L):
    return sum(e[n] * f[m] * th(n, m, y, L) for n in range(3) for m in range(3))


def F0_vec(e, f):
    return sum(e[n] * f[m] * (2 if n == m else 0) for n in range(3) for m in range(3))


def Arch_pair(e, f, L, q, s0):
    F = F0_vec(e, f)
    CST = mp.log(q / mp.pi) - mp.euler - mp.log(1 - mp.e ** (-2 * L))

    def g(y):
        if y == 0:
            return mp.mpf(0)
        K = 2 * mp.e ** (-2 * s0 * y) / (1 - mp.e ** (-2 * y))
        EC = mp.e ** (-(2 - 2 * s0) * y)
        return K * (F * EC - theta_vec(e, f, y, L))

    I = mp.quad(g, [mp.mpf(0), L])
    return F / 2 * CST + I / 2


def P_pair(e, f, mu, d, q):
    L = mp.log(mu)
    tab = chi_tab(d, q)
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    acc = mp.mpf(0)
    for n in range(2, int(mu) + 1):
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
        acc += w * theta_vec(e, f, mp.log(n), L)
    return acc


def H2(name, mu=16, dps=28):
    mp.mp.dps = dps
    d, q, a = CHARS[name]
    L = mp.log(mu)
    s0 = mp.mpf(1) / 4 + mp.mpf(a) / 2
    e1, e2 = frame()
    H = mp.matrix(2)
    parts = {}
    for i, ei in enumerate((e1, e2)):
        for j, ej in enumerate((e1, e2)):
            A = Arch_pair(ei, ej, L, q, s0)
            P = P_pair(ei, ej, mu, d, q)
            H[i, j] = A - P
            parts[(i, j)] = (A, P)
    det = H[0, 0] * H[1, 1] - H[0, 1] * H[1, 0]
    ev = mp.eigsy(H, eigvals_only=True)
    return H, det, ev, parts


if __name__ == "__main__":
    for name in ("chi5", "chi3", "chi4", "chi8", "chi13"):
        H, det, ev, _ = H2(name)
        print(
            f"[{name} 2x2-indep] H11={mp.nstr(H[0,0],5)} H12={mp.nstr(H[0,1],5)} "
            f"H22={mp.nstr(H[1,1],5)} det={mp.nstr(det,4)} eigmin={mp.nstr(min(ev),4)}"
        )
