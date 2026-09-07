# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_enclose_chi8 as ae8

def test_chi8_Q_positive():
    assert ae8.main() == 0
    assert ae8.p8() < 0
    assert ae8.cst8() > 0
