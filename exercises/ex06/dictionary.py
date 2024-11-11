"""Dictionary Utility FUNction"""

__author__ = "730649788"


# signature line to invert dictionaries; dict input, dict output
def invert(input: dict[str, str]) -> dict[str, str]:
    # create an empty dict to add the flipped values to
    inverted_dict: dict[str, str] = {}
    # use a for...in loop to go through the original dict
    for key in input:
        # local variable setting up what value was
        value = input[key]
        # if the value is in the inverted_dict, then an error should arise
        if value in inverted_dict:
            # this is because there cannot be duplicate keys
            # since there can be duplicate values,  flipping these values into
            # the key position
            # would result in duplicate keys
            raise KeyError("Inverting would result in duplicate keys")
        # if all looks well and right, then the key becomes the value and
        # the value becomes the key
        # in the inverted_dict (added onto it)
        inverted_dict[value] = key
    # returns the new list of inverted values
    return inverted_dict


# signature line to find favorite color; dict input, str output
def favorite_color(colors: dict[str, str]) -> str:
    # sets up empty dict to count occurences of each color
    color_counts: dict[str, int] = {}
    # empty str to store the most popular color
    first_seen_color: str = ""
    # variable to store the maximum count
    max_count: int = 0
    # loop through the values in the dict
    for name in colors:
        # gets the favorite color of the current person
        color = colors[name]
        # works to update the count of the color that was found for the current person
        if color in color_counts:
            color_counts[color] += 1
        else:
            # initializes count if there is a new color
            color_counts[color] = 1
        # check to see if the color has higher count than current max count
        if color_counts[color] > max_count:
            # updates max_count to this color's count and sets it as first_seen_color
            max_count = color_counts[color]
            first_seen_color = color
        # if the color's count matches current max count and no max color
        # was set, use this color
        elif color_counts[color] == max_count and first_seen_color == "":
            first_seen_color = color
    # returns the color that appeared the most
    return first_seen_color


# signature line to count how many times a value appears; input list, return dict
def count(values: list[str]) -> dict[str, int]:
    # sets up an empty dict to put in counts of the values in the list
    counts: dict[str, int] = {}
    # uses for... loop to iterate through list
    for item in values:
        # if the item is already in the counts dict
        if item in counts:
            # add one to the count of it
            counts[item] += 1
        else:
            # if it is a newly encountered value, initalize a new count at 1
            counts[item] = 1
    # returns the dict with counts for each variable in the list
    return counts


# signature line to put things in alphabetical categories; list input, dict return
def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    # initializes an empty dict
    order: dict[str, list[str]] = {}
    # loop through each word in the list of words
    for word in words:
        # gets the first letter of each word and makes it lowercase
        first_letter = word[0].lower()
        # checks if first letter is already a key
        if first_letter not in order:
            # if not, it sets up a new entry with this letter as a key + an empty list
            order[first_letter] = []
        # adds the word to the list corresponding to its first letter
        order[first_letter].append(word)
    # returns the dictionary with words organized by first letter
    return order


# signature line for keeping attendance; input dict, str, str and return nothing
def update_attendance(attended: dict[str, list[str]], day: str, student: str) -> None:
    # loops though the attended dict, making sure the specified day already existed
    if day in attended:
        # if the student's name is not already on the attendance list for the day
        if student not in attended[day]:
            # add it to the list
            attended[day].append(student)
    else:
        # if the day is not already in the dictionary, creates a new entry
        # with the day as key
        # and set the value as a list containing the student's name
        attended[day] = [student]
