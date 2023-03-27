"""Dictonary Utilities Unit Tests."""

__author__ = "730465332"

from exercises.ex07.dictionary import count, favorite_color, invert

def test_count():
    # Test 1: Basic functionality with a list of fruit
    items1 = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    assert count(items1) == {'apple': 2, 'banana': 3, 'orange': 1}


def test_count2():
    # Test 2: Case sensitivity with a list of colors
    items2 = ['red', 'green', 'Blue', 'blue', 'RED', 'GREEN']
    assert count(items2) == {'red': 2, 'green': 2, 'Blue': 1, 'blue': 1, 'RED': 1, 'GREEN': 1}


def test_count3():
    # Test 3: Edge case with an empty list
    items3 = []
    assert count(items3) == {}


def test_invert():
    # Test 1: Basic functionality with a dictionary of fruit
    d1 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
    assert invert(d1) == {'apple': 'a', 'banana': 'b', 'cherry': 'c'}


def test_invert2():
    # Test 2: Case sensitivity with a dictionary of colors
    d2 = {'red': 'R', 'green': 'g', 'blue': 'B', 'Orange': 'o'}
    assert invert(d2) == {'R': 'red', 'g': 'green', 'B': 'blue', 'o': 'Orange'}


def test_invert3():
    # Test 3: Edge case with a dictionary with multiple keys pointing to the same value
    d3 = {'a': 'apple', 'b': 'banana', 'c': 'apple'}
    try:
        invert(d3)
    except KeyError as e:
        assert str(e) == "Value apple appears multiple times in the input dictionary."


def test_favorite_color():
    # Test 1: Basic functionality with a dictionary of names and favorite colors
    d1 = {'Alice': 'blue', 'Bob': 'red', 'Charlie': 'blue', 'David': 'green'}
    assert favorite_color(d1) == 'blue'


def test_favorite_color2():
    # Test 2: Case sensitivity with a dictionary of names and favorite colors
    d2 = {'Alice': 'Blue', 'Bob': 'red', 'Charlie': 'blue', 'David': 'Green'}
    assert favorite_color(d2) == 'Blue'


def test_favorite_color3():
    # Test 3: Edge case with an empty dictionary
    d3 = {}
    try:
        favorite_color(d3)
    except ValueError as e:
        assert str(e) == "Input dictionary cannot be empty."