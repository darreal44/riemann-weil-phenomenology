import mpmath as mp, io, contextlib, sys, numpy as np
import __main__
srcC = open('spectro.py').read().replace("    E, V = mp.eigsy(S)", "    import __main__; __main__.SCAP = S; E, V = mp.eigsy(S)")
ns = {}
exec(compile(srcC.replace("if __name__ == '__main__':", "if False:"), "s", "exec"), ns)
def towers_for(tab, q, mu, NP, L):
    om = [2*mp.pi*n/L for n in range(NP)]
    def th(n, m, y):
        if n == 0 and m == 0: return 2*(L - y)/L
        if n == 0 or m == 0:
            j = max(n, m); return -2*mp.sin(om[j]*y)/(mp.sqrt(2)*mp.pi*j)
        if n == m: return 2*((L - y)*mp.cos(om[n]*y)/L - mp.sin(om[n]*y)/(2*mp.pi*n))
        return 2*(n*mp.sin(om[n]*y) - m*mp.sin(om[m]*y))/(mp.pi*(m*m - n*n))
    T = {}
    for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if p >= mu or tab[p % q] == 0: continue
        M = mp.matrix(NP, NP); k = 1
        while p**k <= mu:
            y = k*mp.log(p); w = mp.log(p)/mp.sqrt(p**k)*tab[(p**k) % q]
            for n in range(NP):
                for m in range(n, NP):
                    v = w*th(n, m, y); M[n,m] += v
                    if m != n: M[m,n] += v
            k += 1
        T[p] = M
    return T
mu = float(sys.argv[1]); NB = int(sys.argv[2]); dps = int(sys.argv[3])
for name, q, tab, s in [('chi3', 3, [0,1,-1], 4.00), ('chi4', 4, [0,1,0,-1], 2.93)]:
    mp.mp.dps = dps
    with contextlib.redirect_stdout(io.StringIO()):
        ns['run'](mp.mpf(mu), NB, dps, 12, K=1, q=q, tab=tab, apar=1)
    S = __main__.SCAP; NP = NB+1; L = mp.log(mu)
    E, V = mp.eigsy(S); v = mp.matrix([V[i,0] for i in range(NP)])
    T = towers_for(tab, q, mu, NP, L)
    ps, ld, lk = [], [], []
    for p in sorted(T):
        w = T[p]*v; d = (v.T*w)[0]; k2 = (w.T*w)[0] - d*d
        ps.append(p); ld.append(float(-mp.log(abs(d)))); lk.append(float(-mp.log(mp.sqrt(k2))))
    sd = np.polyfit(ps, ld, 1)[0]; sk = np.polyfit(ps, lk, 1)[0]
    print(f"{name} mu={mu:.0f} N={NP}: eps={mp.nstr(E[0],2)} votants {ps} ; -ln|delta| = {np.round(ld,2)} ; -ln kappa = {np.round(lk,2)} ; pentes : silence {sd:.2f}/p (0.6 s = {0.6*s:.2f}), couplage {sk:.2f}/p", flush=True)
