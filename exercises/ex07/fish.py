"""File to define Fish class."""

__author__ = "730649788"


class Fish:
    age: int

    def __init__(self, age: int):
        self.age = 0

    def one_day(self):
        self.age += 1
        return None
