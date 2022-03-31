# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # profit=[not_have, have]
        # profits = []
        # profits.append([0, -prices[0]])
        #
        # for i in range(1, len(prices)):
        #     # 今天手里没股票,要么昨天卖出,要么今天卖出
        #     not_have = max(profits[i-1][0], profits[i-1][1] + prices[i] - fee)
        #     # 今天手里有股票,要么昨天就有,要么今天刚买
        #     have = max(profits[i-1][1], profits[i-1][0] - prices[i])
        #
        #     profits.append([not_have, have])
        #
        # return profits[-1][0]

        not_have = 0
        have = -prices[0]

        for i in range(1, len(prices)):
            new_not_have = max(not_have, have + prices[i] - fee)
            new_have = max(have, not_have - prices[i])

            not_have, have = new_not_have, new_have

        return not_have


    # 贪心算法
    # 将手续费放在买入时计算
    def greedy(self, prices: List[int], fee: int) -> int:
        # 用buy表示在最大化收益的前提下,如果手上有一只股票,那么它的最低买入价格是多少
        # 初始时,buy的值为prices[0]加上手续费fee,那么当遍历到第i(i>0)天时
        buy = prices[0] + fee
        profit = 0

        for i in range(1, len(prices)):
            # 如果当前价格小于买入价格,将买入价格更新为当前价格
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            else:
                # 当前价格大于买入价格,卖出股票,获得当前收益
                # 如果持续上涨,就是最高点买入,最低点卖出相当于每日买入卖出,而手续费已经加在buy里了,所以,直接
                profit += prices[i] - buy
                buy = prices[i]

        return profit




a = Solution().maxProfit([1, 3], fee = 2)
print(a)