def array_front9(nums):
    if 9 in nums[0:4]:
        return True
    else:
        return False
print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))
