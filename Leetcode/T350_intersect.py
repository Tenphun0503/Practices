"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
you may return the result in any order.
"""
import collections


def intersect(nums1, nums2):
    res = []
    for i in nums2:
        if i in nums1:
            res.append(i)
            nums1.remove(i)
            print(nums1)
    return  res

def solution(nums1, nums2):
    C = collections.Counter
    return list((C(nums1) & C(nums2)).elements())

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(solution(nums1, nums2))