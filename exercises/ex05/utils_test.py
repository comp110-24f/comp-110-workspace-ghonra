"""Implementing list utility functions tests"""

__author__ = "730649788"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_no_mutate() -> None:
    nums: list[int] = [1, 2, 4, 22, 27]
    assert only_evens(nums) == [2, 4, 22]
    assert nums == [1, 2, 4, 22, 27]


def test_only_evens_edge_case() -> None:
    nums: list[int] = []
    assert only_evens(nums) == []


def test_only_evens_odds() -> None:
    nums: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(nums) == []


def test_sub_ret_value() -> None:
    input: list[int] = [33, 55, 77, 99]
    assert sub(input, 1, 3) == [55, 77]


def test_sub_edge_case() -> None:
    input: list[int] = []
    assert sub(input, 1, 4) == []


def test_sub_no_mutate() -> None:
    input: list[int] = [3, 4, 6, 7]
    assert sub(input, 1, 2) == [4]
    assert input == [3, 4, 6, 7]


def test_add_at_index_insert() -> None:
    given: list[int] = [4, 8, 9]
    add_at_index(given, 6, 2)
    assert given == [4, 8, 6, 9]


def test_add_at_index_in_empty_list() -> None:
    given: list[int] = []
    add_at_index(given, 4, 0)
    assert given == [4]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    given: list[int] = [5, 6, 22]
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(given, 7, 7)
