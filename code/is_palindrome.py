# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

# 使用双边指针

# 将整个数字反转，和原始数字做比较
class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        ans = 0

        iter_x = x

        while iter_x > 0:
            iter_x, mod = divmod(iter_x, 10)
            ans = ans*10 + mod

        if ans == x:
            return True
        else:
            return False


# 官方题解，将数字反转一半
class Solution2():
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNum = 0

        while x > revertedNum:
            revertedNum = revertedNum * 10 + x % 10

            x //= 10

        return x == revertedNum or x == revertedNum // 10

a = Solution().isPalindrome(10)
print(a)