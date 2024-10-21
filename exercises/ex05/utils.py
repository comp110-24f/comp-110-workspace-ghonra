"""Implementing list utility functions"""

__author__ = "730649788"


def only_evens(input: list[int]) -> list[int]:
    evens: list[int] = []
    for num in input:
        if num % 2 == 0:
            evens.append(num)
    return evens


def sub(given: list[int], start: int, end: int) -> list[int]:
    if len(given) == 0 or start >= len(given) or end <= 0:
        return []
    result = []
    for i in range(start, end):
        result.append(given[i])
    return result


def add_at_index(input_list: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(0)
    for i in range(len(input_list) - 1, index, -1):
        input_list[i] = input_list[i - 1]
    input_list[index] = element
