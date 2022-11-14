# 位1的个数
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），
# 返回其二进制表达式中数字位数为‘1’的个数（也被成为汉明重量）

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    # 直接循环检查给定整数n的二进制位的每一位是否为1
    # 具体代码中，当检查第i位时，我们可以让n与2的i次方进行与运算，当且仅当n的第i位为1时，运算结果不为0
    def iter_hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret

    # n & (n-1)，其运算结果恰为把n的二进制位中的最低位的1变为0之后的结果
    # 如:6 & (6-1) = 4, 6 = (110)2, 4 = (100)2, 运算结果4即为把6的二进制中的最低位的1变为0之后的结果
    # 这样我们可以利用这个位运算的性质加速我们的检查过程, 在实际代码中, 我们不断让当前的n与n-1做与运算,
    # 直到n变为0即可.
    # 因为每次运算会使得n的最低位的1被翻转,因此运算次数就等于n的二进制位中的1的个数
    def opt_bin_hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n -1
            ret += 1

        return ret