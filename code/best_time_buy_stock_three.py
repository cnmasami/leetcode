# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
from typing import List


class Solution:
    # 这个也是不对的，这个会买卖多次
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy = prices[0]
    #     max_profit = 0
    #     prev_profit = 0
    #
    #     for price in prices[1:]:
    #         # 如果当前价格小于买入价格，把当前价格设置为买入价格
    #         if price < buy:
    #             if prev_profit != 0:
    #                 max_profit = prev_profit
    #             buy = price
    #         else:
    #             # 如果当前价格大于买入价格
    #             current = price - buy
    #             if current > prev_profit:
    #                 prev_profit = current
    #             else:
    #                 max_profit = prev_profit
    #                 buy = price
    #
    #     return max_profit + prev_profit

    # 这个根本就不对，这个是多次买入卖出
    # def dynamic(self, prices: List[int]) -> int:
    #     profit = []
    #     if len(prices) <= 1:
    #         return 0
    #     one_have, one_not_have, two_have, two_not_have = -prices[0], 0, 0, 0
    #     profit.append([one_have, one_not_have, two_have, two_not_have])
    #     # 第三天
    #     for i in range(1, len(prices)):
    #         print(prices[i])
    #         print([profit[i-1]])
    #         # 今天有股票，要么昨天就有，要么昨天没有，今天买入
    #         one_have_new = max(profit[i-1][0], profit[i-1][1] - prices[i])
    #         # 今天没股票，要么昨天就没，要么今天卖出
    #         one_not_have_new = max(profit[i-1][1], profit[i-1][0] + prices[i])
    #         if i == 1:
    #             two_have_new, two_not_have_new = 0, 0
    #         elif i == 2:
    #             # 今天有，说明昨天卖出，今天买入了
    #             two_have_new = profit[i-1][1] - prices[i]
    #             # 今天没有那昨天也没有
    #             two_not_have_new = profit[i-1][1]
    #         else:
    #             two_have_new = max(profit[i-1][2], profit[i-1][3] - prices[i])
    #             two_not_have_new = max(profit[i-1][3], profit[i-1][2] + prices[i])
    #
    #         profit.append([one_have_new, one_not_have_new, two_have_new, two_not_have_new])
    #
    #     return max(profit[-1][1], profit[-1][3])


    # todo 还是很不明白，不能同时进行多笔交易，为什么buy1和buy2要初始为同一个值呢？前两天根本就不可能发生buy2的情况啊

    # 动态规划状态机找的不对
    # 最多可以完成两笔交易，所以在一天结束，额可以出于5个状态的一种
    # 未进行过任何操作
    # 只进行过一次买入操作
    # 进行了一次买入和卖出操作，完成一笔交易
    # 完成一笔交易的前提下，进行了第二次操作
    # 完成了两笔交易
    # 第一个状态利润显然为0，可以不用记录，剩下的记录为buy1，sell1，buy2， sell2
    # 对于buy1，在第i天可以不进行任何操作，保持不变，也可以在未进行任何操作的前提下以当前价格买入股票
    # 那么buy1的状态方程为 buy1 = max(buy1', -prices[i])
    # sell1,在第i天可以不进行任何操作，保持不变，也可以在只进行过一次买入的前提下以当前价格卖出股票
    # sell1 = max(sell1', buy1’+prices[i])
    # 同理可得buy2和sell2的状态转移方程
    # 无论题目是否允许在同一天买入卖出，最终答案不会受影响，因为这一天带来的收益为0
    # 计算sell1，使，直接用buy1，而不是buy1‘进行转移，buy1比buy1’多考虑的是在第i天买入股票的情况
    # 而转移到sell1，考虑的是在第i天卖出股票的情况，这样在同一天买入并且卖出收益为0，不会对答案产生影响？
    # 同理对于buy2和sell2
    def dynamic(self, prices: List[int]):
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


    # 官方题解其实我也没太看懂，但是这个看明白了一部分吧
    # buy1 = min(buy1, prices[i])就是第一次买入的金额尽可能的低
    # sell1 = max(sell1, prices[i] - buy1) 第一次利润（卖出金额 - 买入金额）尽可能的高
    # buy2 = min(buy2, prices[i]) 第二次买入的成本尽可能的低
    # sell2 = max(sell2, prices[i] - buy2 + sell1) 第二次的利润 + 第一次的利润尽可能的高
    # 但是上面sell2是不对的
    # buy2 = min(buy2, prices[i] - sell1) 第二次买需要在第一次的基础上，那么为什么是减去sell1呢？
    # 因为sell1要尽可能的大且buy2要尽可能的小。
    # 不对，这个是因为sell其实是利润，所以第二次买需要利润 - prices，这个相当于
    # min(-buy2, sell - prices[i])
    # sell2 = max(sell2, prices[i] - buy2) 减去buy2，负负得正，那么也可以视为加上sell1？？？？？？

    def other(self, prices: List[int]):
        # buy1 = buy2 = prices[0]
        # sell1 = sell2 = 0
        # for i in range(1, len(prices)):
        #     buy1 = min(buy1, prices[i])
        #     sell1 = max(sell1, prices[i] - buy1)
        #     buy2 = min(buy2, prices[i] - sell1)
        #     sell2 = max(sell2, prices[i] - buy2)
        #
        # return sell2

        # n = len(prices)
        # buy1 = buy2 = prices[0]
        # sell1 = sell2 = 0
        # for i in range(1, n):
        #     buy1 = min(buy1, prices[i])
        #     sell1 = max(sell1, prices[i] - buy1)
        #     buy2 = min(buy2, prices[i] - sell1)
        #     sell2 = max(sell2, prices[i] - buy2)
        # return sell2

        # 按照我自己的理解又改造了一下代码，可以理解了，但是唯一不理解的就是初始化buy2也是princes[0]
        # 但是差不多又可以理解了，因为buy2后来是和sell1 - prices[i]比较的，
        # 应该不管怎样，都是sell1 - prices[i]更大一点，
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0


        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2








a = Solution().other([3,3,5,0,0,3,1,4])
print(a)


