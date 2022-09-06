# 给你一个整数n，请你找出并返回第n个丑数
# 丑数就是只包含质因数2，3，和/或 5的正整数

# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
import heapq


class Solution:
    # 最小堆
    # 1. 起先将最小丑数1放入队列
    # 2. 每次从队列取出最小值x，然后将x所对应的丑数2x，3x，和5x进行入队
    # 3. 对步骤2循环多次，第n次出队的值即是答案
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n-1):
            curr = heapq.heappop(heap)
            for factor in factors:
                next = curr * factor
                if next not in seen:
                    seen.add(next)
                    heapq.heappush(heap, next)

        return heapq.heappop(heap)

    # 我们先模拟手写丑数的过程
    # 1 打头，1 乘 2 1 乘 3 1 乘 5，现在是 {1,2,3,5}
    # 轮到 2，2 乘 2 2 乘 3 2 乘 5，现在是 {1,2,3,4,5,6,10}
    # 手写的过程和采用小顶堆的方法很像，但是怎么做到提前排序呢
    #
    # 小顶堆的方法是先存再排，dp 的方法则是先排再存
    # 我们设 3 个指针 p_2,p_3,p_5
    # 代表的是第几个数的2倍、第几个数 3 倍、第几个数 5 倍
    # 动态方程 dp[i]=min(dp[p_2]*2,dp[p_3]*3,dp[p_5]*5)
    # 小顶堆是一个元素出来然后存 3 个元素
    # 动态规划则是标识 3 个元素，通过比较他们的 2 倍、3 倍、5 倍的大小，来一个一个存
    def dynamic_nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n+1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]

    def test(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1



a = Solution().nthUglyNumber(10)
# a = Solution().dynamic_nthUglyNumber(10)
print(a)