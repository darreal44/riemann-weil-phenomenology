from decimal import Decimal
from fractions import Fraction
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'code'))
from certified_bounds import decimal_bound


@pytest.mark.parametrize('x', [-.123456789, -.7745197170626048, 3.582317493e-48, -1e-300, 1e300, 0., 5e-324])
def test_decimal_bound_encloses_exact_binary_value(x):
    assert Fraction(Decimal(decimal_bound(x, 'lower'))) <= Fraction(x)
    assert Fraction(Decimal(decimal_bound(x, 'upper'))) >= Fraction(x)


@pytest.mark.parametrize('x', [float('nan'), float('inf'), float('-inf')])
def test_nonfinite_bound_rejected(x):
    with pytest.raises(ValueError):
        decimal_bound(x, 'upper')
