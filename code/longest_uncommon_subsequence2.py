# 最长特殊序列2

#给定字符串列表strs ，返回其中 最长的特殊序列的长度。如果最长特殊序列不存在，返回 -1 。

# 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
#
# s的子序列可以通过删去字符串s中的某些字符实现。
#
# 例如，"abc"是 "aebdc"的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc"。
# "aebdc"的子序列还包括"aebdc"、 "aeb"和 ""(空字符串)。
from typing import List


class Solution:
    # 首先，一个字符串的子序列如果不是其他字符串的子序列，那么这个字符串本身也一定不是
    # 因为包含这个字符串本身的，一定也能包含它的任意子序列
    # 所以题目变为从字符串数组中找最长的一个原字符串，该字符串不是其他字符串的子序列
    # 根据数据范围，暴力模拟判断即可
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s: str, t: str):
            pt_s = pt_t = 0
            while pt_s < len(s) and pt_t < len(t):
                if s[pt_s] == t[pt_t]:
                    pt_s += 1
                pt_t += 1

            return pt_s == len(s)

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                # 判断s是不是t的子字符串，因为双重for循环，s和t的顺序总会反过来的
                if i != j and is_subseq(s, t):
                    check = False
                    break
            if check:
                ans = max(ans, len(s))

        return ans


a = Solution().findLUSlength(["aaa","aaa","aa"])
print(a)


