# Successor map: log s = a + b log g1 + c log gap + d log D.
# No parity. Fit on TRAIN, LOO, then three held-out characters.
# Usage: python3 map3.py
import math
import map2

TRAIN = map2.TRAIN
HOLD = map2.HOLD
g1, gap, D = map2.g1, map2.gap, map2.D
COLS = [g1, gap, D]


def rms(rows, c):
    se = 0.0
    for r in rows:
        h = map2.hat_of(c, r, COLS)
        se += (math.log(h) - math.log(r[-1])) ** 2
    return 100 * (math.exp(math.sqrt(se / len(rows))) - 1)


def main():
    c = map2.fit_logs(TRAIN, COLS)
    print('s = {:.3f} * g1^{:.3f} * gap^{:.3f} * D^{:.3f}'.format(
        math.exp(c[0]), c[1], c[2], c[3]))
    print('train rms {:.1f}%'.format(rms(TRAIN, c)))
    print('LOO')
    errs = []
    for i, r in enumerate(TRAIN):
        c_loo = map2.fit_logs(TRAIN[:i] + TRAIN[i + 1 :], COLS)
        h = map2.hat_of(c_loo, r, COLS)
        e = h / r[-1] - 1
        errs.append(e)
        print(f'  {r[0]:4s} s={r[-1]:.2f} hat={h:.2f} {100*e:+5.1f}%')
    print('  LOO rms {:.1f}%'.format(
        100 * (math.exp(math.sqrt(sum(math.log(1 + e) ** 2 for e in errs) / len(errs))) - 1)
        if all(e > -0.9 for e in errs) else float('nan')))
    print('HELD (true OOS, coefficients frozen)')
    for name, odd, g, gp, d, sc, so in HOLD:
        row = (name, odd, g, gp, d, so)
        h = map2.hat_of(c, row, COLS)
        print(f'  {name:4s} hat={h:.2f}  ours={so:.2f} ({100*(h/so-1):+.1f}%)  '
              f'claude={sc:.2f} ({100*(h/sc-1):+.1f}%)')


if __name__ == '__main__':
    main()
