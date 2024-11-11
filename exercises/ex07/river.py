"""File to define River class."""

__author__ = "730649788"

from ex07.fish import Fish
from ex07.bear import Bear


class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish(1))
        for _ in range(0, num_bears):
            self.bears.append(Bear(age=0, hunger_score=0))

    def check_ages(self):
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(5)
        return None

    def check_hunger(self):
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None

    def repopulate_fish(self):
        num_new_fish = (len(self.fish) // 2) * 4
        for fish in range(num_new_fish):
            self.fish.append(Fish(age=0))
        return None

    def repopulate_bears(self):
        num_new_bears = len(self.bears) // 2
        for bears in range(num_new_bears):
            self.bears.append(Bear(age=0, hunger_score=0))
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}:")
        print(f"Fish population: {self.fish}")
        print(f"Bear population: {self.bears}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        "simulate one week in the river"
        for x in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        for fish in range(min(amount, len(self.fish))):
            self.fish.pop(0)
