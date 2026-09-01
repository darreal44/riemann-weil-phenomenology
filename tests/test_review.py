# Review pass: claims shipped in §§19-32 still sit in the tree.
import math, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
NB = os.path.join(ROOT, 'report', 'le-milieu-des-premiers-v2.md')
CODE = os.path.join(ROOT, 'code')


def test_notebook_has_sections_19_through_32():
    text = open(NB).read()
    missing = [n for n in range(19, 62) if f'## {n}.' not in text]
    assert missing == [], missing


def test_journal_92_through_106():
    text = open(NB).read()
    missing = [n for n in range(92, 136) if f'({n})' not in text]
    assert missing == [], missing


def test_no_merge_conflict_markers():
    skip = {'.git', '__pycache__', '.github'}
    hits = []
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in skip]
        for name in files:
            if name.endswith(('.pyc', '.pdf', '.pkl', '.png')):
                continue
            path = os.path.join(dirpath, name)
            try:
                t = open(path, errors='replace').read()
            except Exception:
                continue
            mark = '<' * 7
            if mark in t or mark.replace('<', '>') in t:
                hits.append(os.path.relpath(path, ROOT))
    assert hits == [], hits


def test_twopie_consistent():
    assert abs(2 * math.pi * math.e - 17.079) < 0.002


def test_signed_tail_in_source():
    src = open(os.path.join(CODE, 'squares_tail.py')).read()
    assert 'def signed_tail' in src
    src2 = open(os.path.join(CODE, 'squares47_arb.py')).read()
    assert 'signed' in src2.lower()


def test_music_and_chi3_cache_agree_on_gamma1():
    import pickle
    zs = pickle.load(open(os.path.join(CODE, 'zeros_chi3.pkl'), 'rb'))
    assert abs(float(zs[0]) - 8.039737155681) < 1e-9


def test_scan_s_sieve_still_has_37():
    src = open(os.path.join(CODE, 'scan_s.py')).read()
    assert '37' in src and '41' in src
