# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
#
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
#
# 请你计算并返回达到楼梯顶部的最低花费。
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        spend = [0] * len(cost)

        spend[0] = cost[0]
        spend[1] = cost[1]

        for i in range(2, len(cost)):
            spend[i] = min(spend[i-1] + cost[i], spend[i-2] + cost[i])

        return min(spend[-1], spend[-2])


a = Solution().minCostClimbingStairs([1,100,1,1,100,1,1,1,100,1])
print(a)