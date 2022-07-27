# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

    # 位运算
    # 因为题目里说除了这个单个元素外每个元素出现两次
    # 使用异或的特性
    # 任何元素和它本身异或结果是0
    # 任何元素和0异或结果是它本身
    # 异或满足交换律和结合律，
    # 所以这道题的解法就是对所有元素进行异或操作
    # 最终得到的结果就是那个只出现一次的元素
    def offical(self, nums: List[int]) -> int:
        # reduce(fun,seq) function is used to apply a particular
        # function passed in its argument to all of the list elements
        return reduce(lambda x, y: x^y, nums)


a = Solution().singleNumber([4,1,2,1,2, 5,5])
print(a)


