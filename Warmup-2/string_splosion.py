def string_splosion(str):
    out = ""
    for i in range(len(str)):
        out += str[0:(i+1)]
    return out
print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
