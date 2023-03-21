"""Challenge Question 4."""

def zip(x: list[str], y: list[int]) -> dict[str,int]:
    z: dict[str,int] = {}
    if len(x) != len(y):
        return z
    if len(x) == 0:
        return z
    if len(y) == 0:
        return z
    idx: int = 0
    while idx < len(x):
        z[x[idx]] = y[idx]
        idx += 1
    return z