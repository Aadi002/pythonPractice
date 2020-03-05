def array_front9(nums):
    for i in range(4):
        if nums[i] == 9:
            return True
        else:
            continue
    return False


result = array_front9([1,2,0,7,9])
print(result)