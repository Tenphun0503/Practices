"""
Given an integer n
return an array ans of length n + 1 such that for each i (0 <= i <= n)
ans[i] is the number of 1's in the binary representation of i.
"""


def countBits(n):
    ans = []
    for i in range(n + 1):
        ans.append(bin(i)[2:].count('1'))

    return ans

n = 5
print(countBits(n))