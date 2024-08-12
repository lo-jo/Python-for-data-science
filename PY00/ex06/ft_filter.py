
def ft_filter(function, iterable):
    """
    ft_filter(function, iterable)
    Returns an iterator yielding those items of the iterable for which function(item) is true.
    
    Args:
        function (callable): A function that determines whether an item should be included.
        iterable (iterable): An iterable to filter.
    
    Yields:
        Any: The items of the iterable for which the function returns True.
    """
    if function is not None and iterable is not None:
        item_lst = [i for i in iterable if function(i) is True]
        for item in item_lst:
            yield item
