"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""
import math


def findGCD(nums: list):
    smallest = sorted(nums)[0]
    largest = sorted(nums)[-1]
    print(smallest, largest)
    for i in range(smallest, 0, -1):
        if largest % i == 0 and smallest % i == 0:
            return i


def solution(nums):
    return math.gcd(max(nums), min(nums))


nums = [2, 5, 6, 9, 10]

print(solution(nums))
