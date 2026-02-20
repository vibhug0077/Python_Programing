"""Advanced calculator operations using the math module."""

import math


def power(base, exp):
    return math.pow(base, exp)


def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if int(n) != n:
        raise ValueError("Factorial requires an integer input.")
    return math.factorial(int(n))
