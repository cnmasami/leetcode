# 判断子序列

#给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
# （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，
# 你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


class Solution:
    # 双指针
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        return s_index == len(s)

    # 动态规划
    # 预处理出对于t的每一个位置，从该位置开始往后每一个字符第一次出现的位置
    # 可以使用动态规划的方法实现预处理，
    # 令f[i][j]表示字符串t中从位置i开始往后字符j第一次出现的位置
    # 在进行状态转移时，如果t中位置i的字符就是j，那么f[i][j]=i
    # 否则j出现在位置i+1开始往后，即f[i][j]=f[i+1][j]
    # 因此我们要倒过来进行动态规划，从后往前枚举i
    # 这样可以写出状态转移方程
    # f[i][j] = i when t[i] = j
    # f[i][j] = f[i+1][j] when t[i] != j
    # 假定下标从0开始，那么f[i][j]中有0 <= i <= len(s)-1
    # 对于边界状态f[len(t) -1][..],
    # 我们置f[len(t)][..]为len(t)，让f[len(t) -1][..]可以正常进行转移
    # 这样如果f[i][j]=len(t)，则表示从位置i开始往后不存在字符j
    # 这样，可以利用f数组，每次o(1)地跳转到下一格位置，直到位置变为len(t)或者s中的每一个字符都匹配成功
    # 该解法中，对t的处理和s无关，且预处理完成后，可以利用预处理数组的信息，
    # 线性地算出任意一个字符串s是否为t的子串，
    def dp_isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        # 构造边界状态转移
        f.append([m] * 26)

        for i in range(m-1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]

        add = 0

        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True

a = Solution().dp_isSubsequence(s = "abc", t = "ahbgdc")
print(a)





