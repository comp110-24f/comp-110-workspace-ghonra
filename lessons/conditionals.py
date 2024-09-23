"""practicing my conditionals"""


def less_than_10(num: int) -> None:
    "tell us if num <10"
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("small number!")  # then" block
    else:
        print("big number")
    print("have a nice day!")


less_than_10(num=7)


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


def number_info(num: int) -> int:
    if num < 10:
        print("small number.")
    else:
        if num % 2 == 0:
            print("even number")
        else:
            print("odd number")
    return num


number_info(num=11)
print(number_info(num=4))
