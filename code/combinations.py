# 组合
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(num, depth, res, path, used):
            if depth == k:
                res.append(path.copy())
                return

            # for i in range(num, n):
            for i in range(num, n - (k - len(path)) + 1):
                if not used[i]:
                    path.append(i+1)
                    used[i] = True

                    dfs(i, depth+1, res, path, used)

                    path.pop()
                    used[i] = False

        res = []
        used = [False for _ in range(n)]
        dfs(0, 0, res, [], used)

        return res


a = Solution().combine(4, 2)
print(a)

