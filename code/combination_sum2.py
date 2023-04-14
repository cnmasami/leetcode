# 组合总和 II
# 给定一个候选人编号的集合candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
#
# candidates中的每个数字在每个组合中只能使用一次
#
# 注意：解集不能包含重复的组合。
#

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, size, path, res, prev_sum):

            for i in range(idx, size):
                if not used[i]:
                    if i > 0 and candidates[i] == candidates[i-1] and not used[i-1]:
                        continue

                    cur_sum = prev_sum + candidates[i]

                    if cur_sum == target:
                        res.append(path + [candidates[i]].copy())
                        break
                    elif cur_sum > target:
                        break
                    else:
                        used[i] = True
                        dfs(i+1, size, path + [candidates[i]], res, cur_sum)
                        used[i] = False

        # 先排序，方便剪枝
        candidates.sort()
        size = len(candidates)
        used = [False] * size
        res = []
        dfs(0, size, [], res, 0)

        return res

    # 别人的剪枝方法
    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, size, path, res, prev_sum):

            for i in range(idx, size):
                # if not used[i]:
                # 同一层结点，如果上一层加上的数相同，只需要保留第一个分支的结果
                # 因为后面的分支，候选数是第一个分支的真子集，在第一个分支中已经搜索过了
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                cur_sum = prev_sum + candidates[i]

                if cur_sum == target:
                    res.append(path + [candidates[i]].copy())
                    break
                elif cur_sum > target:
                    break
                else:
                    # used[i] = True
                    dfs(i+1, size, path + [candidates[i]], res, cur_sum)
                    # used[i] = False

        # 先排序，方便剪枝
        candidates.sort()
        size = len(candidates)
        # used = [False] * size
        res = []
        dfs(0, size, [], res, 0)

        return res



a = Solution().combinationSum22([2,5,2,1,2], 5)
print(a)

