"""
Given an array of integers 'nums' and an integer 'target'
Return indices of the two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution
You may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Constraints:
    2 <= len(nums) <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        seen = {}
        for i, value in enumerate(nums):
            remain = target - value

            if remain in seen:
                return [i, seen[remain]]
            else:
                seen[value] = i


# Use below code to test
nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
