import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_enclose_odd as ao

def test_odd_point_positive():
    assert ao.main() == 0
