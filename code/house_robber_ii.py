# 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
from typing import List


class Solution:
    # 如果只有一间房，则偷该房屋
    # 如果有两间房，偷其中一间
    # 大于两间，需要考虑首尾相连，第一间和最后一间不能同时偷
    # 如何保证第一间和最后一间不能同时偷窃
    # 如果偷了第一间，则不能偷窃最后一间，因此偷的范围是第一间到倒数第二间
    # 如果投了最后一间，不能偷第一间，偷的范围是第二间到最后一间
    # 对于两端范围分别计算可以偷到的最高总金额，其中的最大值即为在n间房屋中可以偷窃到的最高总金额
    # 假设偷窃房屋的下标范围是[start, end]，
    # 用dp[i]表示在下标范围[start, i]内可以偷窃到的最高总金额，
    # 那么，状态转移方程：
    # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    # 边界条件：
    # dp[start] = nums[start]
    # dp[start+1] = max(nums[start], nums[start+1])
    def rob(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, length - 2), robRange(1, length - 1))


a = Solution().rob([1,2,1,1])
print(a)




