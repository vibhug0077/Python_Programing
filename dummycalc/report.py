"""Example module showing relative imports inside a package."""

from .advanced import square_root
from .basic import add, multiply


def quick_report(a, b):
    total = add(a, b)
    product = multiply(a, b)
    return {
        "a": a,
        "b": b,
        "sum": total,
        "product": product,
        "sqrt_of_sum": square_root(total) if total >= 0 else None,
    }
