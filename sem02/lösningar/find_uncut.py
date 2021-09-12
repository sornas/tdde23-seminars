def find_uncut(grass):
    uncut = []
    for y in range(len(grass)):
        for x in range(len(grass[y])):
            if not grass[y][x]:
                uncut.append((x, y))
    return uncut


print(find_uncut([
    [True, False, True, False],
    [False, False, True, True],
    [True, False, False, True],
    [False, True, True, True],
]))
