"""Dictonary Utilities."""

__author__ = "730465332"


def invert(d: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            raise KeyError("Values must be unique")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    counts = {}
    for name in colors:
        color = colors[name]
        if color in counts:
            counts[color] += 1
        else:
            counts[color] = 1
    most_common_color = None
    most_common_count = 0
    for color in counts:
        count = counts[color]
        if count > most_common_count:
            most_common_color = color
            most_common_count = count
    return most_common_color


def count(items: list[str]) -> dict[str, int]:
    freq_dict = {}
    for item in items:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
