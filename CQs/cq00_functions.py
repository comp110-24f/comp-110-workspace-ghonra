"""Writing function Practice"""

__author__ = 730549788


def mimic(message: str) -> str:
    "mimic the given message"
    return message


def main() -> None:
    "Main function - print mimic"
    print(mimic(message=input("what is your message")))


if __name__ == "__main__":
    main()
