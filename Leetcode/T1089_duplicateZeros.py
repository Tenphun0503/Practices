"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
"""


def duplicateZeros(arr):
    l = len(arr)

    for i in range(l):
        arr[i] = str(arr[i])
    print(arr)

    for i in range(l):
        if arr[i] == '0':
            arr[i] = '00'
    print(arr)

    tmp = list(''.join(arr)[:l])

    print(tmp)

    for i in range(l):
        arr[i] = int(tmp[i])

    print(arr)


def solution(arr):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0


arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros((arr))
print(arr)
