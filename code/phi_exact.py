import mpmath as mp
mp.mp.dps = 40

# Formes fermees : pour chi primitif reel,
#   pair  (a=0) : Phi(u) = 2 e^(u/2)  * sum chi(n)   exp(-pi n^2 e^(2u)/q),  Lambda(1/2+iz) = int Phi e^(izu) du
#   impair(a=1) : Phi(u) = 2 e^(3u/2) * sum chi(n) n exp(-pi n^2 e^(2u)/q)
# Validation : rapport int/Lambda a plusieurs z (doit etre 1 plat), puis ||Phi||_L2 en serie.
CH = {
 'chi3': (3, [0,1,-1], 1), 'chi4': (4, [0,1,0,-1], 1), 'chi5': (5, [0,1,-1,-1,1], 0),
 'chi7': (7, [0,1,1,-1,1,-1,-1], 1), 'chi8': (8, [0,1,0,-1,0,-1,0,1], 0),
}
def Lam(z, q, tab, a):
    s = mp.mpf('0.5') + 1j*z
    L = q**(-s)*mp.fsum(tab[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if tab[r])
    return mp.re((mp.mpf(q)/mp.pi)**((s+a)/2)*mp.gamma((s+a)/2)*L)

print(f"{'':7s} {'ratio z=0':>12s} {'z=4':>12s} {'z=9':>12s} {'||Phi|| ferme':>16s} {'numerique (avant)':>18s}")
prev = {'chi3':0.51531,'chi4':0.81580,'chi5':0.78699,'chi7':1.87569,'chi8':1.28252}
for name,(q, tab, a) in CH.items():
    def Phi(u):
        # serie sur n>=1, symetrisee par parite de u via l'equation fonctionnelle (Phi paire)
        uu = abs(u)
        w = mp.e**(2*uu)
        s = mp.fsum(tab[n % q]*(n if a else 1)*mp.e**(-mp.pi*n*n*w/q) for n in range(1, 40) if tab[n % q])
        return 2*mp.e**((mp.mpf(3)/2 if a else mp.mpf('0.5'))*uu)*s
    rats = []
    for z in [0, 4, 9]:
        I = mp.quad(lambda u: Phi(u)*mp.cos(z*u), [-2.5, -1, 0, 1, 2.5])
        rats.append(I/Lam(z, q, tab, a))
    n2 = mp.sqrt(mp.quad(lambda u: Phi(u)**2, [-2.5, -1, 0, 1, 2.5]))
    print(f"{name:7s} {mp.nstr(rats[0],8):>12s} {mp.nstr(rats[1],8):>12s} {mp.nstr(rats[2],8):>12s} {mp.nstr(n2,12):>16s} {prev[name]:>18.5f}")

# zeta, rappel avec la meme machinerie (Phi_S = 4 Phi_c)
def PhiS(u):
    uu = abs(u)
    return 4*mp.fsum((2*mp.pi**2*n**4*mp.e**(mp.mpf(9)*uu/2) - 3*mp.pi*n**2*mp.e**(mp.mpf(5)*uu/2))*mp.e**(-mp.pi*n*n*mp.e**(2*uu)) for n in range(1, 12))
n2z = mp.sqrt(mp.quad(lambda u: PhiS(u)**2, [-2, -0.8, 0, 0.8, 2]))
print(f"{'zeta':7s} {'':>12s} {'':>12s} {'':>12s} {mp.nstr(n2z,12):>16s} {1.13093:>18.5f}")
