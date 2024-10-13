"""list utility functions exercise"""

__author__ = 730649788


# signature line for all function, returns bool
def all(int_list: list[int], goal: int) -> bool:
    # sets it up so that if there is nothing in the list it will return false
    if len(int_list) == 0:
        return False
    # using for...in... loop to iterate through all the nums in the int_list
    for num in int_list:
        # if all the nums do not align with the goal, then false is returned
        if num != goal:
            return False
    # otherwise true is returned
    return True


# signature line for max function, returns an int
def max(num_list: list[int]) -> int:
    # error statement if the length of the list is zero
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    # local variable to initialize largest with the first element of the list
    largest = num_list[0]
    # iterates through num list to find the largest number
    for i in num_list:
        # if the index in the list is bigger than the current largest
        if i > largest:
            # then it becomes the new largest value
            largest = i
    # once the whole list has been iterated through, the largest value will be returned
    return largest


# signature line with two lists as inputs, returns bool
def is_equal(list1: list[int], list2: list[int]) -> bool:
    # if the lengths of the two lists are different, false is returned
    if len(list1) != len(list2):
        return False
    # uses range function to iterate through each index of list1 and compare to list2
    for i in range(0, len(list1)):
        # if the numbers do not match at any given index, returns false
        if list1[i] != list2[i]:
            return False
    # if all the ints match at each index, return true
    return True


# signature line for extend, two lists as input with no return value
def extend(L1: list[int], L2: list[int]) -> None:
    # takes the first list and appends it by adding whatever was in the second list
    for idx in L2:
        L1.append(idx)
