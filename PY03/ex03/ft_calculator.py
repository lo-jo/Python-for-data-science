class calculator:
    """
    Calculator class that is able to do calculations
    (addition, multiplication, subtraction, division)
    of vector with a scalar.
    """
    def __init__(self, object) -> None:
        """
        Initializes the calculator with a vector of numbers.

        Parameters:
        object (vector): A vector of numbers to be used
        for arithmetic operations.
        """
        self.vec = object

    def __add__(self, object) -> None:
        """
        Adds a number to each element in the vector.

        Parameters:
        object (int or float): The number to be
        added to each element in the vector.
        """
        self.vec = [item + object for item in self.vec]
        print(self.vec)

    def __mul__(self, object) -> None:
        """
        Multiplies each element in the vector by a number.

        Parameters:
        object (int or float): The number to multiply
        each element in the vector by.
        """
        self.vec = [item * object for item in self.vec]
        print(self.vec)

    def __sub__(self, object) -> None:
        """
        Subtracts a number from each element in the vector.

        Parameters:
        object (int or float): The number to be subtracted
        from each element in the vector.
        """
        self.vec = [item - object for item in self.vec]
        print(self.vec)

    def __truediv__(self, object) -> None:
        """
        Divides each element in the vector by a number.

        Parameters:
        object (int or float): The number to divide
        each element in the vector by.

        Raises:
        ZeroDivisionError: If the object is zero.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Error: division by 0 not allowed")
            self.vec = [item / object for item in self.vec]
            print(self.vec)
        except ZeroDivisionError as e:
            print(e)
