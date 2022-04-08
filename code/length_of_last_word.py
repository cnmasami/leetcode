# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 这个用python内置函数就可以了
        return len(s.strip().split(' ')[-1])


a = Solution().lengthOfLastWord("luffy")
print(a)