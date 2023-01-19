"""
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1
"""

def singleNumber(nums):
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic.keys():
        if dic[i] == 1:
            return i