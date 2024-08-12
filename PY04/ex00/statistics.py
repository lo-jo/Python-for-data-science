def mean(arguments : list) -> int:
    return sum(arguments) / len(arguments)

def median(arguments : list) -> int:
    sorted_list = arguments
    sorted_list.sort()
    length = len(sorted_list)
    if (length%2 == 0):
        length -= 1
    index = int(length/2)
    return sorted_list[index]

def quartile(arguments : list) -> list:
    sorted_list = arguments
    sorted_list.sort()
    length = len(sorted_list)
    if (length%2 == 0):
        length -= 1
    index = int(length/2)
    first_half = sorted_list[0:index]
    second_half = sorted_list[index:length]
    # print("FIRST HALF", first_half)
    # print("SECOND HALF", second_half)

    return list([float(first_half[len(first_half)-1]), float(second_half[len(first_half)-1])])

def variance(data):
    """Calculate the variance of a list of numbers."""
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / len(data)


def stddev(arguments : list):
    """Calculate the standard deviation of a list of numbers.
    TOTALLY MADE IN GPT because i suck at math :(((((((((((("""
    mean_value = mean(arguments)
    # sum of squared differences from the mean and dividing by the nb of the data points
    variance = sum((x - mean_value) ** 2 for x in arguments) / len(arguments)
    # square root of the variance
    return variance ** 0.5

def ft_statistics(*args: any, **kwargs: any) -> None:
    """ 
        DESCRIPTION :
        Function that takes in *args a quantity of unknown number
        and make the Mean, Median, Quartile (25% and 75%),
        Standard Deviation and Variance according to the **kwargs ask.

        NOTIONS :
        ** POSITIONAL ARGUMENTS (*args)
        Arguments passed to the function
        KEYWORD ARGUMENTS (**kwargs)
        Arguments passed to the function with a keyword (name=value)
        Collected into a dictionary called kward

        ** DICTIONARY OF FUNCTIONS
        "string key" : function value (function objects)
    """

    functions = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": stddev,
        "var": variance
    }
 
    arguments = list(args)
    for key in kwargs.items():
        # print(key)
        if (key[1] in functions and args) :
            calling = functions[key[1]]
            print(f"{key[1]} : {calling(arguments)}")
        elif (not args):
            print("ERROR")