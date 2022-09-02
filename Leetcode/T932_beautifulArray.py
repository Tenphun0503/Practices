"""
An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

Example 1:
    Input: n = 4
    Output: [2,1,4,3]

Solution: https://leetcode.com/problems/beautiful-array/discuss/1368125/Detailed-Explanation-with-Diagrams.-A-Collection-of-Ideas-from-Multiple-Posts.-Python3
"""


def recurse(nums):
    if len(nums) <= 2:
        return nums
    return recurse(nums[::2]) + recurse(nums[1::2])


def beautifulArray(n):
    return recurse([i for i in range(1, n + 1)])


print(beautifulArray(10))