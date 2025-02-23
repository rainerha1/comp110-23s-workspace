"""First exercise using lists."""

__author__ = "730465332"


def all(a: list[int], b: int) -> bool:
    """Tests if all members in list are the integer."""
    if len(a) == 0:
        return False
    idx: int = 0
    while idx <= len(a) - 1:
        if a[idx] != b:
            return False
        else:
            idx += 1
    return True


def max(a: list[int]) -> int:
    """Finds maximum number in list."""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    big: int = a[0]
    while idx <= len(a) - 1:
        if big > a[idx]:
            big = big
        else:
            big = a[idx]
        idx += 1
    return big


def is_equal(a: list[int], b: list[int]) -> bool:
    """Tests if two lists are equal."""
    if a == b:
        return True
    else:
        return False