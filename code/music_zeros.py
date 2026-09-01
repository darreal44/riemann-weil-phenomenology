# MUSIC sur la forme de Weil : les zeros emergent du radical (rapport §16).
# Le radical est un sous-espace de bruit rigoureux : Q(v)=lambda => |v^(gamma_k)| <= sqrt(lambda/2).
# CRITERE D'ADMISSION : n'inclure dans le bruit que des barreaux a lambda petit (le vecteur
# a lambda=0.12 admis a tort decale tous les pics de +8 — rapport §16.2).
# Loi de precision mesuree : erreur(gamma_1) ~ e^(-s(chi)*mu) — pleine profondeur (§16.3),
# grace a l'HYPER-NULLITE : la masse lambda est refoulee aux zeros de la frontiere de bande.
# Usage : python3 music_zeros.py zeta 11 46 50 6      (fonction, mu, NB, dps, d_bruit)
#         python3 music_zeros.py chi3 11 40 45 2
import sys, time, numpy as np
import mpmath as mp

def run(kind, mu, NB, dps, d):
    t0 = time.time(); mp.mp.dps = dps
    src = open(__file__.replace('music_zeros.py', 'spectro.py')).read()
    src = src.replace("    E, V = mp.eigsy(S)", "    import __main__; __main__.SCAP = S; E, V = mp.eigsy(S)")
    ns = {}
    exec(compile(src.replace("if __name__ == '__main__':", "if False:"), "sc", "exec"), ns)
    if kind == 'zeta':
        ns['run'](mp.mpf(mu), NB, dps, 12, K=1)
    else:
        ns['run'](mp.mpf(mu), NB, dps, 12, K=1, q=3, tab=[0,1,-1], apar=1)
    import __main__
    S = __main__.SCAP
    E, V = mp.eigsy(S)
    NP = NB+1; L = mp.log(mu); om = [2*mp.pi*n/L for n in range(NP)]
    print(f"[{time.time()-t0:.0f}s] barreaux du bruit : {[mp.nstr(E[k],2) for k in range(d)]}")
    radf = np.array([[float(V[i,k]) for i in range(NP)] for k in range(d)])
    Lf = float(L); omf = np.array([float(o) for o in om])
    def chat_f(g):
        v = np.empty(NP); s = np.sin(g*Lf/2)
        v[0] = 2*s/(g*np.sqrt(Lf)); v[1:] = np.sqrt(2/Lf)*s*2*g/(g*g - omf[1:]**2)
        return v
    gmax = float(om[NP-1])*1.02
    gs = np.arange(1.0, gmax, 0.005)
    mus = np.empty(len(gs))
    for i, g in enumerate(gs):
        c = chat_f(g); pr = radf.dot(c)
        mus[i] = c.dot(c)/(pr.dot(pr) + 1e-300)
    peaks = [gs[i] for i in range(1,len(gs)-1) if mus[i]>mus[i-1] and mus[i]>mus[i+1] and mus[i]>1e6]
    print(f"pics MUSIC : {len(peaks)}")
    phi = (mp.sqrt(5)-1)/2
    def obj(g):
        c = mp.matrix([2*mp.sin(g*L/2)/(g*mp.sqrt(L))] + [mp.sqrt(2/L)*mp.sin(g*L/2)*2*g/(g*g-om[n]*om[n]) for n in range(1,NP)])
        return mp.fsum(mp.fsum(V[i,k]*c[i] for i in range(NP))**2 for k in range(min(d,3)))
    for k, p in enumerate(peaks[:12], 1):
        a, b = mp.mpf(p-0.02), mp.mpf(p+0.02)
        for _ in range(90):
            c1, c2 = b-phi*(b-a), a+phi*(b-a)
            if obj(c1) < obj(c2): b = c2
            else: a = c1
        print(f"  zero {k:2d} : gamma = {mp.nstr((a+b)/2, 22)}")

if __name__ == '__main__':
    run(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
