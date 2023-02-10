# 匹配子序列的单词数

#
# 给定字符串 s和字符串数组words, 返回words[i]中是s的子序列的单词个数。
#
# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，
# 而不改变其余字符的相对顺序。
#
# 例如， “ace” 是 “abcde” 的子序列。
from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_len = len(s)
        dp = [[0] * 26 for _ in range(s_len)]
        dp.append([s_len] * 26)

        for i in range(s_len - 1, -1, -1):
            for j in range(26):
                if j == ord(s[i]) - ord('a'):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j]

        count = 0
        for word in words:
            add = 0
            count_add = 1
            for c in word:
                if dp[add][ord(c) - ord('a')] == s_len:
                    count_add = 0
                    break
                else:
                    add = dp[add][ord(c) - ord('a')] + 1

            count += count_add

        return count

    # 二分查找
    # 构造一个字典
    # 字典的键是s中的所有的单个字符
    # 值是这个字符在s中出现的索引从小到大排序
    # 对于需要匹配的字符串中的单个字符
    # 可以通过对应的pos数组中进行二分查找来找到第一个大于当前idx的位置
    # 如果不存在说明匹配不成功
    # 否则就将s的指针直接移动到找到的这个位置
    # 将w的指针往后移动一位
    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for idx, char in enumerate(s):
            pos[char].append(idx)

        ans = len(words)
        for w in words:
            if len(w) > len(s):
                ans -= 1
                continue
            p = -1
            for c in w:
                ps = pos[c]
                j = bisect_right(ps, p)
                if j == len(ps):
                    ans -= 1
                    break
                p = ps[j]

        return ans

    # 多指针
    # 是针对是否是子字符串的双指针方法的优化
    # 将字符串数组words中的全部字符串和字符串s同时进行匹配
    # 分桶
    # 将words中所有的单词根据首字母来分桶，
    # 即：把所有单词按照首字母分到26个桶中，
    # 每个桶中存储的是该字母开头的所有单词【本题解换成了在words中的索引】
    # 比如对于words=['a', 'bb', 'acd', 'ace'], 得到的分桶结果如下:
    # a: ['a', 'acd', 'ace']
    # b: ['bb']
    # 然后我们从s的第一个字符开始遍历，假设当前字符为'a',
    # 从a开头的桶中取出所有单词。
    # 对于取出的每个单词，如果此时单词长度为1，说明该单词已经匹配完毕，将答案加一
    # 否则，我们将单词的首字母去掉，然后放入下一个字母开头的桶中
    # 比如对于单词‘acd’， 去掉首字母'a'之后，我们将其放入c开头的桶中
    # 这一轮结束后，分桶结果变为：
    # c:['cd', 'ce']
    # b:['bb']
    # 遍历结束得到答案
    def numMatchingSubseq3(self, s: str, words: List[str]) -> int:
        p = defaultdict(list)
        for idx, word in enumerate(words):
            p[word[0]].append((idx, 0))

        ans = 0
        for c in s:
            # 以c为开头的字符串出现的位置在构造的p桶中删除了
            q = p[c]
            p[c] = []
            for idx, sub_idx in q:
                sub_idx += 1
                if sub_idx == len(words[idx]):
                    ans += 1
                else:
                    p[words[idx][sub_idx]].append((idx, sub_idx))

        return ans


a = Solution().numMatchingSubseq3(s = "abcde", words = ["a","bb","acd","ace"])
print(a)


