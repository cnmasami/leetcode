# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max = len(nums)

        real_sum = sum(nums)
        # 等差数列，首项加尾项乘以项数除以2，因为0值不在和里面，不算作首项
        theory_sum = (1 + max) * max // 2

        return theory_sum - real_sum

    # 对数组排序，判断每个下标的元素是否和下表相等，得到丢失数字
    def sort_missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num != i:
                return i

        return len(nums)

    # 哈希集合
    def missingNumber3(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i




a = Solution().missingNumber([9,6,4,2,3,5,7,0,1])
print(a)