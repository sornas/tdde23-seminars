def largest(a, b):
    return a if a > b else b


def find_largest(values):
    if not values:
        return None
    elif len(values) == 1:
        if isinstance(values[0], list):
            return find_largest(values[0])
        else:
            return values[0]
    else:
        return largest(values[0], find_largest(values[1:]))
