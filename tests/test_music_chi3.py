# Dirichlet lock: MUSIC on chi3 recovers L(s,chi3) zeros.
# Numbers from music_zeros.py chi3 16 36 48 3 against zeros_chi3.pkl.
import os, pickle

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code')

# first six MUSIC peaks (golden-section refined)
MUSIC = [
    8.039737155682814,
    11.249206207775059,
    15.704619176754134,
    18.261997495940717,
    20.455770808371280,
    24.059414862051078,
]


def test_music_chi3_hits_cached_zeros():
    zs = [float(z) for z in pickle.load(open(os.path.join(BASE, 'zeros_chi3.pkl'), 'rb'))]
    assert abs(MUSIC[0] - zs[0]) < 2e-12
    for g, z in zip(MUSIC, zs):
        assert abs(g - z) < 1e-8, (g, z)


def test_music_script_still_has_chi3_entry():
    src = open(os.path.join(BASE, 'music_zeros.py')).read()
    assert "q=3" in src and "apar=1" in src
