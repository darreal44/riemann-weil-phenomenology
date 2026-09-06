"""2-plane H = E^T Q_3 E at three hats. Finite explicit formula, no zeros.

    python3 code/cert_2plane.py chi5 16 40
"""
import os, sys
os.environ["RETURN_S"] = "1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_s import assemble
import mpmath as mp


def frame(mp):
    s3, s15 = mp.sqrt(3), mp.sqrt(15)
    e1 = mp.matrix([mp.sqrt(2) / s3, -1 / s3, 0])
    e2 = mp.matrix([-mp.sqrt(2) / s15, -2 / s15, 3 / s15])
    return e1, e2


def cert(name, mu=16.0, dps=40):
    mp.mp.dps = dps
    lam, ell, dt, S = assemble(name, float(mu), 2, dps)
    assert S.rows >= 3
    e1, e2 = frame(mp)
    H = mp.matrix(2)
    for i, ei in enumerate((e1, e2)):
        for j, ej in enumerate((e1, e2)):
            H[i, j] = sum(ei[a] * S[a, b] * ej[b] for a in range(3) for b in range(3))
    det = H[0, 0] * H[1, 1] - H[0, 1] * H[1, 0]
    tr = H[0, 0] + H[1, 1]
    lmin = det / tr if tr != 0 else mp.nan
    ev = mp.eigsy(H, eigvals_only=True)
    print(
        f"[{name} mu={mu} 2-plane dps={dps}]  "
        f"H11={mp.nstr(H[0,0],6)} H12={mp.nstr(H[0,1],6)} H22={mp.nstr(H[1,1],6)}  "
        f"det={mp.nstr(det,4)}  det/tr={mp.nstr(lmin,4)}  "
        f"eig={mp.nstr(min(ev),4)},{mp.nstr(max(ev),4)}  "
        f"Q3.lam0={mp.nstr(lam,4)}"
    )
    return dict(name=name, mu=mu, dps=dps, H11=H[0, 0], H12=H[0, 1], H22=H[1, 1],
                det=det, lmin_bound=lmin, eig_min=min(ev), eig_max=max(ev), Q3=lam)


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "chi5"
    mu = float(sys.argv[2]) if len(sys.argv) > 2 else 16.0
    dps = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    cert(name, mu, dps)
