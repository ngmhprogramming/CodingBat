def diff21(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n
print(diff21(19))
print(diff21(10))
print(diff21(21))
