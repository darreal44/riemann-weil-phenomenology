import numpy as np, pickle, mpmath as mp, time
zeros = np.array(pickle.load(open('zeros280.pkl','rb')))
s = 0.05
w = np.exp(-s*s*zeros*zeros); m = w > 1e-18
zz, ww = zeros[m], w[m]
print(f"Bande s=0.05 : {m.sum()} zeros effectifs -> rang max du noyau = {2*m.sum()} (cos+sin par zero)")

# ---- taux par degre de liberte a U=2.5 fixe, jusqu'au mur de rang ----
print("\nU = 2.5 fixe, on densifie le peigne (float64) :")
prev = None
for J in [6, 11, 21, 41, 51, 61, 71, 81, 86, 91]:
    delta = 2.5/(J-1)
    Dg = np.arange(J)*delta
    kv = np.array([np.sum(2*np.cos(zz*d)*ww) for d in Dg])
    W = kv[np.abs(np.subtract.outer(np.arange(J), np.arange(J)))]
    ev = np.linalg.eigvalsh(0.5*(W+W.T))
    e0, diag = ev[0], kv[0]
    rate = ""
    if prev is not None and e0 > 1e-16*ev[-1] and prev[1] > 0:
        rate = f"   taux/dim = {np.log(prev[1]/(e0/diag))/(J-prev[0]):.3f}"
    flag = " (plancher float64)" if e0 < 1e-13*ev[-1] else ""
    print(f"  J = {J:3d} : marge/diag = {e0/diag:10.3e}{flag}{rate}")
    prev = (J, e0/diag if e0 > 0 else prev[1] if prev else 1)

# ---- plongee multiprecision sur la cellule la plus profonde fiable+1 ----
print("\nVerification multiprecision (dps = 50), J = 61 :")
mp.mp.dps = 50
t0 = time.time()
J = 61; delta = 2.5/(J-1)
zzm = [mp.mpf(g) for g in zz]
kv = []
for j in range(J):
    d = mp.mpf(j)*mp.mpf(delta)
    kv.append(sum(2*mp.cos(g*d)*mp.exp(-mp.mpf(s)**2*g*g) for g in zzm))
M = mp.matrix(J, J)
for a in range(J):
    for b in range(J):
        M[a,b] = kv[abs(a-b)]
E = mp.eigsy(M, eigvals_only=True)
print(f"  marge mp = {mp.nstr(E[0], 6)} ; marge/diag = {mp.nstr(E[0]/kv[0], 6)}")
print(f"  (float64 au meme point : voir ci-dessus ; temps mp = {time.time()-t0:.0f}s)")
