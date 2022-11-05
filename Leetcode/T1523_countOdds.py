"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].
"""
def countOdds(low, high):
    if low % 2 == 1:
        low -= 1
    if high % 2 == 1:
        high += 1
    return (high - low) / 2

def c2(low, high):
    return (high + 1)//2  - low//2


print(c2(2,6))