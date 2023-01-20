"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def removeElement(nums, val):
    i = j = 0
    length = 0
    while j < len(nums):
        if nums[j] == val:
            j += 1
        elif nums[j] != val:
            length += 1
            if i != j:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                i += 1
                j += 1
    return length