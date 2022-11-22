# 区域和检索
# 给定一个整数数组  nums，处理以下类型的多个查询:
#
# 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，
# 包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# 前缀和，列表中下标为i的元素为nums中下标为i的元素 之前的元素和
class prefix_sum_NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [0]

        for num in nums:
            self.nums.append(self.nums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


p = prefix_sum_NumArray([-2, 0, 3, -5, 2, -1])
print(p.sumRange(0,5))
