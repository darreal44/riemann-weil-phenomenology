import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_odd_gauss2 as g2

def test_composite_chi3_positive():
    assert g2.main() == 0
    assert g2.C2_HALF > 0
