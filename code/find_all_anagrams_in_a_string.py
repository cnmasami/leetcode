#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 找到字符串中所有字母异位词

# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，
# 返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = collections.Counter(p)
        left = 0
        right = len(p) - 1
        s_counter = collections.Counter(s[left: right])
        ans = []

        while right < len(s):
            s_counter[s[right]] += 1

            if s_counter == p_counter:
                ans.append(left)

            s_counter[s[left]] -= 1

            if s_counter[s[left]] == 0:
                del s_counter[s[left]]

            left += 1
            right += 1

        return ans


a = Solution().findAnagrams(s = "abab", p = "ab")
print(a)
