# 组合总和
# 给你一个 无重复元素 的整数数组candidates 和一个目标整数target，
# 找出candidates中可以使数字和为目标数target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为target 的不同组合数少于 150 个。
#
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(res, path, depth):
            # depth和i相同，因为同一个元素可以反复使用，但是不能使用i之前的，因为i之前的时候，i之前加本元素组合已经尝试过了
            for i in range(depth, len(candidates)):
                path.append(candidates[i])
                # 大于或者等于target，break剪枝，后面不用再遍历
                if sum(path) > target:
                    path.pop()
                    break
                elif sum(path) == target:
                    res.append(path.copy())
                    path.pop()
                    break
                else:
                    dfs(res, path, i)
                    path.pop()

        # 先排序，方便剪枝
        candidates.sort()
        res = []
        dfs(res, [], 0)

        return res


a = Solution().combinationSum([2, 3, 6, 7], 7)
print(a)






