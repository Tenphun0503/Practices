"""
An integer x is a good if after rotating each digit individually by 180 degrees,
we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.

Given an integer n, return the number of good integers in the range [1, n].
"""


def rotatedDigits(n):
    res = 0
    for i in range(1, n + 1):
        flag = False
        i = str(i)
        for j in i:
            if j in ['2', '5', '6', '9']:
                flag = True
        for j in i:
            if j in ['3', '4', '7']:
                flag = False

        if flag:
            print(i)
            res += 1
    return res


def solution(n):
    count = 0
    for d in range(1, n + 1):
        d = str(d)
        if '3' in d or '4' in d or '7' in d:
            continue
        if '2' in d or '5' in d or '6' in d or '9' in d:
            count += 1
    return count


n = 857
print(rotatedDigits(n))
