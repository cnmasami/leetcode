# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if not prices or k == 0:
            return 0

        buy = [-prices[0]] * k
        sell = [float("-inf")] * k

        for i in range(1, len(prices)):
            buy[0] = max(buy[0], -prices[i])
            sell[0] = max(sell[0], buy[0] + prices[i])
            for j in range(1, k):
                buy[j] = max(buy[j], sell[j-1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])


        return sell[-1]


a = Solution().maxProfit(k = 2, prices = [3,2,6,5,0,3])
print(a)

