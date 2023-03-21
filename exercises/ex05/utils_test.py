"""Testing my utils functions!"""

__author__ = "730465332"

from exercises.ex05.utils import only_evens, sub, concat


def test_all_evens() -> None:
    """Testing only_evens when given list of all evens(Use Case)."""
    test_list: list[int] = [2, 4, 6, 8]
    assert only_evens(test_list) == [2, 4, 6, 8]


def test_mixed_evens() -> None:
    """Testing only_evens when given list of mixed numbers(Use Case)."""
    test_list: list[int] = [2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]


def test_all_odds() -> None:
    """Testing only_evens when given list of all odds(Edge Case)."""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == []


def test_a_little() -> None:
    """Testing concat when given two lists of few numbers(Use Case)."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [11, 12, 13]
    assert concat(test_list1, test_list2) == [1, 2, 3, 11, 12, 13]


def test_a_lot() -> None:
    """Testing concat when given two lists of several numbers(Use Case)."""
    test_list1: list[int] = [1, 2, 3, 4, 5, 6]
    test_list2: list[int] = [11, 12, 13, 14, 15, 16]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16]


def test_none() -> None:
    """Testing concat when given two empty lists(Edge Case)."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_smalls() -> None:
    """Testing sub when given a list of small numbers and two integers that are valid indices(Use Case)."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    test_int1: int = 2
    test_int2: int = 5
    assert sub(test_list, test_int1, test_int2) == [3, 5]


def test_bigs() -> None:
    """Testing sub when given a list of big numbers and two integers that are valid indices(Use Case)."""
    test_list: list[int] = [1000, 2000, 3000, 4000, 5000, 6000]
    test_int1: int = 1
    test_int2: int = 4
    assert sub(test_list, test_int1, test_int2) == [2000, 4000]


def test_huhhh() -> None:
    """Testing sub when given a list of numbers and two integers that are invalid indices(Edge Case)."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    test_int1: int = -10
    test_int2: int = 100
    assert sub(test_list, test_int1, test_int2) == [1, 6]