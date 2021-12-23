# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。

# 暴力枚举
from typing import List


def towSum(nums: List[int], target: int) -> List[int]:

    index_list = []

    for index, val in enumerate(nums):
        other_val = target - val
        if other_val in nums[index:]:
            return [index, nums.index(other_val, index + 1)]

    return index_list


# 哈希表
def HashTwoSum(nums: List[int], target: int):
    hashtable = dict()

    for index, val in enumerate(nums):
        if target - val in hashtable:
            return [hashtable[target - val], index]
        hashtable[val] = index

    return []


# a = ['a', 'b', 'c', 'd', 'e']
#
# print(a.index('d', 2))
