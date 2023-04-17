# 组合总和3

# 找出所有相加之和为n 的k个数的组合，且满足下列条件：
#
# 只使用数字1到9
# 每个数字最多使用一次
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, count, res, prev_sum, path):

            for i in range(start, 10):
                cur_sum = prev_sum + i
                if count > k or cur_sum > n:
                    break
                if k == count and cur_sum == n:
                    res.append(path + [i].copy())
                    break
                elif k == count and cur_sum > n:
                    break
                elif k == count and cur_sum < n:
                    continue
                else:
                    dfs(i+1, count+1, res, cur_sum, path+[i])

        res = []
        dfs(1, 1, res, 0, [])
        return res

a = Solution().combinationSum3(4, 1)
print(a)
