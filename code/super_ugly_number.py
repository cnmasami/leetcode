# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
#
# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
#
# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
#
from typing import List


class Solution:
    # 这个方法会超时
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pointers = [1] * len(primes)
        un = [0] * (n + 1)
        un[1] = 1

        i = 2
        while i < n + 1:
            ugly_numbers = [un[pointer] * primes[idx] for idx, pointer in enumerate(pointers)]
            ugly_number = min(ugly_numbers)
            if ugly_number not in un:
                un[i] = min(ugly_numbers)
                i += 1
            cur_pointer = ugly_numbers.index(ugly_number)
            pointers[cur_pointer] += 1

        return un[n]

    def offical(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        m = len(primes)
        # 质数可更新丑数的index list
        pointers = [0] * m
        # 待更新丑数 list
        nums = [1] * m

        for i in range(1, n + 1):
            min_num = min(nums)
            dp[i] = min_num
            for j in range(m):
                if nums[j] == min_num:
                    pointers[j] += 1
                    nums[j] = dp[pointers[j]] * primes[j]

        return dp[n]


    def dp_nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i]代表第i+1个丑数
        dp = [float('inf')] * n
        dp[0] = 1
        # indexes代表每个质因子现在应该和哪个丑数相乘
        indexes = [0] * m

        for i in range(1, n):
            # 哪个质因子相乘的丑数将会变化
            change_index = 0
            for j in range(m):
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                if primes[j] * dp[indexes[j]] < dp[i]:
                    change_index = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # 如果相等就将此index直接加1，去除重复
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # 变化的坐标 + 1
            indexes[change_index] += 1

        return dp[-1]


a = Solution().offical(12, [2, 7, 13, 19])
print(a)
