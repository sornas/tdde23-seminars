def fibonacci(n):
    if n < 3:
        return n - 1
    a = 0
    b = 0

    for i in range(n - 2):
        c = b
        b = a + b
        a = c
    return b
