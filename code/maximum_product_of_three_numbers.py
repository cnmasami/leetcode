# 三个数的最大乘积
# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


a = Solution().maximumProduct([-100,-98,-1,2,3,4])
print(a)