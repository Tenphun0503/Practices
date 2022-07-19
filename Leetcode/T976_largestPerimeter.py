"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.
"""


def largestPerimeter(nums: list):
    nums.sort(reverse=True)
    i = 0
    while i < len(nums) - 2 and nums[i] - nums[i + 1] >= nums[i + 2]:
        i += 1
    if i == len(nums) - 2:
        return 0
    return nums[i] + nums[i + 1] + nums[i + 2]


def solution(nums):
    nums.sort(reverse=True)
    for i in range(3, len(nums) + 1):
        if nums[i - 3] < nums[i - 2] + nums[i - 1]:
            return sum(nums[i - 3:i])


nums = [1, 2, 1]
print(largestPerimeter(nums))
