def sum_nested(values):
    if not values:
        return 0
    elif isinstance(values[0], list):
        return sum_nested(values[0]) + sum_nested(values[1:])
    else:
        return values[0] + sum_nested(values[1:])
