# 二进制表示中质数个计算置位

# 给你两个整数left和right ，在闭区间 [left, right]范围内，
# 统计并返回 计算置位位数为质数 的整数个数。
#
# 计算置位位数 就是二进制表示中 1 的个数。
#


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count_bits(n):
            count = 0
            while n > 0:
                n = n & (n - 1)
                count += 1

            return count

        prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
        ans = 0

        for i in range(left, right+1):
            if count_bits(i) in prime_list:
                ans += 1

        return ans

    def countPrimesetBit2(self, left: int, right: int) -> int:
        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        return sum(isPrime(x.bit_count()) for x in range(left, right + 1))


a = Solution().countPrimeSetBits(10, 15)
print(a)