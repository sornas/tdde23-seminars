def palin_rec(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and palin_rec(s[1:-1])


print(palin_rec(""))
print(palin_rec("a"))
print(palin_rec("ABBA"))
print(palin_rec("kajak"))
print(palin_rec("aa"))
print(palin_rec("ab"))
print(palin_rec("palin"))
