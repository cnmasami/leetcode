# 计数二进制子串

# 给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，
# 并且这些子字符串中的所有 0 和所有 1 都是成组连续的。
#
# 重复出现（不同位置）的子串也要统计它们出现的次数。
import collections


class Solution:
    # 其实我的思路和官解的思路本质是一样的，但官解是巧妙版
    def countBinarySubstrings(self, s: str) -> int:
        count_dict = collections.Counter()
        ans = 0

        prev = s[0]
        count_dict[int(prev)] += 1

        for sub_s in s[1:]:
            if sub_s == prev:
                count_dict[int(sub_s)] += 1
            elif sub_s != prev:
                count_dict[int(sub_s)] = 1

            if count_dict[int(sub_s)^1] >= count_dict[int(sub_s)]:
                ans += 1

            prev = sub_s

        return ans

    # 官解：
    # 将字符串按照0和1的连续段分组，存在counts数组中，例如s=00111011
    # 可以得到这样的counts数组：counts={2, 3, 1, 2}
    # 这里counts数组中两个相邻的数字为u或者v，它们对应这u个0和v个1
    # 能组成的满足条件的字串数目是min{u, v}，即一对相邻的数字对答案的贡献
    def countBinarySubstrings_offical(self, s:str) -> int:
        count = [1]
        j = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count[j] += 1
            else:
                count.append(1)
                j += 1

        res = 0
        for k in range(1, len(count)):
            res += min(count[k], count[k-1])

        return res

    # 官解优化版
    def countBinarySubstrings_offical2(self, s: str) -> int:
        n = len(s)
        ptr = last = ans = 0

        while ptr < n:
            c = s[ptr]
            count = 0
            while ptr < n and s[ptr] == c:
                ptr += 1
                count += 1

            ans += min(count, last)
            last = count

        return ans


a = Solution().countBinarySubstrings("10101")
print(a)
