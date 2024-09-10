"""Tea Party Time"""

__author__ = "730649788"


def tea_bags(people: int) -> int:
    "# of teabags needed based on the amount of guests"
    return people * 2


def treats(people: int) -> int:
    "# of treats based on the amount of guests"
    return tea_bags(people) * 1.5
