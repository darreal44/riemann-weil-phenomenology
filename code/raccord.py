import numpy as np, pickle
zeros = np.array(pickle.load(open('zeros280.pkl','rb')))

def kernel_vals(Deltas, s):
    w = np.exp(-s*s*zeros*zeros)
    m = w > 1e-18
    return np.array([np.sum(2*np.cos(zeros[m]*d)*w[m]) for d in Deltas]), int(m.sum())

def margin(J, delta, s):
    Dg = np.arange(J)*delta
    kv, neff = kernel_vals(Dg, s)
    W = kv[np.abs(np.subtract.outer(np.arange(J), np.arange(J)))]
    ev = np.linalg.eigvalsh(0.5*(W+W.T))
    return ev[0], ev[-1], kv[0], neff   # marge, max, diagonale, zeros effectifs

# ============================================================
# A. Pente alpha(s) : la fermeture s'accelere-t-elle quand la bande s'ouvre ?
# ============================================================
print("=== A. Pente de fermeture alpha(s), peigne delta = 0.5 ===")
for s in [0.05, 0.025, 0.0125]:
    pts = []
    for J in range(6, 27, 2):
        e0, emax, diag, neff = margin(J, 0.5, s)
        U = (J-1)*0.5
        if e0 > 1e-12*emax:            # au-dessus du plancher float64
            pts.append((U, e0/diag))    # marge normalisee par la diagonale
    pts = np.array(pts)
    A = np.vstack([pts[:,0], np.ones(len(pts))]).T
    sl, b0 = np.linalg.lstsq(A, np.log(pts[:,1]), rcond=None)[0]
    print(f"  s = {s:7.4f} : bande utile gamma < {np.sqrt(np.log(1e18))/s:6.0f} ({neff:3d} zeros), "
          f"alpha = {-sl:.3f}, points propres = {len(pts)}, marge norm. finale = {pts[-1,1]:.3e} a U = {pts[-1,0]}")

# ============================================================
# B. Le plongeon a support fixe U = 2.5 : (s, delta) -> 0
#    Reference CC (base complete, pas de bande) : ~2.4e-48 a U = log 11 = 2.40
# ============================================================
print("\n=== B. Plongeon a U = 2.5 fixe : marge normalisee (marge brute) ===")
print("      float64 ; * = sous le plancher 1e-13*max (non fiable)")
hdr = "  s \\ delta |" + "".join(f"   {d:7.4f}   " for d in [0.5, 0.25, 0.125, 0.0625])
print(hdr)
results = {}
for s in [0.05, 0.025, 0.0125]:
    row = f"  {s:8.4f} |"
    for delta in [0.5, 0.25, 0.125, 0.0625]:
        J = int(round(2.5/delta)) + 1
        e0, emax, diag, neff = margin(J, delta, s)
        flag = "*" if e0 < 1e-13*emax else " "
        results[(s,delta)] = (e0, diag)
        row += f" {e0/diag:9.2e}{flag}  "
    print(row)
print(f"\n  (JJ aux quatre deltas : {[int(round(2.5/d))+1 for d in [0.5,0.25,0.125,0.0625]]})")
print("  Reference Connes-Consani, meme support, base complete, sans bande : ~2.4e-48")
