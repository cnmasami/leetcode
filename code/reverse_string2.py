# 反转字符串2
# 给定一个字符串s和一个整数k，从字符串开头算起，每计数至2k个字符，就反转这2k字符中的前K个字符
# 如果剩余字符少于K个，则将剩余字符全部反转
# 如果剩余字符小于2K但大于或等于K个，则反转前K个字符，其余字符保持原样

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        for i in range(0, len(s), k * 2):
            # if len(s[i: i + 2*k]) >= k:
            #     ans += ''.join(reversed(s[i:i+k]))
            #     ans += s[i+k: i +2*k]
            # else:
            #     ans += ''.join(reversed(s[i:i+2*k]))
            # 不用判断也可以，如果不足，后面是取不到的
            # 但是提交的时候反而每次有if判断的时候耗时更短
            ans += ''.join(reversed(s[i:i + k]))
            ans += s[i + k: i + 2 * k]

        return ans

    def simple(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i+k] = reversed(t[i: i+k])

        return ''.join(t)


a = Solution().reverseStr(s = "abcdefg", k = 8)
print(a)