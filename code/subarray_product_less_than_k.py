# 乘积小于 K 的子数组

# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
from bisect import bisect_right
from math import log
from typing import List


class Solution:
    # 在计算连续子数组的乘积的时候，会出现整型溢出的情况
    # 为了避免整型溢出，我们将不等式两边取对数 连乘取对数 = 乘数本身对数累加和 < log k
    # 因此，子数组的元素乘积小于k 等价于 子数组的元素对数和小于 log k
    # 预处理出数组的元素对数前缀和logPrefix, 即logPrefix[i+1] = 从0到i的元素对数累加和
    # 因为nums是正整数，所以logPrefix是非递减的
    # 枚举子数组的右端点j，在logPrefix的区间0到j内二分查找满足logprefix[j+1] - logPrefix[l] < log k
    # 的最小下标l，那么以j为右端点 且 元素乘积小于k 的子数组数目为 j + 1 - l
    # 返回所有数目之和
    # double类型只能保证15位有效数字是精确的，为了避免计算带来的误差，我们将不等式logPrefix[l] > logPrefix[j+1]- log k
    # 的右边加上10的-10次方，从而防止不等式两边数值相等却被判为大于的情况
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        ans, n = 0, len(nums)
        logPrefix = [0] * (n+1)

        for i, num in enumerate(nums):
            logPrefix[i + 1] = logPrefix[i] + log(num)

        logk = log(k)

        for j in range(1, n+1):
            l = bisect_right(logPrefix, logPrefix[j] - logk + 1e-10, 0, j)
            ans += j - l

        return ans

    # 滑动窗口
    # 固定子数组[i, j]的右端点j的时候，显然左端点i越大，子数组元素乘积越小
    # 对于子数组[i, j], 当左端点i >= l1时，所有子数组的元素乘积都小于k
    # 当左端点i < l1时，所有子数组的元素乘积都大于等于k。
    # 那么对于右端点为j+1的所有子数组，它的左端点i就不需要从0开始枚举
    # 因为对于所有i <l1的子数组，它们的元素乘积都大于等于k，我们只需要从l1处开始枚举
    # 直到子数组i=l2时，子数组[l2, j+1]的元素乘积小于k，那么左端点i >= l2 所有子数组的元素乘积都小于k
    # 根据上面，枚举子数组的右端点j，并且从左端点从i=0开始，用prod记录子数组[i, j]的元素乘积
    # 每枚举一个右端点j，如果当前子数组元素乘积prod大于等于k，那么右移左端点i直到满足当前子数组元素乘积小于k
    # 或者i>j，那么元素乘积小于k的子数组数目为j-i+1,返回所有数目之和
    # prod的值始终不超过k x maxl{nums[l]}，因此无需担心整型溢出的问题
    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0

        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1

            ans += j - i + 1

        return ans



