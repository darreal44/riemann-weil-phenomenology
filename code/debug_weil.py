import mpmath as mp, pickle
import numpy as np
mp.mp.dps = 30

mu = mp.mpf('5.5'); L = mp.log(mu); Lf = float(L)
print(f"mu=5.5, L={Lf:.6f}")

# ---------------- Entree (0,0) : F(y) = 2(L-y)/L ----------------
# 1) POLE : verif forme fermee 32 sinh^2(L/4)/L
W02_num = mp.quad(lambda y: 2*(L-y)/L*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
W02_cf  = 32*mp.sinh(L/4)**2/L
print(f"\nPOLE  : numerique = {mp.nstr(W02_num,8)}  forme fermee = {mp.nstr(W02_cf,8)}  -> {'OK' if abs(W02_num-W02_cf)<1e-10 else 'ECART'}")

# 2) ARCHIMEDIEN : (2.32) vs Q_infini de (2.11) = int |f^(t)|^2 (2 theta'(t)/2pi) dt
CR = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
WR_232 = mp.mpf(2)/2*CR + mp.quad(lambda y: mp.e**(y/2)*(2*(L-y)/L-2)/(mp.e**y-mp.e**(-y)), [0, L])
# Q_infini : f^(t) = L^{-1/2} 2 sin(tL/2)/t ; 2theta'(t)/2pi = (Re psi(1/4+it/2) - log pi)/(2pi)... 
# theta(t) = -t/2 log pi + Im logGamma(1/4+it/2) ; theta'(t) = -log(pi)/2 + Re psi(1/4+it/2)/2
def integrand(t):
    fh2 = (2*mp.sin(t*L/2)/t)**2/L if abs(t)>1e-12 else L
    thp = -mp.log(mp.pi)/2 + mp.re(mp.digamma(mp.mpf('0.25')+0.5j*t))/2
    return fh2*2*thp/(2*mp.pi)
Qinf = 2*mp.quad(integrand, [0, 5, 20, 100, 500, 2000])   # pair -> 2x demi-axe
# queue analytique : theta' ~ (1/2)log(t/4pi... approx (1/2)log(t/2pi)) ; |fh|^2 moy = 2/(L t^2)
T = 2000
tail = 2*mp.quad(lambda t: (2/(L*t*t))*2*((mp.log(t/(2*mp.pi))/2))/(2*mp.pi), [T, mp.inf])
print(f"ARCH  : WR(2.32) = {mp.nstr(WR_232,8)}")
print(f"        -W_R attendu = +Q_inf   ->  Q_inf = {mp.nstr(Qinf,6)} (+ queue ~ {mp.nstr(tail,3)})")
print(f"        donc WR devrait valoir  -Q_inf = {mp.nstr(-Qinf-tail,6)}")

# 3) PREMIERS
pp = [(2,2),(3,3),(4,2),(5,5)]
Wp = mp.fsum(mp.log(p)/mp.sqrt(n)*2*(L-mp.log(n))/L for n,p in pp)
print(f"PRIME : Wp = {mp.nstr(Wp,8)}")

sigma00 = W02_cf - WR_232 - Wp
print(f"\nsigma(0,0) via (2.32) = {mp.nstr(sigma00,6)}")
sigma00b = W02_cf + Qinf + tail - Wp
print(f"sigma(0,0) via Q_inf  = {mp.nstr(sigma00b,6)}")

# 4) COTE ZEROS avec facteur correct : somme sur rho = paires +-gamma
#    Q(eta0) = sum_rho h^(gamma_rho) = sum_{gamma>0} 2 * [2 int_0^L F cos(gamma y) dy]
zeros = pickle.load(open('zeros280.pkl','rb'))
zs = 0.0
for g in zeros:
    # F^ pour F=2(L-y)/L : 2*(2/L)*(1-cos(gL))/g^2
    zs += 2*(4/Lf)*(1-np.cos(g*Lf))/g**2
# queue au-dela de gamma_280 ~ 513.7 : densite dN = log(t/2pi)/(2pi) dt, moyenne (1-cos)=1
gmax = zeros[-1]
tailz = float(2*mp.quad(lambda t: (4/L)/t**2*mp.log(t/(2*mp.pi))/(2*mp.pi), [gmax, mp.inf]))
print(f"\nZEROS : somme 280 zeros = {zs:.6f} + queue ~ {tailz:.6f}  ->  {zs+tailz:.6f}")
