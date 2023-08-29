# 寻找数组的中心下标

# 给你一个整数数组 nums ，请计算数组的 中心下标 。
#
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
#
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
#
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
from typing import List


class Solution:
    # 前缀和
    # 记数组的全部元素之和为total，当遍历到第i个元素的时候，
    # 设其左侧元素之和为sum，则其右侧元素之和为total - sum - si
    # 然后判断两侧是否相等
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        sum_left = 0
        for i in range(len(nums)):
            if 2 * sum_left == total_sum - nums[i]:
                return i
            sum_left += nums[i]

        return -1


a = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
print(a)

