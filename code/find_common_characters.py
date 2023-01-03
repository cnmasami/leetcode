# 查找共用字符

# 给你一个字符串数组 words ，
# 请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），
# 并以数组形式返回。你可以按 任意顺序 返回答案。
#
import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = None
        for word in words:
            # 不能写if ans else 不然空的Counter也会走这个分支
            if ans is None:
                ans = collections.Counter(word)
            else:
                ans = ans & collections.Counter(word)

        return list(ans.elements())


a = Solution().commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"])
print(a)
