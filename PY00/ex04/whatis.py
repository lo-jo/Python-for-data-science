# DESCRIPTION:
# The Even and the Odd

# Create a script that takes a number as argument, checks whether it is odd or even,
# and prints the result.
# If more than one argument is provided or if the argument is not an integer, print an
# AssertionError.

import sys
# print(sys.argv[0], len(sys.argv))

try:
    if len(sys.argv) != 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    if not sys.argv[1].isdigit():
        raise AssertionError("AssertionError: argument is not an integer")
except AssertionError as e:
    print(e)
    exit()

if (len(sys.argv) == 2):
    arg = int(sys.argv[1])
    # No need to check for int overflow because python integers have arbitrary precision 
    if arg%2 == 0:
        print("I am even")
    else:
        print("I am odd")

# assert len(sys.argv) == 2, "more than one argument is provided"


# if sys.argv.size()
# for arg in sys.argv:
#     print(arg)
