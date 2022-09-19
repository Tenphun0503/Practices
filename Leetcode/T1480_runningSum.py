


def runningSum(nums):
    res = [nums[0]]
    for i in range(1, len(nums)):
        res.append(res[-1] + nums[i])

    return res


nums = [1, 2, 3, 4]
print(runningSum(nums))
