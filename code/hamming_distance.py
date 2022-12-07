# 汉明距离
# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
#
# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离。


class Solution:
    # 异或
    def hammingDistance(self, x: int, y: int) -> int:
        r = x ^ y
        return bin(r).count('1')

    def hammingDistanceI(self, x: int, y: int) -> int:
        s = x ^ y
        ret = 0
        while s:
            ret += s & 1
            s >>= 1

        return ret

    def hammingDistanceII(self, x: int, y: int) -> int:
        s = x ^ y
        ret = 0
        while s:
            s &= s - 1
            ret += 1

        return ret

    # 模2取余，余数不等的即距离加一（也就是二进制对应位不一样）
    def hammingDistanceIII(self, x: int, y: int) -> int:
        distance = 0
        # 两个数都为0时结束
        while x or y:
            if x % 2 != y % 2:
                distance += 1
            x //= 2
            y //= 2

        return distance


a = Solution().hammingDistanceIII(1, 4)
print(a)