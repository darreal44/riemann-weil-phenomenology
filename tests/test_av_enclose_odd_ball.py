import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_enclose_odd_ball as ab

def test_odd_ball_chi3_positive():
    assert ab.main() == 0
