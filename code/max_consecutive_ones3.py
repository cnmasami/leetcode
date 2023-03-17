# 最大连续1的个数
# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

 
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        left = 0
        right = 0
        z_count = 0

        while right < len(nums):
            if nums[right] == 0:
                z_count += 1
                
            while z_count > k:
                if nums[left] == 0:
                    z_count -= 1
                left += 1
                
            max_count = max(max_count, (right - left + 1))
            right += 1

        return max_count


    

a = Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
print(a)
