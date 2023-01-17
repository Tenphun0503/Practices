def removeDuplicates(nums):
    i = j = 1
    key = nums[0]
    res = 1
    while j < len(nums):
        if nums[j] == key:
            j += 1
        else:
            res += 1
            key = nums[j]
            if i != j:
                print(nums[i], nums[j])
                tmp = nums[j]
                nums[i] = nums[j]
                nums[j] = tmp
                print(nums)
            i += 1
            j += 1
    return res, nums

nums = [1,1,1,2,3,4,5]
print(removeDuplicates(nums))