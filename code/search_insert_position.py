# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引，
# 如果目标值不存在于数组，返回它将会被按顺序插入的位置
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if middle == left:
                return middle + 1
            elif middle == right:
                return middle

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle


    # 二分查找，官方题解，确实官方的这个更明了一些，因为已经比较过target和middle的值，所以可以直接让左右指针跳过middle这个索引
    def offical(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return left



a = Solution().offical(nums = [1,3,5,6], target = 6)
print(a)