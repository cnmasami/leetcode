# 最长连续递增序列
# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
#
# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，
# 都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
#
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_count = count = 1
        prev = nums[0]

        for num in nums[1:]:
            if num > prev:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 1
            prev = num

        return max_count


a = Solution().findLengthOfLCIS([2,2,2,2,2])
print(a)

