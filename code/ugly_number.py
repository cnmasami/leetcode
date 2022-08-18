# 丑数 就是只包含质因数 2、3 和 5 的正整数。
#
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

class Solution:
    # 根据题意，当n是整数，n = 2的a次方 * 3的b次方 * 5的c次方
    # 所以，对n反复的除以2，3，5，如果剩下的数是1，说明不包含其他质因数
    # 否则，说明n包含其他质因数，不是丑数
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2

        while n % 3 == 0:
            n = n // 3

        while n % 5 == 0:
            n = n // 5

        return n == 1


a = Solution().isUgly(6)
print(a)



