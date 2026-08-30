import mpmath as mp
import numpy as np
mp.mp.dps = 30

# ============ A. Audit des conventions + cote theorique ============
# 1) Phi_c : noyau theta classique, Xi_classique(t) = int_R Phi_c(u) e^{itu} du ?
def Phi_c(u):
    u = abs(u)   # fonction paire (equation fonctionnelle de theta)
    s = mp.mpf(0)
    for n in range(1, 9):
        s += (2*mp.pi**2*n**4*mp.e**(mp.mpf(9)*u/2) - 3*mp.pi*n**2*mp.e**(mp.mpf(5)*u/2))*mp.e**(-mp.pi*n*n*mp.e**(2*u))
    return s

def xi_classique(t):
    s = mp.mpf('0.5') + 1j*t
    return mp.re(mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))

def xi_suzuki(t):
    return 2*xi_classique(t)

print("Verification de l'identite de Fourier (facteur exact) :")
for t in [0, 3, 7, 12]:
    I = 2*mp.quad(lambda u: Phi_c(u)*mp.cos(t*u), [0, 0.5, 1, 1.6])
    xc = xi_classique(t)
    print(f"  t={t:2d} : int Phi_c e^(itu) du = {mp.nstr(I,8)}   xi_cl(1/2+it) = {mp.nstr(xc,8)}   ratio = {mp.nstr(I/xc,6)}")

# 2) norme L2 du noyau correspondant a la convention Suzuki (Xi_S = 2 Xi_cl -> Phi_S = 2 Phi_c)
n2 = 2*mp.quad(lambda u: (2*Phi_c(u))**2, [0, 0.5, 1, 1.6])
print(f"\n||Phi_S||_L2(R) = {mp.nstr(mp.sqrt(n2),8)}    (prediction naive pour c_infini si v_a -> Phi/||Phi|| en L2)")

# 3) ajustement empirique c_a = c_inf + k/mu sur les points convergés en base
data = [(3.5,1.2173),(5.5,1.180),(7.5,1.1648),(9.5,1.1553),(11,1.1537),(16,1.1475)]
X = np.array([[1/m, 1] for m,_ in data]); y = np.array([c for _,c in data])
k, cinf = np.linalg.lstsq(X, y, rcond=None)[0]
pred = X@[k,cinf]
print(f"\nAjustement c_a = c_inf + k/mu : c_inf = {cinf:.4f}, k = {k:.4f}")
for (m,c),p in zip(data,pred):
    print(f"  mu={m:5.1f} : mesure {c:.4f}  ajuste {p:.4f}  ecart {c-p:+.4f}")
print(f"\nCandidats : ||Phi_S|| = {float(mp.sqrt(n2)):.4f} ;  2/sqrt(pi) = {float(2/mp.sqrt(mp.pi)):.4f} ;  c_inf mesure = {cinf:.4f}")
print(f"Rapport c_inf / ||Phi_S|| = {cinf/float(mp.sqrt(n2)):.4f}  (= 1/alpha si une fraction alpha de la masse L2 est dans la forme)")
