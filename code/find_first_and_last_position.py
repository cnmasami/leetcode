# 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回[-1, -1]。
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        if target < nums[0]:
            return [-1, -1]

        if target > nums[-1]:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        # change = False
        res = []

        while left < right:
            # 除法向下取整
            mid = (left + right) // 2

            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        if nums[left] == target:
            res.append(left)

            right = len(nums) -1

            while left < right:
                # 除法向上取整
                mid = (left + 1 + right) // 2

                if nums[mid] == target:
                    left = mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1

            res.append(right)

            return res
        else:
            return [-1, -1]


a = Solution().searchRange(nums = [4, 5, 6, 6, 6, 6, 6, 6, 8], target = 5)
print(a)
