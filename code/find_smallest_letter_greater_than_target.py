# 寻找比目标字母大的最小字母

# 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
#
# 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
from bisect import bisect_right
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter

        return letters[0]

    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]



