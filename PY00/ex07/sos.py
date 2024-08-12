import sys


def main():
    try:
        NESTED_MORSE = {
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            "0": "----- ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
            " ": "/ "
        }
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        if any(char not in NESTED_MORSE for char in sys.argv[1].upper()):
            raise AssertionError("AssertionError: the arguments are bad")
        str = ""
        for char in sys.argv[1].upper():
            if char in NESTED_MORSE:
                str += NESTED_MORSE[char]
        print(str)

    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
