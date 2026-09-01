# Synthetic Q_Gamma on a rigid unfolding (spacing 2*pi), even window mu=11.
# Test A2: if Delta(ell) is window-only, a zero-free arithmetic-free comb
# should produce the same spacing-vs-level profile.
# Usage: python3 delta_synthetic.py
import time
import mpmath as mp

mp.mp.dps = 35
t0 = time.time()
L = mp.log(11)
NB = 24
om = [2*mp.pi*n/L for n in range(NB+1)]

def hat(n, g):
    if n == 0:
        return 2*mp.sin(g*L/2)/(g*mp.sqrt(L)) if g else mp.sqrt(L)
    return 2*mp.sqrt(2/L)*g*mp.sin(g*L/2)/(g*g - om[n]*om[n])

# rigid comb: gamma_k = (k+1/2)*2*pi, k = 0..K-1  (unfolding of spacing 2pi)
# cut near the Nyquist of the window ~ pi*(NB)/ (L/2) wait: omega_max = 2*pi*NB/L
wmax = float(om[-1])
spacing = 2*mp.pi
K = int(wmax/float(spacing)) + 8
gammas = [(mp.mpf(k)+mp.mpf('0.5'))*spacing for k in range(K)]
print(f'comb K={K} g1={float(gammas[0]):.3f} glast={float(gammas[-1]):.2f} wmax={wmax:.2f}')

N = NB+1
Qz = mp.matrix(N)
for n in range(N):
    for m in range(n, N):
        Qz[n,m] = 2*mp.fsum(hat(n,g)*hat(m,g) for g in gammas)
        Qz[m,n] = Qz[n,m]
E = mp.eigsy(Qz, eigvals_only=True)
pos = [E[i] for i in range(N) if E[i] > mp.mpf('1e-30')]
ell = [float(-mp.log(l)) for l in pos[:8]]
dlt = [ell[i]-ell[i+1] for i in range(min(5,len(ell)-1))]
# wait: ell is decreasing if lambda increasing. We want depth of smallest first.
# eigsy returns ascending eigenvalues, so ell[0] is deepest.
dlt = [ell[i]-ell[i+1] for i in range(min(5,len(ell)-1))]
print('ell', [round(x,2) for x in ell])
print('Delta (deep to shallow, so ell[k]-ell[k+1] is negative if sorted ascending lambda)')
# actually ell[0] largest depth, ell[1] smaller depth: Delta_0 = ell[0]-ell[1] wait
# lambda0 < lambda1 => ell0 > ell1 => spacing at deep end = ell0-ell1
spacings = [ell[i]-ell[i+1] for i in range(min(5,len(ell)-1))]
print('spacings Delta at levels', [(round(ell[i+1],1), round(spacings[i],2)) for i in range(len(spacings))])
print(f'done {time.time()-t0:.0f}s')
