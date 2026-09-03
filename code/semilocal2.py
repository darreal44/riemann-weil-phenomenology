# Operateur P1 F P1 sur la tranche en base de cellules, avec MOYENNE EXACTE sur les cellules (Si),
# pas d'evaluation au point milieu : tue le repliement des termes lacunaires.
import numpy as np
from scipy.special import sici
def Si(x): return sici(x)[0]
def avg_Fab(a, b, c, d, scale):
    # (1/(d-c)) int_c^d F_ab(scale*rho) drho, F_ab(xi) = [sin(2pi b xi) - sin(2pi a xi)]/(pi xi)
    # = (1/(d-c)) (1/(scale*pi)) [ Si(2pi b s xi) - Si(2pi a s xi) ]_{xi=c}^{d}   (s = scale)
    def G(x): return (Si(2*np.pi*b*scale*x) - Si(2*np.pi*a*scale*x))/(np.pi*scale)
    return (G(d) - G(c))/(d - c)
def build_exact(N, semilocal=True, NN=40):
    h = 1.0/N; e = np.linspace(0, 1, N+1)
    A = np.empty((N, N))
    for j in range(N):
        a, b = e[j], e[j+1]
        for i in range(N):
            c, d = e[i], e[i+1]
            if not semilocal:
                A[i, j] = avg_Fab(a, b, c, d, 1.0)
            else:
                s = -avg_Fab(a, b, c, d, 0.5)
                for n in range(NN): s += avg_Fab(a, b, c, d, 2.0**n)
                A[i, j] = 0.5*s
    return A, h
if __name__ == '__main__':
    for sl, name in [(False, 'archimedien'), (True, 'semi-local {inf,2}')]:
        for N in (200, 400):
            A, h = build_exact(N, sl)
            asym = np.abs(A-A.T).max()/np.abs(A).max()
            ev = np.linalg.eigvalsh(0.5*(A+A.T)); ev = ev[np.argsort(-np.abs(ev))]
            print(f"[{name}] N={N}: asymetrie {asym:.2e} ; sum lambda^2 = {np.sum(ev**2):.4f} ; |lambda| : {np.round(ev[:8],5)}")
