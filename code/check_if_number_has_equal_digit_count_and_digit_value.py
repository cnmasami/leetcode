# 判断一个数的数字计数是否等于数位的值

# 给你一个下标从 0开始长度为 n的字符串num，它只包含数字。
#
# 如果对于 每个0 <= i < n的下标i，都满足数位i在 num中出现了num[i]次，那么请你返回true，
# 否则返回false。
#
import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        # counts = collections.Counter(num)
        # for idx, val in enumerate(num):
        #     if counts[str(idx)] != int(val):
        #         return False
        for idx, val in enumerate(num):
            if int(val) != num.count(str(idx)):
                return False

        return True

a = Solution().digitCount("030")
print(a)