"""Find max"""

__author__ = "730649788"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    largest = input[0]
    for num in input:
        if num > largest:
            largest = num
    while largest in input:
        input.pop(input.index(largest))
    return largest
