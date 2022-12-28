# 反转字符串中的元音字母

# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
#
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
#

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            while left < n and s[left].lower() not in vowels:
                left += 1

            while right > 0 and s[right].lower() not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)


a = Solution().reverseVowels("leEtcode")
print(a)