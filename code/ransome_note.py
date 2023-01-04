# 赎金信

#给你两个字符串：ransomNote 和 magazine ，
# 判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
#
# magazine 中的每个字符只能在 ransomNote 中使用一次。
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomeNote = collections.Counter(ransomNote)
        magazine = collections.Counter(magazine)

        for item in ransomeNote.keys():
            if ransomeNote.get(item) > magazine.get(item, 0):
                return False

        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        return not collections.Counter(ransomNote) - collections.Counter(magazine)

a = Solution().canConstruct('aa', 'aab')
print(a)