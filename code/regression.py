import numpy as np

# donnees : (nom, gamma1, pente s, err, D = masse arithmetique retiree sum_{p|q} log p/(sqrt p - 1), parite 0=pair 1=impair)
data = [
 ('chi3',  8.040, 4.00, 0.07, 1.5006, 1),
 ('chi4',  6.021, 2.93, 0.04, 1.6730, 1),
 ('chi5',  6.648, 2.41, 0.04, 1.3018, 0),
 ('chi7',  4.476, 1.58, 0.05, 1.1827, 1),
 ('chi8',  4.900, 1.47, 0.05, 1.6730, 0),
 ('chi11', 2.477, 0.91, 0.08, 1.0350, 1),
 ('chi12', 3.805, 0.94, 0.05, 3.1736, 0),
 ('chi13', 3.119, 0.88, 0.06, 0.9840, 0),
 ('chi15', 3.057, 0.70, 0.05, 2.8024, 1),
 ('chi24o',1.977, 0.45, 0.10, 3.1736, 1),
 ('chi24e',2.689, 0.52, 0.05, 3.1736, 0),
]
g  = np.array([d[1] for d in data]); s = np.array([d[2] for d in data])
D  = np.array([d[4] for d in data]); par = np.array([d[5] for d in data])
ls, lg = np.log(s), np.log(g)

def fit(X, y):
    A = np.column_stack([X, np.ones(len(y))])
    coef, res, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    return coef, np.sqrt(np.mean((y - pred)**2)), pred

print("=== Modeles sur les 11 caracteres (ln s comme cible) ===")
c0, r0, _ = fit(lg.reshape(-1,1), ls)
print(f"M0  ln s = {c0[0]:.3f} ln g1 + {c0[1]:.3f}                      RMS = {r0:.4f}")
c1, r1, _ = fit(np.column_stack([lg, D]), ls)
print(f"M1  ln s = {c1[0]:.3f} ln g1 + {c1[1]:+.3f} D + {c1[2]:.3f}       RMS = {r1:.4f}")
c2, r2, _ = fit(np.column_stack([lg, D, par]), ls)
print(f"M2  M1 + parite : coef parite = {c2[2]:+.3f}                  RMS = {r2:.4f}")

# collapse a une variable : X = g1 * exp(-theta D), loi de puissance ln s = b ln X + a
print("\n=== Collapse a une variable : X = gamma1 * exp(-theta*D) ===")
best = None
for th in np.linspace(0, 0.6, 121):
    lX = lg - th*D
    c, r, _ = fit(lX.reshape(-1,1), ls)
    if best is None or r < best[1]: best = (th, r, c)
th, r, c = best
print(f"theta* = {th:.3f} : ln s = {c[0]:.3f} ln X + {c[1]:.3f}, RMS = {r:.4f}  (vs {r0:.4f} sans D)")
lX = lg - th*D
pred = c[0]*lX + c[1]
print("\n  point     g1     D     s mesure   s modele   ecart")
for i, d in enumerate(data):
    print(f"  {d[0]:7s} {d[1]:6.3f} {d[4]:5.2f}   {s[i]:7.2f}   {np.exp(pred[i]):7.2f}   {100*(s[i]/np.exp(pred[i])-1):+5.1f}%")

# validation croisee leave-one-out du collapse
loo = []
for k in range(len(data)):
    m = np.arange(len(data)) != k
    bst = None
    for th2 in np.linspace(0, 0.6, 61):
        lX2 = lg[m] - th2*D[m]
        c2b, r2b, _ = fit(lX2.reshape(-1,1), ls[m])
        if bst is None or r2b < bst[0]: bst = (r2b, th2, c2b)
    _, th2, c2b = bst
    loo.append(abs(ls[k] - (c2b[0]*(lg[k]-th2*D[k]) + c2b[1])))
print(f"\nLOO : erreur mediane {100*np.median(loo):.1f}% , max {100*max(loo):.1f}% ({data[int(np.argmax(loo))][0]})")

# prediction pour chi19 en fonction de gamma1 (D_19 = log19/(sqrt19-1) = 0.8764)
print("\n=== Prediction preenregistree pour chi19 (D = 0.876, impair) ===")
for g19 in [1.5, 2.0, 2.5, 3.0]:
    x = np.log(g19) - th*0.8764
    print(f"  si gamma1(chi19) = {g19} : s predit = {np.exp(c[0]*x + c[1]):.2f}")
print(f"  (modele M0 sans densite predirait : {[f'{np.exp(c0[0]*np.log(gg)+c0[1]):.2f}' for gg in [1.5,2.0,2.5,3.0]]})")
