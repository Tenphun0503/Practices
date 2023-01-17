"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


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
                nums[i] = nums[j]
            i += 1
            j += 1
    return res


nums = [1,1,1,2,3,4,5]
print(removeDuplicates(nums))