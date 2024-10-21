"""find max test """

__author__ = " 730649788"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_ret_value() -> None:
    input: list[int] = [1, 4, 6, 8]
    assert find_and_remove_max(input) == 8


def test_find_and_remove_max_mutate() -> None:
    input: list[int] = [1, 4, 6, 8, 10]
    assert find_and_remove_max(input) == 10
    assert input == [1, 4, 6, 8]


def test_find_and_remove_max_edge_case() -> None:
    input: list[int] = []
    assert find_and_remove_max(input) == -1
