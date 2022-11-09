"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""
import collections


def longestPalindrome(s):
    count = []
    for i in range(len(s)):
        if s[i] != ' ':
            count.append(s.count(s[i]))
            s = s.replace(s[i], ' ')
    res = 0
    pivot = 0
    for i in count:
        if i % 2 == 0:
            res += i
        else:
            if pivot == 0:
                res += i
                pivot = 1
            else:
                res += i - 1
    return res

s = "abccccdd"
print(longestPalindrome(s))
a = collections.Counter(s)
print(a.itervalue)