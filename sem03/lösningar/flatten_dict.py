def flatten_dict(data):
    flat = {}
    for key, val in data.items():
        if isinstance(val, dict):
            flat |= flatten_dict(val)
        else:
            flat[key] = val
    return flat


data = {
    "a": {
        "a": {
            "python": 1,
            "java": 2
        },
        "b": {}
    },
    "b": {
        "c": 3
    },
}
print(data)
print(flatten_dict(data))
