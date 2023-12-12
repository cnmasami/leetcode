#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字符的最短距离

# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
#
# 返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。
#
# 两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
from typing import List


class Solution:
    # 问题可以转换为，对s的每个下标i，求s[i]到其左侧最近的字符c的距离，和s[i]到其右侧最近的字符c的距离的最近距离
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_index_left = c_index = s.find(c)
        res = [(c_index - i) for i in range(0, c_index + 1)]

        c_index_right = s.find(c, c_index + 1)

        while c_index_right != -1:
            res.extend([min(abs(c_index_left -i), abs(c_index_right -i)) for i in range(c_index_left +1, c_index_right + 1)])
            c_index_left = c_index_right
            c_index_right = s.find(c, c_index_left + 1)
        else:
            res.extend([abs(c_index_left - i) for i in range(c_index_left+1, len(s))])

        return res

    # 两次遍历， 从左往遍历，若s[i] = c 则记录此时字符c的下标idx，同时更新answer[i] = i - idx
    # 从右往左遍历，若s[i] = c 则记录此时字符c的下标idx，同时更新answer[i] = min(answer[i], idx -i)
    # 初始的时候idx不存在，用-n或者2n表示
    # 因为最后要取min值。用idx = -n， 假如s不存在c（实际题目s一定存在c），
    # i-idx 就大于等于n，就是表示距离超过了n（即不可达）。取-n和2n是为了方便后面求最小值！
    def shortestToChar_2iter(self, s: str, c: str):
        n = len(s)
        ans = [0] * n

        idx = -n
        for i, ch in enumerate(s):
            if ch == c:
                idx = i
            ans[i] = i - idx

        idx = 2*n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx -i)

        return ans



a = Solution().shortestToChar(s = "loveleetcode", c = "e")
print(a)



