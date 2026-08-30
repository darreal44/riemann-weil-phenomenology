import mpmath as mp, pickle, time
mp.mp.dps = 30

# ============ 1. Route archimedienne de Frullani, validee sur zeta ============
# W_psi(F; s0) = -gamma*F(0) - F(0)*log(1-e^(-2L)) + int_0^L [2F(0)e^(-2y) - 2F(y)e^(-2*s0*y)]/(1-e^(-2y)) dy
# Pour zeta : W_arch = -F(0)*log(pi)/?? ... convention CC (2.32) = (F0/2)(gamma+log(4pi tanh')) + int (e^(y/2)F - F0)/(e^y-e^-y)
# Test sur F(y) = 2(L-y)/L (entree (0,0), mu=5.5), ou (2.32) est certifie contre Q_infini.
L = mp.log(mp.mpf('5.5'))
F  = lambda y: 2*(L-y)/L
F0 = mp.mpf(2)

CR = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
WR_232 = F0/2*CR + mp.quad(lambda y: (mp.e**(y/2)*F(y)-F0)/(mp.e**y-mp.e**(-y)), [0, L])

def W_psi(Ffun, F0v, s0, Lv):
    tail = -F0v*mp.log(1-mp.e**(-2*Lv))
    I = mp.quad(lambda y: (2*F0v*mp.e**(-2*y) - 2*Ffun(y)*mp.e**(-2*s0*y))/(1-mp.e**(-2*y)), [0, Lv])
    return -mp.euler*F0v + tail + I
# arch zeta (convention demi, comme psi#) : (1/2)*[ -F0 log pi + W_psi(s0=1/4) ] * (-1)^? 
# On determine la normalisation empiriquement contre WR_232 :
cand = -(F0*(-mp.log(mp.pi)) + W_psi(F, F0, mp.mpf('0.25'), L))/2
print("Validation Frullani sur zeta (entree (0,0), mu=5.5) :")
print(f"  WR (2.32) certifie      = {mp.nstr(WR_232, 10)}")
print(f"  -(1/2)[-F0 log pi + W_psi(1/4)] = {mp.nstr(cand, 10)}")
print(f"  rapport = {mp.nstr(cand/WR_232, 8)}")

# ============ 2. Evaluateur de Lambda(s, chi_3) et premiers zeros ============
# chi_3 : caractere reel impair mod 3 ; L(s,chi3) = 3^(-s) (zeta(s,1/3) - zeta(s,2/3)) ; a=1
def Lchi3(s):
    return 3**(-s)*(mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
def Lam3(t):
    s = mp.mpf('0.5') + 1j*t
    v = (mp.mpf(3)/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)*Lchi3(s)
    return v
# realite sur la droite critique ?
for t in [0, 2, 5]:
    v = Lam3(t)
    print(f"  Lambda(1/2+{t}i, chi3) = {mp.nstr(v, 6)}  (Im/Re = {mp.nstr(abs(mp.im(v))/abs(mp.re(v)),3)})")

# scan de zeros par changements de signe de Re Lambda
t0 = time.time()
zs, step = [], mp.mpf('0.02')
prev = mp.re(Lam3(mp.mpf('0.01')))
t = mp.mpf('0.01')
while t < 140 and len(zs) < 70:
    t2 = t + step
    cur = mp.re(Lam3(t2))
    if prev*cur < 0:
        r = mp.findroot(lambda x: mp.re(Lam3(x)), (t, t2), solver='bisect')
        zs.append(float(r))
    prev, t = cur, t2
pickle.dump(zs, open('zeros_chi3.pkl','wb'))
print(f"\n{len(zs)} zeros de L(s,chi3) jusqu'a t = {zs[-1]:.2f} en {time.time()-t0:.0f}s")
print("premiers :", [f"{z:.4f}" for z in zs[:6]])
