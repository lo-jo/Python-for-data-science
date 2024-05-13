import sys


def get_lower_count(object: str) -> int:
    """ Returns the sum of lowercase characters in object
    """
    count = 0
    for element in object:
        if element.islower():
            count += 1
    return count


def get_upper_count(object: str) -> int:
    """ Returns the sum of uppercase characters in object
    """
    count = 0
    for element in object:
        if element.isupper():
            count += 1
    return count


def get_space_count(object: str) -> int:
    """ Returns the sum of spaces in object
    """
    count = 0
    for element in object:
        if element.isspace():
            count += 1
    return count


def get_digit_count(object: str) -> int:
    """ Returns the sum of digits in object
    """
    count = 0
    for element in object:
        if element.isdigit():
            count += 1
    return count


def get_punct_count(object: str) -> int:
    """ Returns the sum of punctuation marks in object
    """
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    count = 0
    for char in object:
        if char in punctuations:
            count += 1
    return count


def main():
    text = ''
    try:
        if len(sys.argv) < 2:
            text = input("What is the text to count?\n")
            text += '\n'
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("More than one string provided")
    except AssertionError as e:
        print(e)
        exit()

    print("The text contains", len(text), "characters:")
    print(get_upper_count(text), "upper letters")
    print(get_lower_count(text), "lower letters")
    print(get_punct_count(text), "punctuation marks")
    print(get_space_count(text), "spaces")
    print(get_digit_count(text), "digits")


# your tests and your error handling
if __name__ == "__main__":
    main()
