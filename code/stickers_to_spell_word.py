# 贴纸拼词

# 我们有n中不同的贴纸，每个贴纸上都有一个小写的英文单词
# 您想要拼写出给定的字符串 target，方法是从收集的贴纸中切割单个字母并重新排列它们。
# 如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
#
# 返回你需要拼出 target的最小贴纸数量。如果任务不可能，则返回 -1 。
#
# 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，
# 并且 target被选择为两个随机单词的连接。
#
import collections
# from functools import cache
from typing import List


class Solution:
    # def minStickers2(self, stickers: List[str], target: str) -> int:
    #     m = len(target)
    #
    #     @cache
    #     def dp(mask: int) -> int:
    #         if mask == 0:
    #             return 0
    #         res = m + 1
    #         for sticker in stickers:
    #             left = mask
    #             cnt = collections.Counter(sticker)
    #             for i, c in enumerate(target):
    #                 if mask >> i & 1 and cnt[c]:
    #                     cnt[c] -= 1
    #                     left ^= 1 << i
    #             if left < mask:
    #                 res = min(res, dp(left) + 1)
    #
    #         return res
    #     res = dp((1 << m) -1)
    #     return res if res <= m else -1

    # 从target出发【起始状态】，使用每个贴纸去掉对应个数的字母【状态转移】，
    # 看最终能否出现空字符串【目标状态】。
    # 优化: 优先从左往右去掉当前状态中的字符，减少排列组合情况。
    # (比如我们删1次stickers[0]同时删1次stickers[1]，就有两个顺序达到同样的效果)
    # 【大白话就是先删a后删b，和先删b后删a一样，我们在乎的是选了ab，而不是排列ab】
    #
    def minStickers3(self, stickers: List[str], target: str) -> int:
        # 计算s中target的字符的个数
        def trans(s):
            cnts = collections.Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1

            return cnts

        # 每个sticker可以替换target的字符以及个数
        availables = [trans(st) for st in stickers if trans(st)]
        # 初始状态 target 0次
        queue = collections.deque([(target, 0)])
        # 记录遍历过的
        explored = {target}
        while queue:
            cur, step = queue.popleft()
            # 达成空字符目标，返回次数（也就是最小贴纸数量）
            if not cur:
                return step
            for avl in availables:
                # 如果目标的第一个字符不在贴纸中，直接跳过
                if cur[0] in avl:
                    nxt = cur
                    for k, v in avl.items():
                        # 把K替换掉，替换v次
                        nxt = nxt.replace(k, '', v)
                    # 这时nxt是新的目标了，如果此前没有被遍历过，那么加入到队列中处理
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt, step + 1))

        return -1

    # 感觉这个可以简化成3吧
    def minStickers4(self, stickers: List[str], target: str) -> int:
        stickers_counter = [collections.Counter(sticker) for sticker in stickers]

        dp = {}

        def dfs(t, sticker):
            if t in dp:
                return dp[t]
            ret = 1 if sticker else 0
            reminder = ''

            for c in t:
                if c in sticker and sticker[c] > 0:
                    sticker[c] -= 1
                else:
                    reminder += c

            if reminder:
                used = float('inf')
                for sticker_counter in stickers_counter:
                    if reminder[0] not in sticker_counter:
                        continue
                    used = min(used, dfs(reminder, sticker_counter.copy()))
                dp[reminder] = used
                ret += used

            return ret

        ret = dfs(target, {})

        return ret if ret != float('inf') else -1


a = Solution().minStickers3(["these","guess","about","garden","him"], "atomher")
print(a)