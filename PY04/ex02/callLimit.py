from typing import Any, Callable


def callLimit(limit: int):
    count = 0

    def callLimiter(function: Callable) -> Callable:
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f'Error: {function} call to many times')
        return limit_function
    return callLimiter

# def counter(fn):
#     c = 0
#     def wrapper(*args, **kwargs):
#         nonlocal c
#         c += 1
#         print(f'{fn.__name__} function is called {c} times.')
#         return fn(*args, **kwargs)
#     return wrapper

# @counter
# def mult(a, b):
#     return a * b

# @counter
# def add(a, b, c):
#     return a + b + c

# print(mult(5, 4))
# print(add(3, 6, 8))
