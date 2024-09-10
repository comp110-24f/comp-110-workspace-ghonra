"""A Cozy Tea Party"""

__author__ = "730649788"


def main_planner(guests: int) -> None:
    "determines the total supplies needed and the total cost based on the number of guests that will be in attendance"
    print(
        "A Cozy Tea Party for " + str(guests) + " people!"
    )  # convert guests from int into str or error will occur because cannot directly concatenate int with a str
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # people needs to equal guests because number of guests will be given, not number of people; need to establish that this number going to be the same
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # where it is established that tea_count is equal to the tea_bags function and same for treat_count being equal to treats function


def tea_bags(people: int) -> int:
    "# of teabags needed based on the amount of guests"
    return people * 2


def treats(people: int) -> int:
    "# of treats based on the amount of guests"
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "cost of tea party based on how many treats and tea bags there are"
    return (tea_count * 0.5) + (
        treat_count * 0.75
    )  # ran into trouble here; thought I had to call back to the tea_bags and treats function, but realized that I could do that in my main function


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your party?")))
