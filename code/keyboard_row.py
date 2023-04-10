# 键盘行

# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
#
# 美式键盘 中：
#
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
#
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        keyboards = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for word in words:
            # line_num = 4
            for i in range(len(keyboards)):
                if word[0].lower() in keyboards[i]:
                    line_num = i
                    break

            for w in word[1:].lower():
                if w not in keyboards[line_num]:
                    break
            else:
                res.append(word)

        return res

    # 官解
    # 预处理计算了26个字符对应的行号
    def findWords2(self, words: List[str]) -> List[str]:
        res = []
        rowIdx = "12210111011122000010020202"
        for word in words:
            idx = rowIdx[ord(word[0].lower()) - ord('a')]
            if all(rowIdx[ord(ch.lower()) - ord('a')] == idx for ch in word):
                res.append(word)

        return res


a = Solution().findWords(["Hello", "Alaska", "Dad","Peace"])
print(a)