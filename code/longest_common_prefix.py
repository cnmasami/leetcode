# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
from typing import List


class Solution:
    # 纵向比较，暴力枚举
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        longest_num = len(strs[0])
        count = len(strs)

        for i in range(longest_num):
            for j in range(1, count):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]

        return strs[0]

    # 横向比较， 就是两两比较，先比较前两个，得出前两个的最长公共前缀，拿这个最长公共前缀和现在这个比较，
    # 得出现在这个公共前缀，和后面的依次比较，本质就是比较两个字符串的最长公共前缀
    def horizontal_compare(self, strs:List[str]) -> str:
        if not strs:
            return ''

        perfix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1

        return str1[index]


    # 分治就是 分开比较list的左边和右边，最终的最大公共子串就是两边的最大公共子串的最大公共子串
    def devide_compare(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid+1, end)
            minLength = min(len(lcpLeft), len(lcpRight))

            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) -1)


    # 最长公共前缀的长度不会超过字符串数组中最短字符串的长度，用minLength表示字符串数组中的
    # 最短字符串的长度，则可以在[0, minLength]的范围内通过二分查找得到最长公共前缀的长度。
    # 每次取查找范围的中间值mid，判断每个字符串的长度为mid的前缀是否相同，如果相同则最长公共前缀的
    # 长度一定大于或等于mid，如果不相同则最长公共前缀的长度一定小于mid，通过上述方式将查找范围缩小一半
    # 直到得到最长公共前缀的长度
    def binary_search(self, strs: List[str]) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length]== str0 for i in range(1, count))

        if not strs:
            return ''

        minLength = min(len(s) for s in strs)

        low, high = 0, minLength
        while low < high:
            mid = (high - low+1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid -1

        return strs[0][:low]


    # 这个是在题解里看到的，也是纵向比较的思路，但是他的代码要简洁的多，利用了python语言特性
    def longest(self, strs):
        res = ''
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break

        return res


    # 同一个人的题解，横向比较的思路，同样也是代码简洁的多
    def horiz(self, strs):
        if not strs:
            return ""

        res = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(res) != 0:
                res = res[0: len(res) -1]
            i += 1

        return res


    # 利用python的字符串可以比较的特性，进行排序，直接比较第一个和最后一个单词，有多少前缀相同
    def longestCommon(self, strs):
        if not strs:
            return ""

        strs.sort()

        n = len(strs)
        a = strs[0]
        b = strs[n-1]
        res = ""

        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res




a = Solution().longestCommonPrefix(["doggee","","dogae"])
print(a)



