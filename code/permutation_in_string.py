#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字符串的排列
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
import collections


class Solution:
    # 我能想到的就是暴力解法，会超时
    # 其实也没有必要排序，就是如果a是b的一个排列，那么他们两个类里面每个字符的个数完全相等
    # 所以用滑动窗口+字典来解决
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for i in range(len(s2)):
        #     sub_s2 = s2[i:i+len(s1)]
        #     if sorted(s1) == sorted(sub_s2):
        #         return True
        #
        # return False
        # 换一种解法不会超时，但是很慢
        counter_s1 = collections.Counter(s1)
        for i in range(len(s2)):
            sub_s2 = s2[i:i + len(s1)]
            if counter_s1 == collections.Counter(sub_s2):
                return True

        return False

    # 然后这是别人用滑动窗口 + 字典的写法
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        counter_s1 = collections.Counter(s1)
        left = 0
        right = len(s1) - 1
        counter_s2 = collections.Counter(s2[left: right])

        while right < len(s2):
            counter_s2[s2[right]] += 1

            if counter_s1 == counter_s2:
                return True

            counter_s2[s2[left]] -= 1

            if counter_s2[s2[left]] == 0:
                del counter_s2[s2[left]]

            left += 1
            right += 1

        return False
