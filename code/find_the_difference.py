# 找不同
# 给定两个字符串 s 和 t ，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = collections.Counter(s)
        t = collections.Counter(t)

        return list(t - s)[0]

    # 异或
    def findTheDifference2(self, s: str, t: str) -> str:
        res = 0
        for i in s+t:
            res ^= ord(i)

        return chr(res)

    def findTheDifference3(self, s: str, t: str) -> str:
        for c in s:
            t = t.replace(c, '', 1)

        return t


# 其他方法：
# 分别对两个str进行ASCII码求和，差值就是要返回的字符
# 计数
# 首先遍历字符串 s，对其中的每个字符都将计数值加1；
# 然后遍历字符串 t，对其中的每个字符都将计数值减 1。
# 当发现某个字符计数值为负数时，说明该字符在字符串t中出现的次数大于在字符串s中出现的次数，
# 因此该字符为被添加的字符。
# 排序遍历，不同就直接返回
a = Solution().findTheDifference3('a', 'aa')
print(a)