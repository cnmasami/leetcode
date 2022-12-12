# 反转字符串
# 编写一个函数，其作用是将输入的字符串反转过来。
# 输入字符串以字符数组s的形式给出
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组
# 使用O(1)的额外空间解决这一问题
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
