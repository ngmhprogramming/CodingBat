def string_match(a, b):
    count = 0
    shorter = min(len(a), len(b))
    for i in range(shorter-1):
        a_check = a[i:i+2]
        b_check = b[i:i+2]
        if a_check == b_check:
            count += 1
    return count
print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
