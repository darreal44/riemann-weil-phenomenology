# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Replay the finite mu=11 quorum mechanism with the full cross term.

Q_S = Q + T_M. For an arbitrary frozen vector v, the off-diagonal of
the orthonormal compression is kappa + u^T Q v, not just kappa.
We avoid normalization: w = T_M v - (v^T T_M v)/(v^T v) v, and evaluate
det([[v^T Q_S v, v^T Q_S w], [w^T Q_S v, w^T Q_S w]]) in Arb.
A strictly negative determinant proves indefiniteness on V_46 only.

    python code/quorum_2x2.py
    python code/quorum_2x2.py --output report/quorum-2x2-mu11.json
"""
import argparse
import itertools
import json
import time
from pathlib import Path

from flint import arb, ctx


def compression_certificate(Q, T, v):
    """Certify a symmetric real compression, retaining the eigenvector residual.

    Inputs are square lists of Arb balls enclosing symmetric Q and T, and
    a vector enclosing v. The verdict is false for an inconclusive ball.
    """
    n = len(v)
    if not n or any(len(M) != n or any(len(row) != n for row in M) for M in (Q, T)):
        raise ValueError('matrix/vector dimensions do not match')
    if not all(x.is_finite() for M in (Q, T) for row in M for x in row) or not all(x.is_finite() for x in v):
        raise ValueError('finite input balls required')
    if any(M[i][j].mid() != M[j][i].mid() or M[i][j].rad() != M[j][i].rad()
           for M in (Q, T) for i in range(n) for j in range(i)):
        raise ValueError('symmetric matrices with identical mirrored enclosures required')
    def dot(x, y):
        return sum((a*b for a, b in zip(x, y)), arb(0))
    def matvec(M, x):
        return [dot(row, x) for row in M]
    norm_v = dot(v, v)
    if not norm_v > 0:
        raise ValueError('the vector norm must be strictly positive')
    Tv = matvec(T, v)
    projection = dot(v, Tv) / norm_v
    w = [Tv[i] - projection*v[i] for i in range(n)]
    S = [[Q[i][j] + T[i][j] for j in range(n)] for i in range(n)]
    Sv, Sw = matvec(S, v), matvec(S, w)
    a, cross, d = dot(v, Sv), dot(v, Sw), dot(w, Sw)
    determinant = a*d - cross*cross
    norm_w = dot(w, w)
    normalized = determinant / (norm_v * norm_w) if norm_w > 0 else None
    Qv = matvec(Q, v)
    residual_cross = dot(w, Qv)
    eigenvalue = dot(v, Qv) / norm_v
    residual = [Qv[i] - eigenvalue*v[i] for i in range(n)]
    # Independent interval products x*x can cross zero and make sqrt NaN.
    # Bound the Euclidean norm from above using absolute endpoint bounds.
    residual_norm_upper = (sum((abs(x).upper()**2 for x in residual), arb(0))
                           / norm_v.lower()).sqrt().upper()
    kappa = (norm_w / norm_v).sqrt() if norm_w > 0 else None
    r = residual_cross / (norm_w * norm_v).sqrt() if norm_w > 0 else None
    budget = None
    if r is not None:
        # |kappa+r| >= max(0, lower(kappa)-upper(|r|)).
        cross_lower = max(arb(0), kappa.lower() - abs(r).upper())
        budget = (a*d/(norm_v*norm_w) - cross_lower**2).upper()
    return {'determinant': determinant, 'cross': cross,
            'residual_cross': residual_cross, 'residual_normalized': r,
            'eigen_residual_norm_upper': residual_norm_upper, 'kappa': kappa,
            'residual_budget_upper': budget,
            'normalized_determinant': normalized,
            'indefinite': determinant.is_finite() and determinant < 0}


def tower_matrices(mu, NB, primes):
    """Missing-prime terms T_p; their positive weights do not imply PSD."""
    L = arb(mu).log()
    omega = [2*arb.pi()*n/L for n in range(NB+1)]
    def theta(n, m, y):
        if n == m == 0:
            return 2*(L-y)/L
        if n == 0 or m == 0:
            j = max(n, m)
            return -2*(omega[j]*y).sin()/(arb(2).sqrt()*arb.pi()*j)
        if n == m:
            return 2*((L-y)*(omega[n]*y).cos()/L - (omega[n]*y).sin()/(2*arb.pi()*n))
        return 2*(n*(omega[n]*y).sin()-m*(omega[m]*y).sin())/(arb.pi()*(m*m-n*n))
    matrices = {}
    for p in primes:
        terms = []
        pk = p
        while pk < mu:
            terms.append((arb(pk).log(), arb(p).log()/arb(pk).sqrt()))
            pk *= p
        M = [[arb(0) for _ in range(NB+1)] for _ in range(NB+1)]
        for n in range(NB+1):
            for m in range(n, NB+1):
                M[n][m] = M[m][n] = sum((weight*theta(n, m, y) for y, weight in terms), arb(0))
        matrices[p] = M
    return matrices


def replay(output=None):
    from quorum_full_pd import build, g, arb_from_dyadic, MU, NB, DPS, EPS, WIT
    start = time.time()
    ctx.dps = DPS
    with open(WIT, encoding='utf-8') as f:
        frozen = json.load(f)
    if (frozen.get('kind'), frozen.get('mu'), frozen.get('NB')) != ('zeta', MU, NB):
        raise ValueError('frozen vector metadata do not match the published window')
    v = [arb_from_dyadic(s) for s in frozen['v1_dyadic']]
    if len(v) != NB + 1:
        raise ValueError('incorrect frozen vector dimension')
    packed, n, _ = build(MU, NB, DPS, EPS)
    Q = [[g(packed, i, j) for j in range(n)] for i in range(n)]
    primes = (2, 3, 5, 7)
    towers = tower_matrices(MU, NB, primes)
    rows = []
    for r in range(1, len(primes)+1):
        for missing in itertools.combinations(primes, r):
            T = [[sum((towers[p][i][j] for p in missing), arb(0)) for j in range(n)] for i in range(n)]
            result = compression_certificate(Q, T, v)
            row = {'missing': list(missing), 'indefinite': bool(result['indefinite'])}
            row.update({key: str(value) if value is not None else None
                        for key, value in result.items() if key != 'indefinite'})
            rows.append(row)
            print(f'M={missing}: determinant={result["normalized_determinant"]} certified={row["indefinite"]}', flush=True)
    report = {'kind': 'zeta', 'mu': MU, 'NB': NB, 'dps': DPS, 'eps': EPS,
              'space': 'V_46 (47 cosine modes)', 'exact_eigenvector_assumed': False,
              'witness': Path(WIT).name, 'rows': rows,
              'certified': all(row['indefinite'] for row in rows)}
    if output:
        Path(output).write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    if not report['certified']:
        raise ValueError('2x2 certification incomplete')
    print(f'CERTIFIED: 15/15 proper sub-products on V_46; full cross term; {time.time()-start:.0f}s')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', help='optional JSON certificate path')
    replay(parser.parse_args().output)
