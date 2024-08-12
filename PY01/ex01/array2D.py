import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    DESCRIPTION :
    Takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on
    the provided start and end arguments,
    using the slicing method.

    Slicing in python :
    Taking elements from one given index to another given index.
    The slice is passed like this list[start:end]
    Negatives access the list from the end

    NumPy arrays:
    Arrays are faster than lists in python.
    Arrays can directly handle arithmetic operations while
    lists cannot.
    
    Shape() method :
    Used to obtain the dimensions of a python object.
    Part of the numpy library:
    The initial list object is converted into a NumPy array
    using np.array(family).
    The shape is returned as a tuple.
    """

    result_list = []
    try:
        if not isinstance(family, list):
            raise AssertionError("Object provided is not a list")
        else:
            # Convert initial list to NumPy array
            initial_list = np.array(family)
            print("MY INITIAL SHAPE IS", initial_list.shape)
            new_list = initial_list[start:end]
            print("MY NEW SHAPE IS :", new_list.shape)
            # Convert np array back to list before returning
            result_list = new_list.tolist()
    except AssertionError as e:
        print(e)
        exit(1)

    return result_list
