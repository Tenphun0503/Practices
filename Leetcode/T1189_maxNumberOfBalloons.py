"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""


def maxNumberOfBalloons(text):
    cha = [0] * 26
    for i in text:
        print(i, ord(i)-97)
        cha[ord(i)-97] += 1

    cha[11] //= 2
    cha[14] //= 2
    print(cha[0], cha[1], cha[11], cha[13], cha[14])
    return min(cha[0], cha[1], cha[11], cha[13], cha[14])


def solution(text):
    return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))


txt = 'nlaebolko'
print(maxNumberOfBalloons(txt))
