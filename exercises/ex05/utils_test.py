"""Implementing list utility functions tests"""

__author__ = "730649788"

# imports all the functions from utils.py
from exercises.ex05.utils import only_evens, sub, add_at_index

# says that this is going to be testing stuff
import pytest


# test to make sure the original list is not mutated
def test_only_evens_no_mutate() -> None:
    nums: list[int] = [1, 2, 4, 22, 27]
    # but still makes sure that the correct thing is returned
    assert only_evens(nums) == [2, 4, 22]
    assert nums == [1, 2, 4, 22, 27]


# test of edge case where there is an empty list as in input
def test_only_evens_edge_case() -> None:
    nums: list[int] = []
    # makes sure the return is an empty list
    assert only_evens(nums) == []


# another use test to make sure that the function works correctly
def test_only_evens_odds() -> None:
    # tests only odds to make sure nothing is returned
    nums: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(nums) == []


# test the return value of sub
def test_sub_ret_value() -> None:
    input: list[int] = [33, 55, 77, 99]
    # makes sure only correct numbers are returned in a list form
    assert sub(input, 1, 3) == [55, 77]


# tests edge case where an empty list is given as input
def test_sub_edge_case() -> None:
    input: list[int] = []
    # makes sure it returns an empty list
    assert sub(input, 1, 4) == []


# test to make sure that the orginial input is not mutated
def test_sub_no_mutate() -> None:
    input: list[int] = [3, 4, 6, 7]
    # also makes sure that the correct value is returned
    assert sub(input, 1, 2) == [4]
    assert input == [3, 4, 6, 7]


# test use of the function, makes sure it properly inserts at index
def test_add_at_index_insert() -> None:
    given: list[int] = [4, 8, 9]
    add_at_index(given, 6, 2)
    assert given == [4, 8, 6, 9]


# tests the case that if an empty list is given
def test_add_at_index_in_empty_list() -> None:
    given: list[int] = []
    # makes sure that the number is added to the list, even if originally empty
    add_at_index(given, 4, 0)
    # makes sure return value is correct
    assert given == [4]


# edge case to test an error and raise an IndexError
def test_add_at_index_raises_indexerror_edge() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    given: list[int] = [5, 6, 22]
    # tests that an error is raised with pytest
    with pytest.raises(IndexError):
        add_at_index(given, 7, 7)
