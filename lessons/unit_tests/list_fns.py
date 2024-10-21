"""unit tests"""


def get_first(start: list[str]) -> str:
    """return first element"""
    if len(start) == 0:
        return ""
    return start[0]


def remove_first(bye: list[str]) -> None:
    """remove first element"""
    bye.pop(0)


def get_and_remove_first(edit: list[str]) -> str:
    """remove AND return first element"""
    first_elem: str = edit[0]
    edit.pop(0)  # remove first elem
    return first_elem
