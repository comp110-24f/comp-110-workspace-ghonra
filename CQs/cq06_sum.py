"""Summing the elements of a list using different loops"""

__author__ = 730649788


def w_sum(vals: list[float]) -> float:
    total = 0.0
    idx = 0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    total = 0.0
    for values in vals:
        total += values
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for values in range(0, len(vals)):
        total += vals[values]
    return total


result = f_range_sum([1.1, 0.9, 1.0])
print(result)
