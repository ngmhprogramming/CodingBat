def monkey_trouble(a_smile, b_smile):
    if a_smile == True:
        if b_smile == True:
            return True
        else:
            return False
    else:
        if b_smile == False:
            return True
        else:
            return False
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
