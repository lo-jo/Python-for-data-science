import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) == 3:
            if (all(chr.isalpha() or chr.isspace() for chr in sys.argv[1])):
                lst = sys.argv[1].split(' ')
                number = int(sys.argv[2])

                iterator = ft_filter(lambda x: (len(x) >= number), lst)

                lst_iterator = list(iterator)

                print(lst_iterator)
            else:
                raise AssertionError("AssertionError: the arguments are bad")
        else:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)
        exit()


# your tests and your error handling
if __name__ == "__main__":
    main()
