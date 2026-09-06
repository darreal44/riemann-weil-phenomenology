# Heavy tests — run on the server

The suite is split in two. The light part (~170 tests, ~15 s) runs anywhere:

    python -m pytest tests/ -q --ignore-glob="tests/test_heavy_*" \
      --ignore=tests/test_cert_mu3.py --ignore=tests/test_chi5_mu62.py --ignore=tests/test_chi3_mu80_assembly.py \
      --ignore=tests/test_gl2_eight_curves.py --ignore=tests/test_gl2_quorum_laws.py --ignore=tests/test_gl2_conventions.py \
      --ignore=tests/test_depth_law.py --ignore=tests/test_orphans_wrapped.py \
      --ignore=tests/test_chi3_mu80_judge.py

Requirements on the server: `pip install python-flint` (Arb bindings, used by the two certificate tests;
without it those two tests are skipped with a message, not failed), plus mpmath, numpy, scipy.

The heavy part (eight files, 6–10 minutes total, each recomputing a certificate or a live assembly) is
meant for the server. Run them one file per line so a failure is attributable:

    python -m pytest tests/test_cert_mu3.py            -q --tb=short     # Arb certificate Q(mu=3) PSD, ~72 s
    python -m pytest tests/test_orphans_wrapped.py     -q --tb=short     # mu=11 certificate + Theta endpoints scripts, ~60 s
    python -m pytest tests/test_chi5_mu62.py           -q --tb=short     # live chi5 assembly at mu=62 (Grok), ~25 s
    python -m pytest tests/test_chi3_mu80_assembly.py  -q --tb=short     # chi3 mu=80 Galerkin wall (Grok)
    python -m pytest tests/test_gl2_conventions.py     -q --tb=short     # GL2 prime side vs the 11a1 zero Gram, ~60 s
    python -m pytest tests/test_gl2_eight_curves.py    -q --tb=short     # eight curves, rank detection, ~90 s
    python -m pytest tests/test_gl2_quorum_laws.py     -q --tb=short     # 67a1 quorum 22/38, 32a1 mute prime, d*s law, ~150 s
    python -m pytest tests/test_depth_law.py           -q --tb=short     # discrete Landau count and ell ~ 11 D_max, ~40 s
    python -m pytest tests/test_chi3_mu80_judge.py     -q --tb=short     # chi3 mu=80 scan_s NB=8/24/32 (~20 s)
    python -m pytest tests/test_chi3_assemblies.py     -q --tb=short     # scan_s vs spectro quadrature, cheap window
    python -m pytest tests/test_gl2_37a1_Q_vs_gram.py  -q --tb=short     # 37a1 prime Q vs Gram, not identified
    python -m pytest tests/test_gl2_37a1_drop3.py      -q --tb=short     # 37a1 μ=62 drop 3 (prereg §116), json
    python -m pytest tests/test_gl2_37a1_mu74.py       -q --tb=short     # 37a1 μ=74/80 drop 3 plateau, json

Or all at once (be patient):

    python -m pytest tests/test_cert_mu3.py tests/test_orphans_wrapped.py tests/test_chi5_mu62.py tests/test_chi3_mu80_assembly.py tests/test_gl2_conventions.py tests/test_gl2_eight_curves.py tests/test_gl2_quorum_laws.py tests/test_depth_law.py -q --tb=short --durations=10

Known interaction under investigation: in one full run, test_chi5_mu62 raised a ValueError after other tests had
run, while passing alone and in pairs; tests/conftest.py now resets mpmath precision and GL2_* variables before
each test. If the failure reappears on the server, please paste the --tb=short output.
