"""
T1
for (int i = 1 to n) {
  for (int j = i to n) {
    for (int k = j to n) {
      Sum += a[i]*b[j]*c[k]
    }
    If (gcd(i,j) == 1) {
j=n }
} }
"""


def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

print(gcd(1, 10))


# n = 10
# sums = 0
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# for i in range(1, n + 1):
#     j = i
#     while j <= n:
#         for k in range(j, n + 1):
#             print(i, j, k)
#             sums += nums[i] * nums[j] * nums[k]
#         if gcd(i, j) == 1:
#             print(i, j)
#             j = n
#         else:
#             j += 1
