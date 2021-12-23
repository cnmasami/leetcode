# 给你一个字符串s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

# 请你返回字符串的能量。


class Solution:
    def maxPower(self, s: str) -> int:
        temp = ''
        max_num =  0
        longest = 1
        for sub_s in s:
            if temp == sub_s:
                longest += 1
            else:
                temp = sub_s
                max_num = max(max_num, longest)
                longest = 1

        return max(max_num, longest)

a = Solution().maxPower('tt')
print(a)