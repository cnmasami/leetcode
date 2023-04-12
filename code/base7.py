# 七进制数
# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        neg = '-' if num < 0 else ''
        ans = ''

        num = abs(num)

        while num:
            num, mod = divmod(num, 7)
            ans = str(mod) + ans

        return neg + ans


a = Solution().convertToBase7(100)
print(a)