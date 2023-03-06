# 最大连续1的个数
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0

        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0

        return max_len
    

a = Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])
print(a)

        