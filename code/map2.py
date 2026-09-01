# Two-variable (and stripped) maps for s(chi), trained on the published
# uniformized table, tested on the three held-out characters.
# Usage: python3 map2.py
import math

# name, odd, g1, gap, D, s   -- depth-note table, chi15 dropped (rising)
TRAIN = [
    ('24o', 1, 1.977, 2.746, 3.174, 0.46),
    ('24e', 0, 2.689, 2.604, 3.174, 0.50),
    ('19',  1, 1.516, 3.961, 0.876, 0.58),
    ('21',  0, 2.315, 3.465, 2.683, 0.58),
    ('17',  0, 3.728, 1.907, 0.907, 0.71),
    ('13',  0, 3.119, 4.112, 0.984, 0.95),
    ('12',  0, 3.805, 2.888, 3.174, 1.01),
    ('11',  1, 2.477, 4.323, 1.035, 1.07),
    ('8',   0, 4.900, 2.728, 1.673, 1.53),
    ('7',   1, 4.476, 2.370, 1.183, 1.70),
    ('5',   0, 6.648, 3.183, 1.302, 2.47),
    ('4',   1, 6.021, 4.223, 1.673, 3.04),
    ('3',   1, 8.040, 3.209, 1.501, 4.00),
]
# held-out: (name, odd, g1, gap, D, s_claude_uniform, s_our_last_segment)
HOLD = [
    ('-8',  1, 3.576155, 3.858, 1.673, 1.30, 1.46),
    ('-20', 1, 2.358935, 2.317, 2.975, 0.68, 0.55),
    ('-23', 1, 2.871340, 1.344, 0.826, 0.54, 0.47),
]


def lstsq(X, y):
    n, k = len(X), len(X[0])
    A = [[0.0] * k for _ in range(k)]
    b = [0.0] * k
    for i in range(n):
        for p in range(k):
            b[p] += X[i][p] * y[i]
            for q in range(k):
                A[p][q] += X[i][p] * X[i][q]
    M = [A[i] + [b[i]] for i in range(k)]
    for i in range(k):
        piv = max(range(i, k), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        f = M[i][i]
        for q in range(i, k + 1):
            M[i][q] /= f
        for r in range(k):
            if r == i:
                continue
            f = M[r][i]
            for q in range(i, k + 1):
                M[r][q] -= f * M[i][q]
    return [M[i][k] for i in range(k)]


def fit_logs(rows, cols):
    X, y = [], []
    for r in rows:
        X.append([1.0] + [math.log(f(r)) for f in cols])
        y.append(math.log(r[-1]))
    return lstsq(X, y)


def hat_of(c, r, cols):
    return math.exp(c[0] + sum(c[i + 1] * math.log(f(r)) for i, f in enumerate(cols)))


g1 = lambda r: r[2]
gap = lambda r: r[3]
D = lambda r: r[4]


def dump(title, cols, rows=TRAIN):
    c = fit_logs(rows, cols)
    print(f'\n== {title} ==')
    print('coeff', [round(x, 3) for x in c])
    se = 0.0
    for r in rows:
        h = hat_of(c, r, cols)
        se += (math.log(h) - math.log(r[-1])) ** 2
        print(f'  {r[0]:4s} s={r[-1]:.2f} hat={h:.2f} {100*(h/r[-1]-1):+5.1f}%')
    print(f'  train rms {100*(math.exp(math.sqrt(se/len(rows)))-1):.1f}%')
    print('  HELD')
    for name, odd, g, gp, d, sc, so in HOLD:
        row = (name, odd, g, gp, d, sc)
        h = hat_of(c, row, cols)
        print(f'  {name:4s} hat={h:.2f}  claude={sc:.2f} ({100*(h/sc-1):+.0f}%)  '
              f'ours={so:.2f} ({100*(h/so-1):+.0f}%)')
    return c


if __name__ == '__main__':
    # 2-var as proposed: log s = a + b log g1 + c * odd
    X, y = [], []
    for r in TRAIN:
        X.append([1.0, math.log(r[2]), float(r[1])])
        y.append(math.log(r[-1]))
    c = lstsq(X, y)
    print('== g1 + parity (the candidate) ==')
    print(f's = {math.exp(c[0]):.3f} * g1^{c[1]:.3f} * {math.exp(c[2]):.3f}^[odd]')
    for name, odd, g, gp, d, sc, so in HOLD:
        h = math.exp(c[0] + c[1] * math.log(g) + c[2] * odd)
        print(f'  {name:4s} hat={h:.2f}  claude={sc:.2f} ({100*(h/sc-1):+.0f}%)  '
              f'ours={so:.2f} ({100*(h/so-1):+.0f}%)')
    dump('g1 + gap + D (no parity)', [g1, gap, D])
    print('\nchi-23 is odd but sits on the even locus (g1=2.87 ~ 24e/21).')
    print('Parity is the axis that kills. Dropping it saves the hold-out')
    print('that killed the published 4-var map — not a new trained map.')
