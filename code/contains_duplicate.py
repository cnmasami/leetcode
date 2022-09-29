# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；
# 如果数组中每个元素互不相同，返回 false 。
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)

        return False


    def containsDuplicate_bylens(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))