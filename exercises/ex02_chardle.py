"""EX02 - Chardle - A cute step towards wordle"""

__author__ = "730649788"


def input_word() -> str:
    word: str = input("Enter a 5 character word: ")
    if (
        len(word) == 5
    ):  # if the length of the word is 5 characters long, it will print the word, if not it will show an error statement
        return word
    else:
        print(str("Error: Word must contain 5 characters."))
        exit()  # exits program if the word does not meet the needed conditions


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if (
        len(letter) == 1
    ):  # similar to the first function, but now is for a single letter
        return letter
    else:
        print(str("Error: Character must be a single character."))
        exit()  # even if the inputted word has 5 characters and more than one character is inputted, then it will exit the function


def contains_char(word: str, letter: str) -> None:
    print(str("Searching for " + str(letter) + " in " + str(word)))
    count: int = 0  # local variable to help keep track of the matches found
    # checks each index for where it may be the same as the inputted letter
    if word[0] == letter:
        print(str(letter + " found at index 0"))
        count += 1
    if word[1] == letter:
        print(str(letter + " found at index 1"))
        count += 1
    if word[2] == letter:
        print(str(letter + " found at index 2"))
        count += 1
    if word[3] == letter:
        print(str(letter + " found at index 3"))
        count += 1
    if word[4] == letter:
        print(str(letter + " found at index 4"))
        count += 1

    if count == 0:
        print("No instance of " + str(letter) + " found in " + str(word))
    else:
        print(
            str(count) + " instance of " + str(letter) + " found in " + str(word)
        )  # takes the count of how many instances of a letter there are is in a word and inputs it into the printed string


def main() -> None:  # main function to help put it all together
    return contains_char(
        word=input_word(), letter=input_letter()
    )  # uses the previously defined function as arguments in the contains_char function


if __name__ == "__main__":
    main()
