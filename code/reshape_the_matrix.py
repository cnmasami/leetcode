# 重塑矩阵

# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
#
# 给你一个由二维数组 mat 表示的m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
#
# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
#
# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
#
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_num = len(mat) * len(mat[0])
        if mat_num != r * c:
            return mat
        else:
            # ans = []
            # srow = []
            #
            # for row in mat:
            #     for col in row:
            #         srow.append(col)
            #         if len(srow) == c:
            #             ans.append(srow.copy())
            #             srow = []
            #
            # return ans
            ans = [[0] * c for _ in range(r)]
            for x in range(len(mat) * len(mat[0])):
                ans[x // c][x % c] = mat[x // len(mat[0])][x % len(mat[0])]

            return ans


a = Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4)
print(a)
