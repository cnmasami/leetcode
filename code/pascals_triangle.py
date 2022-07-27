# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            if i == 0:
                ans.append([1])
            else:
                level = []
                for idx in range(1, len(ans[i-1])):
                    sum_num = ans[i-1][idx-1] + ans[i-1][idx]
                    level.append(sum_num)
                level.insert(0, 1)
                level.append(1)
                ans.append(level)

        return ans

    def re_generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            row = []
            # 每行的元素个数等于行号
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j] + ret[i-1][j-1])
            ret.append(row)

        return ret




a = Solution().re_generate(5)
print(a)
