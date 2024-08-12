from array2D import slice_me
def prPurple(skk): print("\033[95m {}\033[00m".format(skk))

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

familia = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

prPurple("LIST TO SLICE :")
prPurple(family)
prPurple("\n SLICING WITH 0,2")
print(slice_me(family, 0, 2))
prPurple("SLICING WITH 1,-2")
print(slice_me(family, 1, -2))
prPurple("SLICING OUT OF RANGE 1,6 ??")
print(slice_me(family, 1, 6))
prPurple("SLICING A TUPLE (not a list) WITH 0,1")
print(slice_me(familia, 0, 1))