"""Implementing list utility functions"""

__author__ = "730649788"


# signature line for only_evens, has one input (list of ints) and returns list of ints
def only_evens(input: list[int]) -> list[int]:
    # starts the evens list as an empty list so the evens can be added into it
    evens: list[int] = []
    # for-in loop to iterate through all values in given list
    for num in input:
        # if there is are remainder of 0 when divided by 2 then the number is even
        if num % 2 == 0:
            # then that number is added to the empty evens list
            evens.append(num)
    # the list of evens will be returned
    return evens


# sig. line for sub, 3 inputs: list of ints, start, and end index, returns list of ints
def sub(given: list[int], start: int, end: int) -> list[int]:
    # if list has nothing in it or the start/end indexes are out of range of the length
    if len(given) == 0 or start >= len(given) or end <= 0:
        # returns an empty list
        return []
    # adjusts start index in case it is negative
    if start < 0:
        # makes it start at index 0
        start = 0
    # adjust end index in case it goes over the length of the list
    if end > len(given):
        # makes it only go to the length of the list
        end = len(given)
    # starts with empty list
    result = []
    # Appends elements from given start index to end index to the result list
    for i in range(start, end):
        # Add each element to the empty result list
        result.append(given[i])
    # returns the values in between the start and end index (not inclusive) in a list
    return result


# sig line for add_at_index, 3 inputs: list of ints, new element, and where to add it
def add_at_index(input_list: list[int], element: int, index: int) -> None:
    # raise error if there is an issue with the index; if it it out of bounds
    if index < 0 or index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    # acts as a placeholder for the new element being added
    input_list.append(0)
    # for-in loop that iterates backwards through the list until it gets to specificed
    # index
    for i in range(len(input_list) - 1, index, -1):
        # shifts everything to the right to make room for new value
        input_list[i] = input_list[i - 1]
    # inserts the given number at the given index
    input_list[index] = element
