# 颠倒给定的32位无符号整数的二进制位


class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0

        for i in range(32):
            # 先得到n的二进制最低位数字
            low_bit = n & 1
            # 先把结果数字左移1位, 再将得到的二进制位添加到结果的最低位
            # 这样得到的结果就是n的最低位在ret的最高位
            ret = ret << 1 | low_bit
            # 将n右移一位
            n = n >> 1

        return ret

    # 位运算分治
    # 要翻转一个二进制串, 可以将其均分成左右两部分, 对每部分递归执行翻转操作,
    # 然后将左半部分拼在右半部分的后面, 即完成了翻转
    # 由于左右两部分的计算方式相似,利用位掩码和位移运算,自底向上地完成这一分治流程
    # 对于递归的最底层,需要交换所有奇偶位
    # 1. 取出所有奇数位和偶数位
    # 2. 将奇数位移到偶数位上, 偶数位移到奇数位上
    # 对于倒数第二层,每两位分一组,按组号取出所有奇数组和偶数组,然后将奇数组移到偶数组上,偶数组移到奇数组上
    # 依次类推, 比如
    # 原数据为:12345678
    # 第一轮 奇偶位交换 21436587
    # 第二轮 每两位交换 43218765
    # 第三轮 每四位交换 87654321
    def div_reverseBits(self, n: int) -> int:
        # 01010101010101010101010101010101
        m1 = 0x55555555
        # 00110011001100110011001100110011
        m2 = 0x33333333
        # 00001111000011110000111100001111
        m4 = 0x0f0f0f0f
        # 00000000111111110000000011111111
        m8 = 0x00ff00ff
        # 首先，我们知道 （单个二进制码 & 1) = 其本身，所以对于参数 M1，可以看成是用来将一串二进制码的奇数位提取出来；
        # 接着，n >> 1，右移，可以看作是将 n 上原来的偶数位变成奇数位，为什么不说奇数位也变成偶数位，是因为右移将第一个奇数位移除了；
        # 其次，(n >> 1) & M1，就是如1所述，将（n >> 1）的奇数位提取出来，也就是原 n 的偶数位；
        # 再次，(n & M1) << 1，就是先将 n 的奇数位提出来，然后左移，将其变成偶数位；
        # 然后，奇数位(原 n 的偶数位) | 偶数位(原 n 的奇数位)，相或，就达到了原 n 的奇数位和偶数位互换的目的；
        # 第一轮 奇偶位交换
        n = n >> 1 & m1 | n & m1 << 1
        # 第二轮 每两位交换
        n = n >> 2 & m2 | n & m2 << 2
        # 第二轮 每四位交换
        n = n >> 4 & m4 | n & m4 << 4
        # 第三轮 每八位交换
        n = n >> 8 & m8 | n & m8 << 8
        # 最后16位交换
        return n >> 16 | n << 16


a = Solution().reverseBits(43261596)
print(a)



