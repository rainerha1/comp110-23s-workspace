"""Example function for unit tests with range"""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    for idx in range(len(xs)):
        sum_total += xs[idx]
    return sum_total
    



