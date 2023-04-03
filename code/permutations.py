# 全排列

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return

            for i in range(size):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True

                    print('递归之前', depth, i, path)
                    dfs(nums, size, depth + 1, path, used, res)
                    print('递归之后', depth, i, path)

                    path.pop()
                    used[i] = False

        if not nums: return []

        size = len(nums)

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)

        return res

    # 库函数
    def permute2(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


a = Solution().permute2([1, 2, 3])
print(a)