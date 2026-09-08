# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""LMFDB Maass labels for the scanners.

Full label N.k.a.m.d (LMFDB: N.k.a.m.d):
  N     level
  k     weight
  N.a   Conrey character (two numbers, a dot)
  m     spectral index
  d     multiplicity index (1 on this dump)

Short label N.m when k=0, a=1, d=1 (the LMFDB box "Label: 1.2").
So 1.2 → 1.0.1.2.1, character 1.1 — not character 2.1.
2.1 → 2.0.1.1.1, character 2.1 (Conrey N.a at level 2).

User encoding of the prefix: <level>.<weight>.<character q.n>
  1.0.1.1 → 1.0.1.1.1 (m=d=1).

zeros_maass{1..5} are Booker–Then Table 1 = 1.0.1.{1..5}.1,
not lexicographic 1.0.1.10.1 / 1.0.1.100.1. Degree 2. Not Weil.
"""
from __future__ import annotations

ALIAS = {
    "maass1": "1.0.1.1.1",
    "maass2": "1.0.1.2.1",
    "maass3": "1.0.1.3.1",
    "maass4": "1.0.1.4.1",
    "maass5": "1.0.1.5.1",
}

LABEL_TO_SHORT = {lab: name for name, lab in ALIAS.items()}

TABLE1 = {
    "maass1": {"label": "1.0.1.1.1", "R": 9.533695, "g1": 17.0249},
    "maass2": {"label": "1.0.1.2.1", "R": 12.173008, "g1": 5.1055},
    "maass3": {"label": "1.0.1.3.1", "R": 13.779751, "g1": 2.8977},
    "maass4": {"label": "1.0.1.4.1", "R": 14.358510, "g1": 3.7647},
    "maass5": {"label": "1.0.1.5.1", "R": 16.138073, "g1": 4.0704},
}

NOT_TABLE1 = ("1.0.1.10.1", "1.0.1.100.1")


def parse_label(lab: str) -> dict:
    """Split N.k.a.m.d. Character is Conrey N.a (two numbers)."""
    p = lab.strip().split(".")
    if len(p) != 5:
        raise ValueError(f"need N.k.a.m.d, got {lab!r}")
    N, k, a, m, d = p
    chi = f"{N}.{a}"
    short = f"{N}.{m}" if k == "0" and a == "1" and d == "1" else lab
    return {
        "level": int(N),
        "weight": int(k),
        "a": int(a),
        "character": chi,
        "m": int(m),
        "d": int(d),
        "short": short,
        "full": lab,
        "degree": 2,
    }


def is_maass_name(name: str) -> str | None:
    """Full N.k.a.m.d if this is a Maass label (maass1, 1.2, 11.0.1.1.1)."""
    s = name.strip()
    if s in ALIAS:
        return ALIAS[s]
    p = s.split(".")
    if p and all(x.isdigit() for x in p) and len(p) in (2, 4, 5):
        return resolve(s)
    return None


def resolve(name: str) -> str:
    """maass2 | 1.2 | 1.0.1.1 | 1.0.1.2.1 → full N.k.a.m.d."""
    s = name.strip()
    if s in ALIAS:
        return ALIAS[s]
    p = s.split(".")
    if len(p) == 5:
        return s
    if len(p) == 2:
        # short N.m (k=0, a=1, d=1)
        N, m = p
        return f"{N}.0.1.{m}.1"
    if len(p) == 4:
        # <level>.<weight>.<character q.n> → m=d=1
        N, k, q, n = p
        a = n
        return f"{N}.{k}.{a}.1.1"
    return s


def slug(name: str) -> str:
    return resolve(name)


def short_name(label: str) -> str | None:
    return LABEL_TO_SHORT.get(resolve(label))
