"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.
"""


def romanToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if 'IV' in s:
        num += 4
        s = s.replace('IV', '')
    elif 'IX' in s:
        num += 9
        s = s.replace('IX', '')
    if 'XL' in s:
        num += 40
        s = s.replace('XL', '')
    elif 'XC' in s:
        num += 90
        s = s.replace('XC', '')
    if 'CD' in s:
        num += 400
        s = s.replace('CD', '')
    elif 'CM' in s:
        num += 900
        s = s.replace('CM', '')
    for i in s:
        num += dic[i]

    return num


def solution(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number


s = 'MCMXCIV'
print(romanToInt(s))
