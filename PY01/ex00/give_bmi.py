import numpy as np


# Python 2 and Python 3 provide arbitrary precision integers.
# This means that you don’t need to worry about overflowing
# or underflowing the integer datatypes.
# Floats, however, are not arbitrary precision.
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculates and returns a list of body mass index (BMI) values
    """
    try:
        assert height and weight, "Error: one of the lists is empty"
        assert len(height) == len(weight), "Error: the lists have diff. lens"
        hArr = np.array(height)
        wArr = np.array(weight)
        if hArr.dtype.kind not in 'iu' and hArr.dtype.kind != 'f':
            raise AssertionError("Error: list height has different types")
        if wArr.dtype.kind not in 'iu' and wArr.dtype.kind != 'f':
            raise AssertionError("Error: list weight has different types")
        assert np.all(hArr > 0) and np.all(wArr > 0), "Error: not positive num"
        bmiVals = []
        # zip() is used to combine multiple iterables into a single iterator
        for h, w in zip(height, weight):
            # Convert height and weight to np.float64 for higher precision
            bmi = np.float64(w) / (np.float64(h) ** 2)
            bmiVals.append(bmi)
        return bmiVals

    except AssertionError as e:
        print(e)
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of booleans (True if above the limit)"""
    try:
        assert bmi, "Error: there is no BMI to apply_limit to"
        assert limit, "Error: there is no limit"
        if not isinstance(limit, int) or limit <= 0:
            raise AssertionError("Error: limit must be int positive")
        bmiArr = np.array(bmi)
        if bmiArr.dtype.kind not in 'iu' and bmiArr.dtype.kind != 'f':
            raise AssertionError("Error: list weight has different types")
        assert np.all(bmiArr > 0), "Error: not positive numbers"
        # In numpy, operations like (bmiArr > limit) are vectorized operations
        # This means that the comparison is applied element-wise to
        # the entire array bmiArr without the need for explicit iteration
        return (bmiArr > limit).tolist()
    except AssertionError as e:
        print(e)
