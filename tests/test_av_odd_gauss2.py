# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_odd_gauss2 as g2

def test_composite_chi3_positive():
    assert g2.main() == 0
    assert g2.C2_HALF > 0
