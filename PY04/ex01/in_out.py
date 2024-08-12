def square(x: int | float) -> int | float:
    """Function that returns the square of argument"""
    return x * x

def pow(x: int | float) -> int | float:
    """Function that returns the exponentiation
     of argument by itself
    """
    return x ** x

def outer(x: int | float, function) -> object:
    """Function that takes as argument a number and a function
    and returns an object that when called returns the result
    of the arguments calculation"""
    result = x
    def inner() -> float:
        nonlocal result
        result = function(result)
        return result
    return inner