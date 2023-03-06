"""More lists YAY"""

__author__ = "730465332"

def only_evens(numeros: list[int]) -> list[int]:
    """Returns only evens"""
    even_steven: list[int] = []
    for numbers in numeros:
        if numbers % 2 == 0:
            even_steven.append(numbers)
    return even_steven

def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns a combination of the lists"""
    for numbers in b:
        a.append(numbers)
    return a

def sub(mist: list[int], a: int, b: int) -> list[int]:
    """Returns a subset of list"""
    subbed: list[int] = []
    idx1: int = 0
    if len(mist) == 0:
        return subbed
    if a > len(mist):
        return subbed
    if b < 0:
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