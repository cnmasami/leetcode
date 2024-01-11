#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
import collections


class Solution:
    # 会超时
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        ans = s+t
        counter_t = collections.Counter(t)
        left = 0
        right = len(t)

        while right < len(s) + 1:
            if counter_t - collections.Counter(s[left:right]):
                right += 1
            else:
                if len(ans) > (right - left):
                    ans = s[left: right]

                left +=1

        return '' if ans == s+t else ans

    def minWindow2(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        ans = s+t
        counter_t = collections.Counter(t)
        left = 0
        right = len(t) - 1
        counter_s = collections.Counter(s[left:right + 1])

        while right < len(s):
            if counter_t - counter_s:
                right += 1
                if right < len(s):
                    counter_s[s[right]] += 1
            else:
                if len(ans) > (right - left + 1):
                    ans = s[left: right+1]

                counter_s[s[left]] -= 1
                left += 1

        return '' if ans == s+t else ans



a = Solution().minWindow2(s="ADOBECODEBANC", t="ABC")
print(a)




