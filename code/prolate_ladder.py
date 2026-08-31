import mpmath as mp, sys, time
import numpy.polynomial.legendre as NL

def ladder(c, N, dps):
    mp.mp.dps = dps
    t0 = time.time()
    xr0, _ = NL.leggauss(N)
    xs, ws = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(6):
            P = mp.legendre(N, x); Pm = mp.legendre(N-1, x)
            dP = N*(x*P - Pm)/(x*x - 1); x = x - P/dP
        P = mp.legendre(N, x); Pm = mp.legendre(N-1, x)
        dP = N*(x*P - Pm)/(x*x - 1)
        xs.append(x); ws.append(2/((1-x*x)*dP*dP))
    cc = mp.mpf(c)
    M = mp.matrix(N, N)
    for i in range(N):
        for j in range(i, N):
            d = xs[i]-xs[j]
            K = cc/mp.pi if i == j else mp.sin(cc*d)/(mp.pi*d)
            v = mp.sqrt(ws[i]*ws[j])*K
            # complement : I - S
            M[i,j] = (1 if i == j else 0) - v
            M[j,i] = M[i,j]
    E = mp.eigsy(M, eigvals_only=True)
    lv = [float(-mp.log(E[k])) for k in range(10) if E[k] > 0]
    print(f"c = {c} (2c = {2*c}), N = {N}, dps = {dps}, {time.time()-t0:.0f}s")
    print("  niveaux -ln(1-lambda_k) :", [f"{x:.1f}" for x in lv[:8]])
    print("  espacements :", [f"{lv[k]-lv[k+1]:.1f}" for k in range(min(6, len(lv)-1))])

if __name__ == '__main__':
    ladder(float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
