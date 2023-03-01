# 排列硬币
# 你总共有n枚硬币，并计划将它们按阶梯状排列。
# 对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

# 给你一个数字n ，计算并返回可形成 完整阶梯行 的总行数。
#

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            k = left + (right - left + 1) // 2
            sum = (k+1) * k // 2
            if sum == n:
                return k
            elif sum > n:
                right = k - 1
            else:
                left = k

        return left

    # 数学方法，求解方程 (x+1)* x // 2 = n
    # 就是x ** 2 + x - 2n = 0
    # 根据求根公式，x = b的平方 -4ac
    # 而n是大于等于1的，所以b的平方 -4ac > 0
    # 也就是说8n+1>0
    # 而根是整数，所以，根的数学公式是 (-1 + 根号下(8n+1)) // 2
    def arrangeCoins_math(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) -1) / 2)


a = Solution().arrangeCoins(1)
print(a)
