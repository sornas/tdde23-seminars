def dict_func(d):
    result = {}
    for key in d:
        if d[key] in result:
            result[d[key]].append(key)
        else:
            result[d[key]] = [key]
    return result
