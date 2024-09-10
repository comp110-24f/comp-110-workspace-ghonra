"""practicing my conditionals"""


def less_than_10(num: int) -> None:
    "tell us if num <10"
    if num < 10:  # check if this is true
        print("small number!")  # then" block
    else:
        print("big number")
    print("this is the end of the function")


def wake_up(alarm: bool) -> str:
    """return a message based on if alarm is going off"""
    if alarm:
        return "Wake up! Go to Comp 110"
    else:
        return "Keep sleeping. You deserve it:)"


print(wake_up(alarm=False))


"""check first letter"""


def check_first_letter(word: str, letter: str) -> str:
    """checks if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match"


print(check_first_letter(word="happy", letter="h"))
