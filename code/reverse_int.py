# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，就返回 0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。

# 输入：x = 123
# 输出：321


class Solution:
    def reverse(self, x: int) -> int:
        # res_list = []
        res_num = 0

        # abs_x = x
        abs_x = abs(x)

        while abs_x:
            abs_x, res = divmod(abs_x, 10)
            # res_list.append(res)
            res_num = res_num * 10 + res

        real_res_num = res_num if x > 0 else res_num * -1

        if real_res_num < pow(-2, 31) or real_res_num > (pow(2, 31) -1):
            return 0
        else:
            return real_res_num

a = Solution().reverse(-123)
print(a)
