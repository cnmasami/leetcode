# 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
from typing import List

# 应该是用动态规划，当前fi的最高金额应该是fi-2 + i
class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        rob = [0] * (len(nums)+ 3)

        for idx, num in enumerate(nums):
            rob[idx + 3] = max(rob[idx] + num, rob[idx+1] + num)

            ans = max(ans, rob[idx + 3])

        return ans

    # 偷K个房子有两种偷法：
    # 1：偷前K-1间房子，最后一间不偷
    # 2：偷前k-2间房子和最后一间
    # 所以动态转移公式fk = max(f(k-1), f(k-2) + hk)
    # 在写递推关系的时候，要注意写上k=0和k=1的基本情况
    # 当k=0时，没有房子，所以f0=0
    # 当k=1时，只有一个房子，偷这个房子就行所以f1=h0
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, n+1):
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])

        return dp[n]


a = Solution().rob([2,7,9,3,1])
print(a)