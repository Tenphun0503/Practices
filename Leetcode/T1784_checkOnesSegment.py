"""
Given a binary string s without leading zeros
return true if s contains at most one contiguous segment of ones. Otherwise, return false.
"""


def checkOnesSegment(s):
    if_zero = False
    for i in s:
        if if_zero:
            if i == '1':
                return False
        if i == '0':
            if_zero = True
    return True


s = '1111000000'
print(checkOnesSegment(s))
