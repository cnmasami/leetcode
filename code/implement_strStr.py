# 实现strStr()函数。
#
# 给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回 -1 。

# 说明：
# 当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当needle是空字符串时我们应当返回 0 。
# 这与 C 语言的strstr()以及 Java 的indexOf()定义相符。




class Solution:
    # I know 这道题应该用KMP，但是其实我一直不是很明白KMP
    # KMP利用已匹配部分中相同的【前缀】和【后缀】来加速下一次的匹配
    # KMP的原串指针不会进行回溯（没有暴力解法中回到下一个【发起点】的过程）
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0


