'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

subarray is a contiguous array

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

def minSubArrayLen(target, nums):
    left = 0
    res = float('inf')
    sums = 0
    for right in range(0, len(nums)):
        sums += nums[right]
        while sums >= target:
            res = min(right - left + 1, res)
            sums -= nums[left]
            left += 1
    return 0 if res == float('inf') else res


target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))