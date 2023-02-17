# 数字转换为十六进制数

# 给定一个整数，编写一个算法将这个数转换为十六进制数。
# 对于负整数，我们通常使用补码运算方法

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        if num < 0:
            num += 2 ** 32

        ans = ''

        while num:
            num, mode = divmod(num, 16)
            if mode < 10:
                ans = str(mode) + ans
            else:
                ans = chr(ord('a') + mode - 10) + ans

        return ans

    # 位运算，32位整数转十六进制。一位十六进制数对应四位二进制数
    # 将num二进制数按照四位一组分成8组，依次将每一位转换为对应的十六进制数
    # 假设二进制数的 8 组从低位到高位依次是第 0 组到第  7 组，
    # 则对于第  i 组，可以通过
    # (nums>>(4×i))&0xf得到该组的值
    def toHex2(self, num: int) -> str:
        if num == 0:
            return '0'
        ret = []
        template = '0123456789abcdef'
        result = []
        num = num & 0xFFFFFFFF

        while num:
            result.append(template[num & 0XF])
            num = num >> 4

        return ''.join(result[::-1])


a = Solution().toHex(285)
print(a)