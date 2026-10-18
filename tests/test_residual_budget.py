import sys
from pathlib import Path
from flint import arb
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
from quorum_2x2 import compression_certificate


def test_residual_can_change_sufficient_budget_without_changing_exact_compression():
    Q = [[arb(1), arb(1)], [arb(1), arb(2)]]
    T = [[arb(0), arb(2)], [arb(2), arb(0)]]
    result = compression_certificate(Q, T, [arb(1), arb(0)])
    assert result['normalized_determinant'].contains(-7)
    assert result['kappa'].contains(2)
    assert result['residual_normalized'].contains(1)
    assert result['eigen_residual_norm_upper'] >= 1
    assert result['residual_budget_upper'] >= 1
    assert result['indefinite']


def test_nonsymmetric_matrix_cannot_be_certified():
    Q = [[arb(1), arb(10)], [arb(-10), arb(1)]]
    T = [[arb(0), arb(1)], [arb(1), arb(0)]]
    with pytest.raises(ValueError, match='symmetric'):
        compression_certificate(Q, T, [arb(1), arb(0)])


def test_residual_norm_stays_finite_when_residual_ball_contains_zero():
    off = arb(0, '1e-30')
    Q = [[arb(1, '1e-30'), off], [off, arb(2)]]
    T = [[arb(0), arb(2)], [arb(2), arb(0)]]
    result = compression_certificate(Q, T, [arb(1), arb(0)])
    assert result['eigen_residual_norm_upper'].is_finite()
    assert result['eigen_residual_norm_upper'] > 0
