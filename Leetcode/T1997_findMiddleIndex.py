"""
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where
nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0.
Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
"""

def findMiddleIndex(nums):
    for i in range(len(nums)):
        if i == 0:
            left = 0
            right = sum(nums[1:])
        elif i == len(nums) - 1:
            right = 0
            left = sum(nums[:-1])
        else:
            left = sum(nums[:i])
            right = sum(nums[i+1:])

        if left == right:
            return i
    return -1


def solution2(nums):
    leftSum = 0
    rightSum = sum(nums)

    for i in range(len(nums)):
        if leftSum == rightSum - nums[i]:
            return i

        leftSum += nums[i]
        rightSum -= nums[i]

    return -1

nums = [12,5]
print(findMiddleIndex(nums))
