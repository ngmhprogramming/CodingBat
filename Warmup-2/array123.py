def array123(nums):
    if nums == []:
        return False
    for i in range(len(nums)):
        try:
            if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
                return True
        except:
            return False
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
