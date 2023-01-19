"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
"""
def containsDuplicate(nums):
    dic = {}
    for i in nums:
        if i not in dic.keys():
            dic[i] = 1
        else:
            return True
    return False

nums = [1,2,3,4]
print(containsDuplicate(nums))