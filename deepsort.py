def deep_sorted(x):
    # If x is a number (int or float) – nothing to sort, just return it
    if isinstance(x, (int, float)):
        return x

    # If x is a string:
    # - If it looks like a number (for example, "45"), convert it to int
    # - Otherwise, keep it as a string
    if isinstance(x, str):
        if x.isdigit():
            return int(x)
        return x

    # If x is a list:
    # 1. Apply deep_sorted to each element (go inside recursively)
    # 2. Sort the results
    #    Use key=str so different types can still be compared
    if isinstance(x, list):
        result = []
        for item in x:
            result.append(deep_sorted(item))
        return sorted(result, key=str)

    # If x is a tuple:
    # Same logic as list, but return a tuple at the end
    if isinstance(x, tuple):
        result = []
        for item in x:
            result.append(deep_sorted(item))
        return tuple(sorted(result, key=str))

    # If x is a set:
    # Sets are unordered, so:
    # 1. Convert to list
    # 2. Recursively sort elements
    # 3. Sort them for consistent order
    # 4. Convert back to set
    if isinstance(x, set):
        result = []
        for item in x:
            result.append(deep_sorted(item))
        return set(sorted(result, key=str))

    # If x is a dictionary:
    # 1. Sort keys
    # 2. Recursively apply deep_sorted to each value
    if isinstance(x, dict):
        result = {}
        for key in sorted(x, key=str):
            result[key] = deep_sorted(x[key])
        return result


if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest
    print (doctest.testmod())
