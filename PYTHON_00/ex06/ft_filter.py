def ft_filter(condition, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    filtered_result = []
    # filtered_result.append(item for item in iterable if condition(item))
    filtered_result = [item for item in iterable if condition(item)]
    return filtered_result

def ft_positive(item):
    if item > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    # print(ft_filter.__doc__)
    test = { 0, 5, -4, -9 , 10}
    filtered_result = list(ft_filter(ft_positive, test))
    print(filtered_result)