# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。

# 输入: a = "11", b = "1"
# 输出: "100"


# 输入: a = "1010", b = "1011"
# 输出: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        holder = 0
        res = ''

        while la > 0 or lb > 0:
            print(la)
            print(lb)
            num_a = a[la -1] if la > 0 else '0'
            num_b = b[lb -1] if lb > 0 else '0'
            sum_num = int(num_b) + int(num_a) + holder

            holder, sub_res = divmod(sum_num, 2)
            res = str(sub_res) + res

            la -= 1
            lb -= 1

            # if sum_num == 3:
            #     holder = 1
            #     res = '1' + res
            # elif sum_num == 2:
            #     holder = 1
            #     res = '0' + res
            # elif sum_num == 1:
            #     holder = 0
            #     res = '1' + res
            # else:
            #     holder = 0
            #     res = '0' + res

        if holder:
            res = '1' + res

        return res

# 官方题解
# python自带的高精度运算
class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


# 位运算
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry

        return bin(x)[2:]


# a = Solution().addBinary('1010', '1011')
# print(a)


# print('{0:b}'.format(int('1010', 2) + int('1011', 2)))

# print(int('10', 2))
print(bin())