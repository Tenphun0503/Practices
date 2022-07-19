"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array.Otherwise, return false.
"""


def threeConsecutiveOdds(arr):
    hit = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            hit += 1
        if hit == 3:
            print(arr[i - 2], arr[i - 1], arr[i])
            return True
        if arr[i] % 2 == 0:
            hit = 0

    return False


def solution(arr):
    return "111" in "".join([str(i % 2) for i in arr])


arr = [1, 1, 1]
print(threeConsecutiveOdds(arr))
