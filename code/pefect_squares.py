# 给你一个整数n，返回和为n的完全平方数的最少数量
# 完全平方数是一个整数，其值等于另一个整数的平方，换句话说，其值等于一个整数自乘的积
# 例如1, 4, 9和16都是完全平方数，而3和11不是
# 比如n为12，则返回3，因为12=4+4+4
import math


class Solution:
    # 动态规划
    # 可以根据题目的要求写出状态表达式f[i]表示最小需要多少个数的平方来表示整数i
    # 这些数必然落在区间[1, 根号n],可以枚举这些数，假设当前枚举到j，那么我们还需要取若干数的平方
    # 构成i-j的平方，
    # 此时该子问题和原问题类似，只是规模变小了。这符合动态规划的要求，
    # 于是可以写出状态转移方程
    # f[i] =  1 + minf[i-j2]
    # 其中f[0]=0为边界条件，实际上我们无法表示数字0，只是为了保证状态转移过程中遇到j恰为根号i的情况合法
    # 同时因为计算f[i]时所需要用到的状态仅有f[i-j的平方],必然小于i，
    # 因此，我们只需要从小到大地枚举i来计算f[i]即可
    def numSquares(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, n+1):
            minn = float('inf')
            j = 1
            while j * j <= i:
                minn = min(minn, f[i - j*j])
                j += 1

            f[i] = minn + 1

        return f[n]

    # 四平方和定理
    # 四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和
    # 同时四平方和定理包含了一个更强的结论，当且仅当n!=4的k次方 * （8m+7）时
    # n可以被表示为至多三个正整数的平方和
    # 因此，当n=4的k次方x(8m+7)时，n只能被表示为4个正整数的平方和，此时我们可以直接返回4
    # 当n！= 4的k次方 * （8m+7）时,需要判断到底多少个完全平方数能够表示n
    # 我们知道答案只会是1，2，3中的一个
    # 答案为1时，则必有n为完全平方数，这很好判断
    # 答案为2时，则有n=a的平方+b的平方，只需要枚举所有的a，判断，n-a的平方是否为完全平方数即可
    # 答案为3时，我们很难在一个优秀的时间复杂度内解决它，但我们只需要检查答案为1或2的两种情况，利用排除法确定答案
    def math(self, n: int) -> int:
        def is_perfect_square(x: int):
            y = int(math.sqrt(x))
            return y * y == x

        def check_answer_4(x: int):
            while x % 4 == 0:
                x /= 4

            return x % 8 == 7

        if is_perfect_square(n):
            return 1

        if check_answer_4(n):
            return 4

        i = 1
        while i * i <= n:
            j = n - i*i
            if is_perfect_square(j):
                return 2

        return 3


a = Solution().bfs(12)
print(a)

