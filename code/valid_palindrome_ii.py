# 验证回文串 II
# 给你一个字符串 s，最多 可以从中删除一个字符。
#
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                # 删除 左指针指向的字符 或者 右指针指向的字符，判断 剩余的所有字符 是否可以构成回文串。
                return checkPalindrome(low+1, high) or checkPalindrome(low, high-1)

        return True


a = Solution().validPalindrome('abcaeba')
print(a)
