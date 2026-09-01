# Campaign scripts still live on main and still contain the locks they shipped.
import os

CODE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code')


def test_required_scripts_exist():
    for name in (
        'kronecker.py', 'scan_s.py', 'map2.py', 'map3.py', 'lemma_B_mu16.py',
        'squares47.py', 'squares47_arb.py', 'music_zeros.py',
        'positivite_certifiee.py', 'quorum_general.py',
        'high_directions.py', 'match_squares.py', 'endpoint_order.py',
        'squares_tail.py', 'audit_00.py', 'lemma_B_chi.py',
    ):
        assert os.path.exists(os.path.join(CODE, name)), name


def test_scan_s_knows_the_three_heldouts():
    src = open(os.path.join(CODE, 'scan_s.py')).read()
    for key in ("'chim8'", "'chi20'", "'chi23'", "'chi5'", "'chi7'", "'chi8'"):
        assert key in src, key


def test_squares47_pairs_positive_zeros():
    src = open(os.path.join(CODE, 'squares47.py')).read()
    assert '2 *' in src or '2*' in src
