"""More lists YAY."""

__author__ = "730465332"


def only_evens(numeros: list[int]) -> list[int]:
    """Returns only evens."""
    even_steven: list[int] = []
    for numbers in numeros:
        if numbers % 2 == 0:
            even_steven.append(numbers)
    return even_steven


def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns a combination of the lists."""
    combo: list[int] = []
    for numbers in a:
        combo.append(numbers)
    for numbers in b:
        combo.append(numbers)
    return combo


def sub(mist: list[int], a: int, b: int) -> list[int]:
    """Returns a subset of list."""
    subbed: list[int] = []
    if len(mist) == 0:
        return subbed
    if a > len(mist):
        return subbed
    if b < 0:
        return subbed
    if a == len(mist):
        return subbed
    if a < 0:
        subbed.append(mist[0])
    else: 
        subbed.append(mist[a])
    if b > len(mist):
        subbed.append(mist[len(mist) - 1])
    else:
        subbed.append(mist[b - 1])
    return subbed