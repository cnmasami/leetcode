# 2的幂

# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n:
            n, mod = divmod(n, 2)
            if n and mod != 0:
                return False

        return True

    # 求log2(n)，结果为整数，就表明可以
    def math_isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if math.log2(n) == int(math.log2(n)):
            return True

        return False

    # 二进制表示
    # 一个数n是2的幂，当且仅当n是正整数，并且n的二进制表示中仅包含1歌1
    # 因此可以考虑使用位运算，将n的二进制表示中最低位的那个1提取出来，再判断剩余的数值是否为0即可。
    # 有两种常见的【二进制表示中最低位】相关的位运算技巧
    # 第一个技巧是 n & (n-1)
    # & 表示按位与运算，该位运算技巧可以直接将n进制表示的最低位1移除，它的原理是：
    # 假设n的二进制表示为{a10.。。0}2，其中a表示若干个高位，1表示最低位的那个1，0.。0表示后面若干个0
    # 那么n-1的二进制表示为：{a01...1}2
    # 我们将这两个数字进行按位与运算，高位a不变，在这之后的所有位都会变为0，
    # 这样我们就将最低位的那个1移除了
    # 因此，如果n是正整数，并且n&（n-1）=0，那么n就是2的幂
    # 第二个技巧是n & （-n）
    # -n是n的相反数，为负数，由于负数是按照补码规则在计算机中存储的，
    # -n的二进制表示为n的二进制表示的每一位取反再加上1，因此它的原理为
    # 假设n的二进制表示为{a10.。。0}2，其中a表示若干个高位，1表示最低位的那个1，0.。0表示后面若干个0
    # 那么-n的二进制表示为
    # {a01...1}2 + (1)2 = a(10...0)2
    # 其中a表示将a每一位取反，我们将(a10...0)2与(a10...0)2进行按位与运算，高位全部变为0
    # 最低位的1以及之后的所有0不变，这样我们就获取了n个二进制表示的最低位的1
    # 因此，如果n是正整数，并且n & (-n) == n，那么n就是2的幂
    def binary_reprecent(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0

    # 在题目给定的32位有符号整数的范围内，最大的2的幂为2的30次方，只需要判断n是否为2的30次方的约数即可
    def math_two(self, n: int) -> bool:
        big = 2 ** 30
        return n > 0 and big % 2 == 0

    def other(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1



