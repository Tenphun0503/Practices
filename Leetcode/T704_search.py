"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
"""

"""
Some key points:
    while condition: left can == right, which is only one element 
    when update left or right, it != mid
"""
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((right + left) / 2)
        if target == nums[mid]:
            return mid
        elif target >= nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
print(search(nums, 13))
