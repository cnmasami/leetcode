# 完美数
# 对于一个正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
#
# 给定一个整数n，如果是完美数，返回 true；否则返回 false。
#
from math import sqrt


class Solution:
    # 枚举的时候只需要枚举不超过根号num的数
    # 因为如果num有一个大于根号num的因数，那么必定有一个小于根号num的因数
    # 只要找到了较小的那个因数，可以计算出较大的那个因数
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 1

        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i * i < num:
                    sum += num / i

        return sum == num

a = Solution().checkPerfectNumber(8128)
print(a)