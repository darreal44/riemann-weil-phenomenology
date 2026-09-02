import mpmath as mp, pickle, time, importlib.util, os, sys
t0 = time.time(); mp.mp.dps = 15
spec = importlib.util.spec_from_file_location("kr", "/home/claude/push/remote/code/kronecker.py"); kr = importlib.util.module_from_spec(spec); spec.loader.exec_module(kr)
chars = {'chi19': (-19, 19), 'chi24e': (24, 24), 'chi24o': (-24, 24), 'chi23': (-23, 23)}
name = sys.argv[1]; budget = float(sys.argv[2]); d, q = chars[name]; phi = (5**0.5-1)/2
tab = kr.chi_tab(d, q)
def a2(t):
    s = mp.mpf('0.5')+1j*mp.mpf(t); v = q**(-s)*mp.fsum(tab[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if tab[r]); return float(mp.re(v)**2+mp.im(v)**2)
out = f'zeros_{name}_150.pkl'
Z = sorted(float(str(x)) for x in pickle.load(open(out if os.path.exists(out) else f'zeros_{name}.pkl','rb')))
start = Z[-1]; t = start+0.35; h = 0.35; p2 = a2(t-h); p1 = a2(t)
print(f"{name}: reprise a {start:.1f} ({len(Z)} zeros)", flush=True)
while t < 150 and time.time()-t0 < budget:
    c = a2(t+h)
    if p1 < p2 and p1 < c:
        a, b = t-h, t+h
        for _ in range(26):
            c1, c2 = b-phi*(b-a), a+phi*(b-a)
            if a2(c1) < a2(c2): b = c2
            else: a = c1
        zm = (a+b)/2
        if a2(zm) < 1e-5:
            Z.append(zm); pickle.dump(sorted(set(Z)), open(out,'wb'))
    p2, p1 = p1, c; t += h
print(f"   -> {len(Z)} zeros (max {max(Z):.1f}) {'FINI' if t >= 150 else 'partiel'}   [{time.time()-t0:.0f}s]", flush=True)
