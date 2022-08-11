# 集合 s 包含从 1 到n的整数。不幸的是，因为数据错误，
# 导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
# 导致集合 丢失了一个数字 并且 有一个数字重复 。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
#
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
import collections
from typing import List


class Solution:
    # 还是利用等差数列公式
    def findErrorNums(self, nums: List[int]) -> List[int]:
        real_nums = set(nums)

        dup_num = sum(nums) - sum(real_nums)

        total_num = len(nums)

        mis_num = (1 + total_num) * total_num // 2 - sum(nums) + dup_num

        return [dup_num, mis_num]

    # 排序判断相邻元素，相等就是重复数字，相差为2，两个元素中间的值就是丢失的数字
    # 边界数字要特殊判断
    def sort_findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()

        rept = miss = -1

        if nums[0] != 1:
            miss = 1
        elif nums[-1] != len(nums):
            miss = len(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                rept = nums[i]
            elif nums[i] - nums[i-1] == 2:
                miss = nums[i] -1

        return [rept, miss]


    def hash_findErrorNums(self, nums: List[int]) -> List[int]:
        count_dict = collections.Counter(nums)
        dup = mis = -1

        for i in range(1, len(nums) +1):
            tmp = count_dict.get(i, 0)
            if tmp == 0:
                mis = i
            elif tmp == 2:
                dup = i

        return [dup, mis]








