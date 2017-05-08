def near_hundred(n):
    if n > 89 and n < 111 or n > 189 and n < 211:
        return True
    else:
        return False
print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
