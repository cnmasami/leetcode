# 托普利茨矩阵

# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
#
# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        # 只需要遍历第一行和第一列就可以
        # 遍历第一行,第一行的i其实是列
        for i in range(col):
            x = 0
            y = i
            while x < row and y < col:
                if matrix[x][y] != matrix[0][i]:
                    return False
                x += 1
                y += 1


        # 遍历第一列
        for j in range(1, row):
            x = j
            y = 0
            while x < row and y < col:
                if matrix[x][y] != matrix[j][0]:
                    return False
                x += 1
                y += 1

        return True

    # 官方，根据题意，当且仅当矩阵中每个元素都与其左上角相邻元素相等时，该矩阵为托普利兹矩阵
    # 因此遍历该矩阵，将每一个元素与它左上角的元素相比对即可
    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True


a = Solution().isToeplitzMatrix([[1,2],[2,2]])
print(a)

