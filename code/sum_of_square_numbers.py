# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a平方 + b平方 = c 。


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = 0

        while c > 0:
            c -= x
            x += 2

        return c == 0


a = Solution().judgeSquareSum(5)
print(a)