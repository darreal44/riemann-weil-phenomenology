# Verification publique de l'identification Weil-Bombieri des composantes certifiees.
# Identites testees (g = correlation de eta_0, le premier vecteur de base) :
#   (1) POLE  : int_0^L Theta(y)(e^{y/2}+e^{-y/2}) dy  =  ghat(i/2) + ghat(-i/2)      [exacte]
#   (2) ARCH  : A_code(g) + g(0) log(pi)  =  (1/2pi) int ghat(t) Re psi(1/4 + it/2) dt [exacte ;
#               le residu numerique est la queue oscillante de l'integrale de controle, en 1/T]
# Usage : python3 weil_normalization_check.py   (~20 s, mpmath seul)
import mpmath as mp
mp.mp.dps = 30
L = mp.log(11)
ghat = lambda t: 4*mp.sin(t*L/2)**2/(L*t*t)
CL = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
A_code = -(CL + mp.quad(lambda y: (mp.e**(y/2)*2*(L-y)/L - 2)/(mp.e**y - mp.e**(-y)), [0, L]))
P00 = mp.quad(lambda y: 2*(L-y)/L*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
gpole = mp.quad(lambda y: (L-abs(y))/L*(mp.e**(y/2)+mp.e**(-y/2)), [-L, 0, L])
print(f"(1) pole : {mp.nstr(P00,12)} = {mp.nstr(gpole,12)}  (ecart {mp.nstr(P00-gpole,2)})")
for T in [400, 1600]:
    pts = [0, 4, 20, 80] + list(range(200, T+1, 100))   # panneaux fins face a l'oscillation sin^2(tL/2)
    arch = (1/mp.pi)*mp.quad(lambda t: ghat(t)*mp.re(mp.digamma(mp.mpf('0.25')+0.5j*t)), pts)
    tail = (2/(mp.pi*L))*(mp.log(T/2)+1)/T
    print(f"(2) arch, controle a T={T:5d} : psi-integrale+queue = {mp.nstr(arch+tail,9)}  vs  A_code+log(pi) = {mp.nstr(A_code+mp.log(mp.pi),9)}  (ecart {mp.nstr(arch+tail-A_code-mp.log(mp.pi),2)})")
print("accord au niveau de la queue d'ordre suivant (~1/T) ; identite (2) exacte, demonstration : note #3, appendice B.")
