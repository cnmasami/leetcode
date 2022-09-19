# 给一个整数columnNumber，返回它在excel表中相对应的列名称
#

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber, mod = divmod(columnNumber, 26)
            if mod != 0:
                ans = chr(mod + 64) + ans
            else:
                # 如果余数是0，就像上一位借个1（26）出来，让余数强行等于26
                ans = chr(26 + 64) + ans
                columnNumber -= 1

        return ans

    # 这题本质上是进制转换题
    # 但是其他的进制转换的数值取值范围在[0, x)的前提下逢x进一
    # 但是本题是从1开始，所以，在进制转换之前，我们先要对columnNumber执行减一操作
    # 实现整体偏移
    def offical(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, mod = divmod(columnNumber, 26)
            ans = chr(mod + ord('A')) + ans

        return ans

    def dfs(self, columnNumber: int) -> str:
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if columnNumber <= 26: return letter[columnNumber -1]
        a, b = divmod(columnNumber -1, 26)
        return self.dfs(a) + letter[b]


a = Solution().convertToTitle(130)
print(a)