# 1 比特与 2 比特字符

#有两种特殊字符：
# 第一种字符可以用一比特0 表示
# 第二种字符可以用两比特（10或11）表示
# 给你一个以 0 结尾的二进制数组bits，如果最后一个字符必须是一个一比特字符，则返回 true 。
import collections


class Solution:
    # 因为1肯定是连着下一个，所以遇见1，走两步，遇见0，走一步
    # 判断能不能走到最后一位
    def oneBitAnd2bitCharacters(self, bits):
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return False


a = Solution().oneBitAnd2bitCharacters([1, 0, 0])
print(a)