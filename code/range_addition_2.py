# 范围求和 II
# 给你一个 m xn 的矩阵M，初始化时所有的 0 和一个操作数组 op ，
# 其中 ops[i] = [ai, bi] 意味着当所有的 0 <= x < ai 和 0 <= y < bi 时，
# M[x][y] 应该加 1。
#
# 在执行完所有操作后，计算并返回矩阵中最大整数的个数。
#
from typing import List


class Solution:
    #  最大的数重复操作最多次数，只要找到最小的行，列操作就行。
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # 一行解法
        # return mul(*map(min, zip(*ops))) if ops else m * n
        if not ops:
            return m * n

        min_x = float('inf')
        min_y = float('inf')

        for op in ops:
            min_x = min(op[0], min_x)
            min_y = min(op[1], min_y)

        return min_x * min_y


a = Solution().maxCount(18, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]])
print(a)