from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruit: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruit) == "apples"


def test_remove_first_ret_value() -> None:
    """test that removes first value, returns none"""
    fruit: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruit) is None


def test_remove_first_behavior() -> None:
    fruit: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruit)
    assert fruit == ["oranges", "bananas"]


def test_get_first_edge_case() -> None:
    """test that get_frst works with empty list"""
    input: list[str] = []
    assert get_first([]) == ""
