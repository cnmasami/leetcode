# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

        # if x == 0:
        #             return 0
        #
        #         left = 1
        #         right = x
        #
        #         while left < right:
        #             middle = left + (right - left) // 2
        #
        #             if middle == left:
        #                 break
        #
        #             if middle * middle < x:
        #                 left = middle
        #             elif middle * middle > x:
        #                 right = middle
        #             else:
        #                 return middle
        #
        #         return left

    # 官方二分
    def offical_binary(self, x: int) -> int:
        l, r, ans = 0, x, -1

        while l <= r:
            mid = (l + r) // 2

            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid -1

        return ans

    # 牛顿迭代
    def newton(self, x: int) -> int:
        if x == 0:
            return 0

        c, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + c/x0)

            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)

a = Solution().offical_binary(0)
print(a)

