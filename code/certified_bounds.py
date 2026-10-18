"""Directed conversion of finite binary bounds to printable decimal bounds."""
import math
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR


def decimal_bound(value, direction, digits=7):
    """Round an exact binary64 bound outward to `digits` significant decimals."""
    if direction not in ('lower', 'upper') or digits < 1:
        raise ValueError('direction must be lower/upper and digits positive')
    value = float(value)
    if not math.isfinite(value):
        raise ValueError('finite bound required')
    exact = Decimal.from_float(value)
    with localcontext() as context:
        context.prec = max(digits + 2, len(exact.as_tuple().digits) + 2)
        quantum = Decimal(1).scaleb(exact.adjusted() - digits + 1)
        rounded = exact.quantize(quantum, rounding=ROUND_CEILING if direction == 'upper' else ROUND_FLOOR)
    return format(rounded, '+E')


def arb_float_bound(ball, direction):
    """Outward binary64 conversion, after all ball arithmetic is complete."""
    if direction not in ('lower', 'upper') or not ball.is_finite():
        raise ValueError('finite ball and lower/upper direction required')
    endpoint = ball.lower() if direction == 'lower' else ball.upper()
    return math.nextafter(float(endpoint), -math.inf if direction == 'lower' else math.inf)
