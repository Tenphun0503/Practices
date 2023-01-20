"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
"""

def sortedSquares(nums):
    res = []
    left, right = 0, len(nums) - 1
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            res.append(nums[right] ** 2)
            right -= 1
        else:
            res.append(nums[left] ** 2)
            left += 1
    res.reverse()
    return res

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))