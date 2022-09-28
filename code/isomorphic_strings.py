# 同构字符串
# 给定两个字符串s和t，判断它们是否是同构的
# 如果s中的字符可以按某种映射关系替换得到t，那么这两个字符串是同构的
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序
# 不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，
# 字符可以映射到自己本身


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}

        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in s2t and s2t[x] != y:
                return False
            elif x not in s2t:
                s2t[x] = y

            if y in t2s and t2s[y] != x:
                return False
            elif y not in t2s:
                t2s[y] = x

        return True

a = Solution().isIsomorphic('paper', 'title')
print(a)


