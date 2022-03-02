# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, 1

        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
                continue

            right += 1
            left += 1

        return nums

    # 官方，仅判断右指针的值
    def offical(self, nums: List[int]):
        n = len(nums)
        left = right = 0

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1


    # 题解里看到的对官方解法的优化
    def better_offical(self, nums: List[int]):
        n = len(nums)
        left = right = 0

        while right < n:
            if nums[right] != 0:
                if right > left:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1

        return nums


a = Solution().better_offical([1, 0, 0, 3, 12])
print(a)
