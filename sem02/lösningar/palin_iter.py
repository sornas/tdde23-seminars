def palin_iter(s):
    mid = len(s) // 2
    for i in range(mid):
        if s[i] != s[-(i + 1)]:
            return False
    return True


print(palin_iter(""))
print(palin_iter("a"))
print(palin_iter("ABBA"))
print(palin_iter("kajak"))
print(palin_iter("aa"))
print(palin_iter("ab"))
print(palin_iter("palin"))
