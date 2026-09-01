# The 4.5% is not the 1-cos oscillation (notebook 41).
import math
L = math.log(11.0)
G = 811.18
OSC = abs(math.sin(L * G) / (L * G * G))
FLAT = 1.0 / G


def test_analytic_osc_is_tiny():
    assert OSC / FLAT < 0.001


def test_omega2_term_tiny_on_5x5():
    w4 = 2 * math.pi * 4 / L
    assert (2 * w4 * w4) / (G * G) < 0.001
