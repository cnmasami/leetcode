# 子数组最大平均数 I

# 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
#
# 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
#
# 任何误差小于 10-5 的答案都将被视为正确答案。
#
from typing import List


class Solution:
    # 会超时
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = float('-inf')
        i = 0

        while i + k <= len(nums):
            this_avg = sum(nums[i:i+k]) / k
            avg = max(avg, this_avg)
            i += 1

        return avg

    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        max_total = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total + nums[i] - nums[i-k]
            max_total = max(total, max_total)

        return max_total / k


a = Solution().findMaxAverage(nums = [1,12,-5,-6,50,300], k = 4)
print(a)