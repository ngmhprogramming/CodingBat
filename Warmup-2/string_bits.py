def string_bits(str):
    out = ""
    for i in range(len(str)):
        if i % 2 == 0:
            out += str[i]
    return out
print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
