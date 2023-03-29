"""Ünit tests"""

def sumoo(xs: list[float]) -> float:
    """return sum of all xs"""
    sum_total: float = 0.0
    idx: int = 0
    while idx <= len(xs) - 1:
        sum_total += xs[idx]
        idx += 1
    return sum_total

def sum(xs: list[float]) -> float:
    """return sum of all xs"""
    sum_total: float = 0.0
    for jaundice in xs:
        sum_total += jaundice
    return sum_total

x: str = "26"
int()