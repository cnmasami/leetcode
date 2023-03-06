# 数字的补数

# 对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。
#
# 例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
# 给你一个整数 num ，输出它的补数。
#

class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        reverse = False
        for i in range(31, -1, -1):
            n = num >> i
            if not reverse and n == 1:
                cur_bit = (n & 1) ^ 1
                reverse = True
                ans += pow(2, i) * cur_bit
            elif reverse:
                cur_bit = (n & 1) ^ 1

                ans += pow(2, i) * cur_bit

        return ans

a = Solution().findComplement(1)
print(a)