def front_times(str, n):
    if len(str) < 3:
        return str * n
    else:
        return str[0:3] * n
print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))
