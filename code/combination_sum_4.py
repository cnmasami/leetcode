# 组合总和 Ⅳ

# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
#
# 题目数据保证答案符合 32 位整数范围。
#
from typing import List


class Solution:
    # 回溯 剪枝 会超时[1, 2, 3] 32
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0

        def dfs(start, prev_sum, size):
            nonlocal ans

            for i in range(start, size):
                cur_sum = prev_sum + nums[i]
                if cur_sum > target:
                    break
                elif cur_sum == target:
                    ans += 1
                    break
                else:
                    dfs(0, cur_sum, size)

        nums.sort()
        dfs(0, 0, len(nums))

        return ans

    # 动态规划
    # 用dp[x]表示选取的元素之和等于x的方案数，目标是求dp[target]
    # 动态规划的边界是dp[0] = 1, 只有当不选取任何元素时，元素之和才为0，因此只有一种方案
    # 当1<=i<=target时，如果存在一种排列，
    # 其中的元素之和等于i，则该排列的最后一个元素一定是数组nums中的一个元素
    # 假设该排列的最后一个元素是num，则一定有num <= i,
    # 对于元素之和等于i-num的每一种排列，在最后添加num之后，即可得到一个元素之和等于i的排列
    # 因此在计算dp[i]时，应该计算所有的dp[i-num]之和
    # 由此得到动态规划的做法：
    # 1. 初始化dp[0] = 1
    # 2. 遍历i从1到target，对于每个i，进行如下操作
    #  遍历数组nums中的每个元素num，当num<=i时，将dp[i-num]的值加到dp[i]
    # 最终得到dp[target]的值即为答案
    # 上述是否考虑到选取元素的顺序？答案是肯定的，因为外层循环是遍历从1到target的值，
    # 内层循环是遍历数组nums的值，在计算dp[i]的值时，
    # nums中的每个小于等于i的元素都可能作为元素之和等于i的排列的最后一个元素
    def dp_combination_sum(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]

        return dp[target]


a = Solution().combinationSum4([4,2,1], 32)
print(a)


