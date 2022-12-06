# 比特位计数
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，
# 计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
from typing import List


class Solution:
    # 位运算，令n与n-1进行与运算，消除低位1，重复运算直到n为0
    # 运算次数即为1的比特数个数
    def countBits(self, n: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x-1)
                ones += 1

            return ones

        bits = [countOnes(i) for i in range(n + 1)]
        return bits

    # 当计算i的1的比特数时，如果存在0<=j < i, j的1的比特数已知，
    # 而且i和j相比，i的二进制表示只多了一个1，则可以快速得到i的一比特数
    # 令bits[i]表示i的 1的比特数，则bits[i] = bits[j] + 1
    # 对于正整数x，如果可以知道最大的正整数y，使得y<=x且y是2的整数次幂，
    # 则y的二进制表示中只有最高位是1，其余都是0，此时称y为x的最高有效位
    # 令z=x-y，显然对于0 <= z < x,有bits[x] = bits[z] + 1
    # 使用位运算判断一个正整数是不是2的整数次幂
    # 显然，0的 1的比特数 为0，使用highBit表示当前的最高有效位，
    # 遍历从1到n的每个正整数i，
    # 如果i & (i-1)=0, 则令highBit=i，更新当前的最高有效位
    # i比i-hightBit的 1的比特数 多1， 由于是从小到达遍历每个整数，
    # 因此遍历到i时，i-hightBit的1的比特数 已知，
    # 令bits[i] = bits[i - hightBit] + 1
    def dp_highest_countBits(self, n: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, n +1):
            if i & (i -1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)

        return bits

    # 最低有效位
    # 上面这个动态规划需要实时维护最高有效位，换一个思路，使用最低有效位计算一比特数
    # 对于正整数x，将其二进制表示右移一位，等价于将其二进制表示的最低位去掉
    # 得到的数是x//2，如果bits[x//2]的值已知，则可以得到bits[x]的值
    # 如果x是偶数，则bits[x] = bits[x//2]
    # 如果x是奇数，则bits[x] = bits[x//2] + 1
    # 上述两种情况可以合并为：bits[x]的值等于bits[x//2]的值加上x除以2的余数
    # 由于x//2可以通过x>>1得到，x除以2的余数可以通过x&1得到，
    # 因此有bits[x] = bits[x>>1] + (x&1)
    # 遍历从1到n的每个正整数i，计算bits的值，
    # 最终得到的数组bits即为答案
    def dp_lowest_countBits(self, n: int):
        bits = [0]
        for i in range(1, n +1):
            bits.append(bits[i>>1] + (i & 1))

        return bits


    # 最低设置位
    # 定义正整数x的[最低设置位]为x的二进制表示中的最低的1所在位
    # 例如10的二进制表示是1010，则最低设置位为2，对应的二进制表示是10
    # 令y=x&(x-1)，则y为将x的最低设置位从1变成0之后的数，
    # 显然0<=y<x,bits[x] = bits[y] + 1.
    # 因此对于任意正整数x，都有bits[x] = bits[x&(x-1)] + 1
    def dp_low_countBits(self, n: int):
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i & (i -1)] + 1)

        return bits

    # 判断奇偶，偶数则等于其一半的值，即res[2] = res[1] = 1;
    # 奇数则等于其上一个值加一
    # 其实和动态规划最低有效位本质上是一样的
    def count_bits(self, n: int):
        bits = [0] * (n +1)
        for i in range(1, n+1):
            if i % 2 == 0:
                bits[i] = bits[i // 2]
            else:
                bits[i] = bits[i-1] + 1

        return bits





a = Solution().dp_highest_countBits(5)
print(a)
