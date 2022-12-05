# 3的幂
# 给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        t = 1
        while t < n:
            # 也可以写成t = (t << 1) + t
            # 因为t*3 = t*(2+1) =  t* 2 +  t
            t = t * 3

        return t == n


    def isPowerOfThreeII(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //=3

        return n == 1



a = Solution().isPowerOfThreeII(2)
print(a)