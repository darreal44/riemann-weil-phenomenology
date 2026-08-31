# Identites de bord de la table de correlation (App. A de la note quorum) + table vs quadrature directe.
# Usage : python3 tests/test_theta_endpoints.py   (mpmath seul, ~10 s)
import mpmath as mp
mp.mp.dps = 25
L = mp.log(11); om = [2*mp.pi*n/L for n in range(8)]
def th(n, m, x):
    if n==0 and m==0: return 2*(L-x)/L
    if n==0 or m==0:
        j=max(n,m); return -2*mp.sin(om[j]*x)/(mp.sqrt(2)*mp.pi*j)
    if n==m: return 2*((L-x)*mp.cos(om[n]*x)/L - mp.sin(om[n]*x)/(2*mp.pi*n))
    return 2*(n*mp.sin(om[n]*x)-m*mp.sin(om[m]*x))/(mp.pi*(m*m-n*n))
# Theta(0) = 2 (diagonale), 0 (hors-diagonale) ; Theta(L) = 0 partout (recouvrement vide)
for n in range(4):
    for m in range(4):
        assert abs(th(n,m,mp.mpf(0)) - (2 if n==m else 0)) < 1e-20, (n,m,'x=0')
        assert abs(th(n,m,L)) < 1e-20, (n,m,'x=L')
# table = autocorrelation symetrisee (base cosinus decalee), 3 points de controle
def eta(k,u): return (1/mp.sqrt(L)) if k==0 else mp.sqrt(2/L)*mp.cos(om[k]*(u+L/2))
def auto(n,m,x):
    return mp.quad(lambda u: eta(n,u)*eta(m,u+x), [-L/2, L/2-x]) + mp.quad(lambda u: eta(n,u)*eta(m,u-x), [-L/2+x, L/2])
for (n,m,x) in [(1,1,0.7),(1,2,0.7),(0,3,0.9)]:
    assert abs(th(n,m,mp.mpf(x)) - auto(n,m,mp.mpf(x))) < 1e-18, (n,m,x)
print("test_theta_endpoints : OK (bords exacts, table = autocorrelation a 1e-18)")

# identite du pole (App. B / weil_normalization_check) : P(0,0) = ghat(i/2)+ghat(-i/2), exacte
P00 = mp.quad(lambda y: 2*(L-y)/L*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
gpole = mp.quad(lambda y: (L-abs(y))/L*(mp.e**(y/2)+mp.e**(-y/2)), [-L, 0, L])
assert abs(P00 - gpole) < 1e-18, "identite du pole cassee"
print("test pole : OK (P(0,0) = ghat(i/2)+ghat(-i/2) a 1e-18)")
