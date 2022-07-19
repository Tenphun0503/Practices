"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""


def decompressRLElist(nums):
    res = []
    for i in range(0, len(nums), 2):
        print(i + 1)
        for j in range(nums[i]):
            res.append(nums[i + 1])
    return res


def solution(nums):
    L, A = len(nums), []
    for i in range(0, L, 2):
        print(type(nums[i]), type(nums[i+1]))
        A.extend(nums[i] * [nums[i + 1]])
    return A


def solution2(N):
    return sum([N[i] * [N[i + 1]] for i in range(0, len(N), 2)], [])


nums = [1, 1, 2, 3]
print(solution2(nums))


