# 买卖股票的最佳时机2

# 给定一个数组 prices ，其中prices[i] 表示股票第 i 天的价格。
#
# 在每一天，你可能会决定购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
# 返回 你能获得的 最大 利润。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        prev_profit = 0

        for price in prices[1:]:
            # 如果当前价钱小于买入价钱，买入
            if price < buy_price:
                # 说明真的买入了
                if prev_profit != 0:
                    max_profit += prev_profit
                    prev_profit = 0
                buy_price = price
            else:
                # 如果当前价钱高于买入价钱，
                # 计算当前利润
                current_profit = price - buy_price
                # 如果当前利润比前一天卖出高，更新前一天利润
                if current_profit > prev_profit:
                    prev_profit = current_profit
                else:
                    # 如果当前利润比前一天卖出低，把最大利润加上前一天的利润
                    max_profit += prev_profit
                    # 重置前一天的利润，并且更新买入价格
                    prev_profit = 0
                    buy_price = price

        return max_profit + prev_profit


    # 只要第二天的价格比前一天的价格高，就将这两者之间的差计入总利润中
    # 贪心
    def offical(self, prices):
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i] - prices[i-1])

        return max_profit

    # 因为不能同时参加多笔交易，因此每天交易结束后只可能存在手里有一支股票或者没有股票的状态
    # 状态dp[i][0]表示第i天交易完后手里没有股票的最大利润
    # 状态dp[i][1]表示第i天交易完后手里有股票的最大利润
    # 如果这一天交易完后手里没有股票，那么可能的状态为前一天已经没有股票 即dp[i -1][0]
    # 或者前一天结束的时候手里有一只股票，即dp[i -1][1]
    # 这时候我们要将其卖出，并获得prices[i]的收益，
    # 为了收益最大化：
    # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    # 然后考虑dp[i][1],同样的，可能的转移状态为前一天已经持有一只股票，即dp[i-1][1],
    # 或者前一天结束时没有股票，即dp[i-1][0]，这时候我们要将其买入，并减少prices[i]的收益
    # 得出
    # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    # 对于初始状态，我们可以知道，第0天交易结束的时候
    # dp[0][0] = 0, dp[0][1] = -prices[0]
    # 因此，只要从前往后计算状态即可，由于全部交易结束，持有的股票收益一定低于不持有股票的收益
    # 因此这时候dp[n-1][0]的收益必然是大于dp[n-1][1]的，最后的答案就是dp[n-1][0]
    def dynamic(self, prices):
        # 原始版本
        # n = len(prices)
        # dp = []
        # dp.append([0, -prices[0]])
        # for i in range(1, n):
        #     no_stock = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #     one_stock = max(dp[i-1][1], dp[i-1][0] - prices[i])
        #     dp.append([no_stock, one_stock])
        #
        # return dp[n-1][0]

        # 而每一天的状态只与前一天的状态有关，而与更早的状态都无关，因此不必存储无关状态
        # 只需要存储dp[i-1][0] 和 dp[i-1][1]有关，通过它们可以计算出dp[i][0]和dp[i][1]并返回对应的变量
        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, len(prices)):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])

        return dp0



    # 题解区看到一个和我的思路一样的?，依旧代码比我的简洁
    def others(self, prices):
        buy = sell = prices[0]
        profit = 0
        for price in prices[1:]:
            if price >= sell:
                sell = price
            else:
                profit += (sell - buy)

                buy = sell = price

        return profit + (sell - buy)


a = Solution().dynamic([2, 1, 2, 0 ,1])
print(a)