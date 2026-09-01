# Endpoint tail coefficient: C = 2 Lambda(mu) / (pi L sqrt(mu)).
# Usage: python3 endpoint_tail.py
import math

def lambda_over_sqrt(mu):
    n = int(mu)
    m, p, lam = n, 2, 0.0
    while p * p <= m:
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        if e:
            lam = math.log(p)
            break
        p += 1
    if m > 1 and lam == 0.0:
        lam = math.log(m)
    return lam / math.sqrt(n)


def C_endpoint(mu):
    L = math.log(mu)
    return (4.0 / L) * lambda_over_sqrt(mu) / (2.0 * math.pi)


if __name__ == '__main__':
    for mu in (9, 11, 13, 16):
        print(f'mu={mu} C={C_endpoint(mu):.4f}  old={lambda_over_sqrt(mu)/4:.4f}')
