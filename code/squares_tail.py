# Explicit tail bound for Q^z - Q^z_cut on the even window at mu=11.
# hat(eta_0)(g) = 2 sin(g L/2) / (g sqrt(L))  <= 2/(g sqrt(L))
# hat(eta_n)(g) = 2 sqrt(2/L) g sin(g L/2) / (g^2 - w_n^2)
# For g > 2 w_max, |hat_n(g)| <= 4 / (g sqrt(L))  (uniform in n <= N0).
# Density of zeros <= (1/2pi) log(g/2pi) + 1  (explicit Riemann-von Mangoldt envelope).
# Usage: python3 squares_tail.py [Gcut] [N0]
import sys, math
Gcut = float(sys.argv[1]) if len(sys.argv) > 1 else 513.7
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 4
L = math.log(11)
wmax = 2*math.pi*N0/L
c = 4.0 / math.sqrt(L)   # uniform |hat| bound for g > 2 wmax

def rv_density(g):
    return max(0.0, math.log(g/(2*math.pi))/(2*math.pi) + 1.0)

# integral_{Gcut}^infty 2 * (c/g)^2 * density(g) dg   (factor 2 for +/- gamma)
# <= 2 c^2 integral_G^infty (log(g/2pi)/(2pi) + 1) / g^2 dg
def tail_diag(G):
    # int_G^infty log(g/2pi)/g^2 dg = (log(G/2pi)+1)/G
    # int_G^infty 1/g^2 dg = 1/G
    if G <= 2*wmax:
        return float('inf')
    lg = math.log(G/(2*math.pi))
    integ = (lg + 1)/(2*math.pi) / G + 1.0/G
    return 2 * (c**2) * integ

def signed_tail(G, which='nm'):
    """Entry-dependent leading 1/g^2 tail.
    2 hat0 hat0 ~ (4/L)(1-cos)/g^2
    2 hat0 hatn ~ (4 sqrt(2)/L)(1-cos)/g^2
    2 hatn hatm ~ (8/L)(1-cos)/g^2
    """
    if G <= 2 * wmax:
        return float('inf')
    pref = {'00': 4.0/L, '0n': 4.0*math.sqrt(2)/L, 'nm': 8.0/L}[which]
    avg = 1.0 / G
    osc = abs(math.sin(L * G) / (L * G))
    return pref * (avg + osc)

td = tail_diag(Gcut)
sd = signed_tail(Gcut)
print(f'N0={N0} wmax={wmax:.1f} Gcut={Gcut:.1f}')
print(f'uniform |hat| bound c/g with c={c:.3f}')
print(f'unsigned tail (density envelope): {td:.4e}')
print(f'signed tail   (1-cos oscillation): {sd:.4e}')
print(f'ratio unsigned/signed = {td/sd:.1f}')
print(f'compare to measured mid |Qpr-Qz_cut| ~ 2e-3-4e-3 at N0=4')
for G in (280, 513.7, 811.2, 2000):
    print(f'  G={G:<8} unsigned={tail_diag(G):.4e}  signed={signed_tail(G):.4e}')
