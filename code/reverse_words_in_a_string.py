# 反转字符串中的单词 III
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []

        for c in s.split():
            ans.append(c[::-1])

        return ' '.join(ans)


a = Solution().reverseWords("God Ding")
print(a)