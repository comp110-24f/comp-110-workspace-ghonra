"""concatentation"""

__author__ = "730649788"


def concat(word1: str, word2: str) -> str:
    return str(word1) + str(word2)


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
