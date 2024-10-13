"""Mutating Functions"""

__author__ = 730649788


def manual_append(input: list[int], num: int) -> None:
    input.append(num)


def double(give: list[int]) -> None:
    index: int = 0
    while index < len(give):
        give[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
