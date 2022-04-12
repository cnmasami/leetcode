# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

from functools import lru_cache


class Solution:
    @lru_cache()
    # 我们可以通过在 n-1 阶的那块一次性爬 1 步来达到 n 楼层，以及通过在 n - 2 阶 一次性爬 2 步来达到 n 楼层。
    # 所以就是这两种情况的总和。
    def climbStairs(self, n: int) -> int:
        # n的方法是 （n-1） + 1 这是一种可能性，因为他只能迈一步
        # n的方法是 （n-2） + 2 这是一种可能性，因为他如果迈在 n-1上，再迈一步就是上面的这种可能性
        if n == 1:
            return 1
        if n == 2:
            return 2

        total = self.climbStairs(n -2) + self.climbStairs(n -1)

        return total


a = Solution().climbStairs(9)
print(a)