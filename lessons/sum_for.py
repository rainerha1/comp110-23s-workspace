"""Example function for unit tests with for loop"""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    for elem in xs:
        sum_total += elem
    return sum_total