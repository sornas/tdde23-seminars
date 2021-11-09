def S1(s):
    if len(s) < 2:
        return False
    elif s[0] == "a":
        return A1(s[1:])
    elif s[0] == "b":
        return B1(s[1:])
    else:
        return False

def A1(s):
    if not s:
        return True
    elif s[0] == "a":
        return B1(s[1:])
    return False

def B1(s):
    return s == "a" or s == "b"

def S2(s):
    if not s:
        return True
    elif s == "a" or s == "b":
        return True
    elif s[0] == "a" and s[-1] == "a":
        return S2(s[1:-1])
    elif s[0] == "b" and s[-1] == "b":
        return S2(s[1:-1])
    return False


def is_two(foo):
    if foo == foo[::-1]:
        for letter in foo:
            if letter != "a" and letter != "b":
                return False
        return True
    return False

def is_two(s):
    return s == s[::-1] and all(let == "a" or let == "b" for let in s)

def contains_prefix(prefs, strs):
    if len(prefs) > len(strs):
        raise ValueError
    if len(prefs) == 0:
        return True
    if prefs[0] == strs[0][0:len(prefs[0])]:
        return contains_prefix(prefs[1:], strs[1:])
    else: 
        return False

def is_two(foo):
    if foo == foo[::-1]:
        for letter in foo:
            if letter != "a" and letter != "b":
                return False
        return True
    return False

def is_two(s):
    return s == s[::-1] and all(let == "a" or let == "b" for let in s)

def contains_prefixes(prefixes, strs):
    return all(any(s.startswith(prefix) for s in strs) for prefix in prefixes)
