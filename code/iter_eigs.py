"""Inverse iteration / RQI for prime-side Q.

    python3 code/iter_eigs.py chi5 16 8 22
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["RETURN_S"] = "1"
from scan_s import assemble
import mpmath as mp


def eye(N):
    I = mp.matrix(N)
    for i in range(N):
        I[i, i] = mp.mpf(1)
    return I


def inv_iter(S, nsteps=4):
    N = S.rows
    v = mp.matrix([mp.mpf(1), mp.mpf(-1)] + [mp.mpf(0)] * (N - 2))
    v = v / mp.norm(v)
    for _ in range(nsteps):
        v = mp.lu_solve(S, v)
        v = v / mp.norm(v)
    return (v.T * S * v)[0], v


def rqi(S, nsteps=8):
    N = S.rows
    v = mp.matrix([mp.mpf(1), mp.mpf(-1)] + [mp.mpf(0)] * (N - 2))
    v = v / mp.norm(v)
    sig = (v.T * S * v)[0]
    for _ in range(nsteps):
        v = mp.lu_solve(S - sig * eye(N), v)
        v = v / mp.norm(v)
        nxt = (v.T * S * v)[0]
        if abs(nxt - sig) < mp.mpf("1e-20") * max(abs(nxt), mp.mpf("1e-40")):
            sig = nxt
            break
        sig = nxt
    return sig, v


def main():
    name, mu, NB, dps = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    lam, ell, dt, S = assemble(name, mu, NB, dps)
    t0 = time.time()
    li, _ = inv_iter(S)
    print(f"inv0  {mp.nstr(li, 6)}  {time.time()-t0:.2f}s")
    t0 = time.time()
    lq, _ = rqi(S)
    print(f"RQI   {mp.nstr(lq, 6)}  {time.time()-t0:.2f}s")
    print(f"eigsy {mp.nstr(lam, 6)}")


if __name__ == "__main__":
    main()
