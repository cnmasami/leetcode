# 前K个高频单词

# 给定一个单词列表words和一个整数 k ，返回前k个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_fre = collections.Counter(words)
        # rec = list(word_fre.keys())
        # rec.sort(key=lambda x: (-1 * word_fre[x], x))
        rec = sorted(word_fre, key=lambda word: (-word_fre[word], word))
        return rec[:k]

a = Solution().topKFrequent(["i","love","leetcode","i","love","coding"], k = 3)
print(a)