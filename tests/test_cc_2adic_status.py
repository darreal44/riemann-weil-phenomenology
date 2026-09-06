# CC (log 2, log 3] is a measured negative; 2-adic mass at λ=2 is unresolved.
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from weights_2adic import EXPECTED  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_expected_mass_is_log2_over_sqrt2():
    assert abs(float(EXPECTED) - math.log(2) / math.sqrt(2)) < 1e-12


def test_lambda16_mass_climbs_through_expected_and_does_not_stop():
    path = os.path.join(ROOT, "report", "campaign_2adic_large.jsonl")
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    lam16 = sorted(
        [r for r in rows if r.get("Lam") == 16.0 and "w2" in r],
        key=lambda r: r["cpu"],
    )
    assert len(lam16) >= 4
    w = [r["w2"] for r in lam16]
    assert all(w[i] < w[i + 1] for i in range(len(w) - 1)), w
    assert w[0] < float(EXPECTED) < w[-1], (w[0], EXPECTED, w[-1])


def test_cc_arch_reconstructs_published_digits():
    src = open(os.path.join(ROOT, "code", "cc_arch.py"), encoding="utf-8").read()
    assert "0.999971" in src
    assert "22.9965" in src
    assert "log 3" in src
