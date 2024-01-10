#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for sr in strs:
            key = ''.join(sorted(sr))
            mp[key].append(sr)

        return list(mp.values())


    def groupAnagrams_counter(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            mp[tuple(counts)].append(st)

        return list(mp.values())


