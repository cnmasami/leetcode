# 二分查找

# 给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，
# 写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。
#
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

a = Solution().search(nums = [-1,0,3,5,9,12], target = 2)
print(a)