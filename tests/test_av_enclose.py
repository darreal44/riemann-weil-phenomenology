"""Judge for the flint-free A(v) enclosure."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))
import av_enclose as ae


def test_A_ball_inside_window():
    assert ae.main() == 0
