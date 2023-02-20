# 最好的扑克手牌
# 给你一个整数数组ranks和一个字符数组suit。你有5张扑克牌，第i张牌大小为ranks[i]，花色为suits[i]。
#
# 下述是从好到坏你可能持有的 手牌类型：
#
# "Flush"：同花，五张相同花色的扑克牌。
# "Three of a Kind"：三条，有 3 张大小相同的扑克牌。
# "Pair"：对子，两张大小一样的扑克牌。
# "High Card"：高牌，五张大小互不相同的扑克牌。
# 请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型。
#
# 注意：返回的字符串大小写需与题目描述相同。
#
import collections
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits_set = set(suits)
        rank_set = set(ranks)

        if len(suits_set) == 1:
            return 'Flush'
        elif len(rank_set) == 5:
            return 'High Card'
        else:
            rank_count = collections.Counter(ranks)
            rank_sorted = sorted(rank_count.items(), key=lambda k: k[1], reverse=True)

            for rank in rank_sorted:
                if rank[1] >= 3:
                    return 'Three of a Kind'
                elif rank[1] == 2:
                    return 'Pair'


    def simplify(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'

        counter = collections.Counter(ranks)

        if len(counter) == 5:
            return 'High Card'

        if any(cnt >= 3 for cnt in counter.values()):
            return 'Three of a kind'

        return 'Pair'

a = Solution().bestHand(ranks = [1,1,1,2,2], suits = ["a","b","c","a","d"])
print(a)