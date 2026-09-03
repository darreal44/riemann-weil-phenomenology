"""2-adic peak weights of tau_S - tau_arch vs Lambda.
Expected (Connes 1999 Thm 4): mass log2/sqrt(2) ~= 0.490 at lambda=2 and 1/2.
"""
import time
import numpy as np
import sys
sys.path.insert(0, "code")
from trace_dist import tau_curve

EXPECTED = np.log(2) / np.sqrt(2)


def weights(Lam, cpu, half=0.12):
    lams = np.concatenate([
        np.linspace(0.30, 0.90, 61),
        np.linspace(0.905, 1.095, 77),
        np.linspace(1.10, 3.30, 221),
    ])
    t0 = time.time()
    tA = tau_curve(Lam, False, lams, cells_per_unit=cpu)
    tS = tau_curve(Lam, True, lams, cells_per_unit=cpu)
    dt = time.time() - t0
    d = tS - tA
    out = {"Lam": Lam, "cpu": cpu, "sec": dt}
    for c in (0.5, 2.0):
        m = np.abs(lams - c) < half * c
        w = np.trapezoid(d[m] / lams[m], lams[m])
        peak = d[np.argmin(np.abs(lams - c))]
        out[f"w{c}"] = float(w)
        out[f"peak{c}"] = float(peak)
    # also a tighter and a wider window
    for c, tag, h in ((2.0, "tight", 0.06), (2.0, "wide", 0.25)):
        m = np.abs(lams - c) < h * c
        out[f"w2_{tag}"] = float(np.trapezoid(d[m] / lams[m], lams[m]))
    return out


if __name__ == "__main__":
    print(f"attendu  log2/sqrt(2) = {EXPECTED:.4f}")
    rows = []
    # Lambda=4,8 at cpu=16 (trend); 4 at cpu=32 (replay); 12 and 16 at cpu=12
    jobs = [(4, 16), (8, 16), (4, 32), (12, 12), (16, 10)]
    for Lam, cpu in jobs:
        r = weights(Lam, cpu)
        rows.append(r)
        print(
            f"Lam={r['Lam']:4.0f} cpu={r['cpu']:2d}  "
            f"w(1/2)={r['w0.5']:+7.3f}  w(2)={r['w2.0']:+7.3f}  "
            f"w2 tight/wide={r['w2_tight']:+6.3f}/{r['w2_wide']:+6.3f}  "
            f"peak2={r['peak2.0']:+7.2f}  {r['sec']:.1f}s"
        )
