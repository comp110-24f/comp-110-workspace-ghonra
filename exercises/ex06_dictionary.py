"""Dictionary Utility FUNction"""

__author__ = "730649788"


def invert(input: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}
    for key in input:
        value = input[key]
        if value in inverted_dict:
            raise KeyError("Inverting would result in duplicate keys")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    color_counts = {}
    first_seen_color = ""
    count = 0
    for name in colors:
        color = colors[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

        if color_counts[color] > count:
            count = color_counts[color]
            first_seen_color = color
        elif color_counts == count and first_seen_color == "":
            first_seen_color = color
    return first_seen_color


def count(values: list[str]) -> dict[str, int]:
    counts = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    order = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in order:
            order[first_letter] = []
        order[first_letter].append(word)
    return order


def update_attendance(attended: dict[str, list[str]], days: str, students: str) -> None:
    if days in attended:
        attended[days].append(students)
    else:
        attended[days] = [students]
