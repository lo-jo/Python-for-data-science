def count_in_list(lst : list, string : str) -> int:
    """
    Count occurrences of a string in a list using 'list comprehension'

    Args:
        lst (list): The list to search for occurrences of the string.
        string (str): The string to count occurrences of.

    Returns:
        int: The number of occurrences of the string in the list.
    """
    return len([item for item in lst if item == string])
