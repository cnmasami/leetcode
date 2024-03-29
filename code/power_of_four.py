# 4的幂
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n and n % 4 == 0:
            n //= 4

        return n == 1

    # 如果n是4的幂则必然是2的幂
    # 然后在此基础上再判断是不是4的幂
    # 如果是4的幂，那么二进制中只有一个1，并且这个1出现在从低位开始的第偶数个二进制位上
    # 为什么是偶数，因为4是2的2次方，所以任何4的幂都可以表示为2的2n次方
    # 必在偶数位上
    # 所以我们可以构造一个整数mask，它的所有偶数二进制位都是0
    # 奇数二进制位都是1，这样一来，将n和mask按位与运算，可以得到0
    # 说明n二进制中1出现在偶数为止，否则出现在奇数位置，这样的mask为
    # (10101010101010101010101010101010)2
    # 十六进制为(AAAAAAAA) 16
    def bitpos(self, n: int) -> bool:
        return n > 0 and (n & (n -1)) == 0 and (n & 0xaaaaaaaa) == 0


    # 如果n是4的幂，那么 4的x次方 = (3 + 1)的x次方
    # (3+1) ^x利用二项式定理展开，除了1^x这一项之外，剩下的每一项都含有因子3，因此将(3+1)^x对3取余的结果一定等于1^x，也就是一定等于1
    # 那么它除以3的余数一定为1
    # 如果n是2的幂却不是4的幂，那么它可以表现为4的x次方*2
    # 此时它除以3的余数一定为2
    # 所以可以通过n除以3的余数是否为1来判断n是否是4的幂
    def mod(self, n: int) -> bool:
        return n > 0 and (n & (n -1)) == 0 and n % 3 == 1
