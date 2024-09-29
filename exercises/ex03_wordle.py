"""Making a Wordle!"""

__author__ = "730649788"


def input_guess(expected_length: int) -> str:
    guess = input(
        f"Enter a {expected_length} character word: "
    )  # local variable that is initial prompt to user
    while True:
        if len(guess) == expected_length:
            return guess  # if the word is correct length, return it!
        else:
            guess = input(
                f"That wasn't {expected_length} chars! Try again: "
            )  # error message + reprompts the user if incorrect length


def contains_char(
    search_word: str, goal_char: str
) -> bool:  # search for char in word, return True/False
    """check if a given character is found in given word"""
    assert len(goal_char) == 1  # the goal char will only be one letter
    index: int = 0  # index to start at first letter of word
    while index < len(
        search_word
    ):  # while loop to comb through word until char is found
        if (
            search_word[index] == goal_char
        ):  # if the index of the word is the goal char, return true
            return True
        index += 1  # go to the next letter until word is over
    return False  # if char is not found, exit loop and return False


def emojified(user_word: str, secret_word: str) -> str:
    """compares input word to secret word, checks if any chars match,output emoji"""
    assert len(user_word) == len(
        secret_word
    )  # the user word has to be the same len as the secret word or error
    WHITE_BOX: str = "\U00002B1C"  # emoji definition using binary stuff
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result: str = " "  # setting up empty string to copy values over
    index: int = 0
    while index < len(user_word):
        if (
            user_word[index] == secret_word[index]
        ):  # if the a char in user word matches postion in secret word
            emoji_result += GREEN_BOX  # a green box is returned
        elif contains_char(
            secret_word, user_word[index]
        ):  # if a char is in user word, but not same position as secret word
            emoji_result += YELLOW_BOX  # a yellow box is returned
        else:  # if a char is the user word is no in the secret word at all
            emoji_result += WHITE_BOX  # a white box returned
        index += (
            1  # moves to the next letter and checks conditions until the word is done
        )
    return emoji_result  # returns the emoji for each char of a word


def main(classified_word: str) -> None:  # main funciton of program, ties all together
    """the entrypoint of the program and game loop"""
    max_turns: int = 6  # local variable stating how many turns a user has
    current_turn: int = 1  # local variable stating the starting turn of user
    game_won: bool = False  # local variable saying the game starts out not won
    while current_turn <= max_turns and not game_won:  # starts game loops
        print(
            f"===Turn {current_turn}/{max_turns}==="
        )  # shows user what turn they're on
        guess: str = input_guess(
            expected_length=len(classified_word)
        )  # prompts user for word same len as classified word
        emoji_result: str = emojified(
            guess, classified_word
        )  # finds emojis results of classified word to guess word
        print(emoji_result)  # prints these emojis
        if guess == classified_word:  # if user gets it right
            print(
                f"You won in {current_turn} turns!"
            )  # print the win statment with how many turns it took
            game_won = True  # game_won turns into a true statment, stopping the loop
        else:
            current_turn += 1  # moves to the next turn and reruns loop
    if not game_won:
        print(
            str("X/6 - Sorry, try again tomorrow!")
        )  # print if user does not get the classified word at all


if __name__ == "__main__":  # helps run whole program!!
    main(classified_word="codes")
