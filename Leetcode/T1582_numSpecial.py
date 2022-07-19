"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0
(rows and columns are 0-indexed).
"""
import numpy as np


def numSpecial(mat):
    res = 0
    m = len(mat)
    n = len(mat[0])
    mat = np.mat(mat)
    sum_i = mat.sum(1).tolist()
    sum_j = mat.sum(0).tolist()
    for i in range(m):
        for j in range(n):
            if mat[i, j] == 1 and sum_j[0][j] == 1 and sum_i[i][0] == 1:
                res += 1
    return res


def solution2(mat):
    matTrans = [list(x) for x in zip(*mat)]
    count = 0
    for row in mat:
        if row.count(1) != 1:
            continue

        oneIndex = row.index(1)
        if matTrans[oneIndex].count(1) == 1:
            count += 1

    return count


mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# print(b.sum(1).tolist()[0][0])
# print(b.sum(0).tolist()[0][1])
print(numSpecial(mat))
