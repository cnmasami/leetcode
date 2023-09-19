# 旋转矩阵

# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
#
# 不占用额外内存空间能否做到？
#
#
import copy
from typing import List


class Solution:
    # 可以找到规律
    # 第i行元素旋转到第n-1-i列 元素
    # 第j列元素旋转到第j行元素
    # 对于矩阵任意第i行，第j列元素matrix[i][j]，矩阵旋转90度后
    # matrix[i][j] -> matrix[j][n-1-i]
    # 根据元素旋转公式，遍历矩阵，将各元素依次写入到旋转后的索引位置，但仍存在问题
    # 直接写入原矩阵元素会被覆盖，因此丢失的元素无法被写入旋转后的索引位置
    # 为解决问题，需要借助辅助矩阵暂存原矩阵
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        tmp = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 -i] = tmp[i][j]


    # 不借助辅助矩阵，通过在原矩阵中直接原地修改
    # 以矩阵四个角点的元素为例，设左上角A,右上角B，右下角C，右下角D,
    # 旋转90度之后，相当于先后执行D->A, C->D, B-> C, A->B修改元素
    # 顺序相当于A <- D <- C <- B <- A
    # 由于第一步A被覆盖，无法导致最后一步A->B赋值，可以借助辅助变量tmp预先存储A，
    # A <- D <- C <- B <- tmp
    # 一轮可以完成矩阵 4 个元素的旋转。因而，只要分别以矩阵左上角 1/4的各元素为起始点执行以上旋转操作，即可完整实现矩阵旋转。
    # 具体来看，当矩阵大小 n 为偶数时，取前 n/2行、前 n/2列的元素为起始点；当矩阵大小 nnn 为奇数时，取前 n/2行、
    # 前 n+1/2列的元素为起始点。
    def rotate_inplace(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp

    # 翻转代替旋转，先通过水平翻转，再根据主对角线翻转
    def rotate_flip(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i -1][j] = matrix[n-i-1][j], matrix[i][j]

        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


