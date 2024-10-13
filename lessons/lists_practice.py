"""list practice"""

my_number: list[float] = list()  # constructor
my_number: list[float] = []  # literal

print(my_number)

# add an item to the list
my_number.append(1.5)
my_number.append(2.3)

print(my_number)

# create an already populated list
game_points: list[int] = [102, 86, 94]
# modifying elements
game_points[1] = 72
print(game_points)

# subscription notation/indexing
print(game_points[2])

# getting length
print(len(game_points))

# remove an element
game_points.pop(1)
print(game_points)

# write function called display
# input: list[int]
# return value: none
# loop over the input and print every value
# try calling on gam_points


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


print(display(game_points))
