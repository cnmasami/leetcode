# 最长回文串
# 给定一个包含大写字母和小写字母的字符串s，返回通过这些字母构造成的最长的回文串
# 在构造过程中，请注意区分大小写，比如‘Aa’不能当作一个回文字符串
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        s_counter = collections.Counter(s)

        odd = False
        for item in s_counter.values():
            if item % 2 != 0:
                if odd:
                    ans += (item - 1)
                else:
                    ans += item
                    odd = True
            else:
                ans += item

        return ans


a = Solution().longestPalindrome('abccccdd')
print(a)