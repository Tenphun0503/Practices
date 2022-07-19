"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"
"""


def defangIPaddr(address):
    ans = ''
    for i in address:
        if i == '.':
            ans += '[.]'
        else:
            ans += i
    return ans


def solution(address):
    return address.replace('.', '[.]')


address = "1.1.1.1"
print(defangIPaddr(address))
