def find_uncut(grass):
    uncut = []
    h = len(grass)
    w = len(grass[0])  # assume square
    for y in range(h):
        for x in range(w):
            if not grass[y][x]:
                uncut.append((x, y))
    return uncut


def find_uncut2(grass):
    h = len(grass)
    w = len(grass[0])
    return [(x, y) for y in range(h) for x in range(w) if not grass[y][x]]


print(find_uncut([
    [True, False, True, False],
    [False, False, True, True],
    [True, False, False, True],
    [False, True, True, True],
]))

print(find_uncut2([
    [True, False, True, False],
    [False, False, True, True],
    [True, False, False, True],
    [False, True, True, True],
]))
