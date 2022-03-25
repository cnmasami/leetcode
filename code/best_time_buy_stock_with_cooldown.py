# 买卖股票的最佳时机含冷冻期

# 给定一个整数数组prices，其中第prices[i]表示第i天的股票价格 。
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from typing import List


class Solution:
    # 分析状态
    # 当天有股票，当天没股票
    # 当天有股票，要么就是当天买入的，前一天冷静期，
    # 要么就前一天就买入了
    # 当天没股票，要么就是当天卖出的，
    # 要不就是冷静期
    def maxProfit(self, prices: List[int]) -> int:
        # profit = [[not_have, have, cool]]
        profit = []
        profit.append([0, -prices[0], 0])

        for i in range(1, len(prices)):
            # 当天没有股票，要么当天冷静期，要么就当天刚卖，
            # 当天冷静期的话，就是昨天刚卖，就是昨天没股票
            # 今天刚卖，就是昨天有股票+今天股票价格
            not_have = max(profit[i-1][0], profit[i-1][1] + prices[i])
            # 当天有股票，要么前一天冷静期，当天买入，
            # 要么就昨天就有股票
            have = max(profit[i-1][1], profit[i-1][2] - prices[i])
            # 当天冷静期，那利润就是昨天没有股票的利润
            cool = profit[i-1][0]

            profit.append([not_have, have, cool])

        print(profit)

        return max(profit[-1][0], profit[-1][2])

    # 官方动态规划转移
    # 官方的状态机和我的状态机不同，但是我也通过了
    # 官方fi[0]表示持有股票
    # fi[1]表示不持有股票，并在冷冻期
    # fi[2] 不持有股票，不在冷冻期
    def offical(self, prices: List[int]):
        profit = []
        profit.append([-prices[0], 0, 0])

        for i in range(1, len(prices)):
            # 当天持有股票，两种情况，1，昨天就持有profit[i-1][0]
            # 2. 今天买入的，那么昨天就是不持有并不在冷冻期，对应状态为profit[i-1][2] 加上买入股票负收益
            have = max(profit[i-1][0], profit[i-1][2] - prices[i])
            # 当天冷静期，这天冷冻期的原因是当天卖出了股票，那么在昨天必须持有一支股票，对应状态是下面
            # 这不对吧？这天是冷静期，说明是昨天卖出了股票
            cool = profit[i-1][0] + prices[i]
            # 如果当天没有股票也不在冷静期，说明当天没有任何操作，即昨天没有股票
            # 如果出于冷冻期，状态是f[i-1][1]
            # 如果不处于冷冻期，状态为f[i-1][2]
            not_have = max(profit[i-1][1], profit[i-1][2])

            profit.append([not_have, have, cool])

        return max(profit[-1][0], profit[-1][2])



a = Solution().maxProfit([2, 1, 2, 0 ,1])
print(a)

