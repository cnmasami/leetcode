# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
#

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            middle = (left + right) // 2

            if middle * middle == num:
                return True
            elif middle * middle < num:
                left = middle + 1
            else:
                right = middle - 1

        return False

    # 题解看到的
    # 对于完全平方数而言，可以写成：
    # num=n的平方=1+3+5+...+(2∗n−1)
    # 因此对num进行不断的奇数试减，如果最终能减到0，说明num可以展成上面公式的形式，num为完全平方数
    def useMath(self, num: int) -> bool:
        x = 1

        while num > 0:
            num -= x
            x += 2

        return num == 0

a = Solution().isPerfectSquare(1)
print(a)
