import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_enclose_even as ae

def test_all_even_Q_positive():
    assert ae.main() == 0
