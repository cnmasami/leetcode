# 二维区域和检索
# 给定一个二维矩阵 matrix，以下类型的多个请求：
#
# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
# 实现 NumMatrix 类：
#
# NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、
# 右下角 (row2, col2) 所描述的子矩阵的元素 总和 。
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = []

        for row in matrix:
            prefix_sum_row = [0]
            for row_el in row:
                prefix_sum_row.append(prefix_sum_row[-1] + row_el)

            self.matrix.append(prefix_sum_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0

        for row in range(row1, row2 +1):
            sum += (self.matrix[row][col2 +1] - self.matrix[row][col1])

        return sum


class D2NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.matrix = [[0] * (len(matrix[0]) + 1)] * (len(matrix) + 1)
        r = len(matrix)
        c = len(matrix[0])
        self.matrix = [[0] * (c + 1) for _ in range(r + 1)]

        for row in range(r):
            for col in range(c):

                self.matrix[row+1][col+1] = self.matrix[row][col+1] + self.matrix[row+1][col] - self.matrix[row][col] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] \
               + self.matrix[row1][col1]



a = D2NumMatrix([[-4,-5]])
print(a.sumRegion(0,0,0,0))