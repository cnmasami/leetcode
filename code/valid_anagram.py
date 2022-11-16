# 有效的字母异位词
# 给定两个字符串S和t,编写一个函数来判断t是否是s的字母异位词
# 若s和t中每个字符出现的次数都相同, 则称s和t互为字母异位词
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

    def sort_isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        return s == t

    def hash_isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_dict = collections.defaultdict(int)

        for i in range(len(s)):
            count_dict[s[i]] += 1
            count_dict[t[i]] -= 1

        for count in count_dict.values():
            if count != 0:
                return False

        return True


a = Solution().hash_isAnagram('bed', 'rac')
print(a)