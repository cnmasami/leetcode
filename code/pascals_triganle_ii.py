# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1]


        prev_row = [1]

        for i in range(1, rowIndex + 1):
            row = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev_row[j-1] + prev_row[j])
            prev_row = row

        return prev_row

    # 使用一个数组，由于当前行第i项的计算只与上一行第i-1项及第i项有关，
    # 可以倒着计算当前行，这样计算到第i项时，第i-项仍然是上一行的值
    def offical_getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j-1]

        return row

    # 根据计算公式来算
    def math_getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            row.append(row[i-1] * (rowIndex + 1 - i) // i)

        return row



a = Solution().offical_getRow(3)
print(a)