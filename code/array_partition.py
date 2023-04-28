# 数组拆分

# 给定长度为2n的整数数组 nums ，你的任务是将这些数分成n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，
# 使得从 1 到n 的 min(ai, bi) 总和最大。
#
# 返回该 最大总和 。
#
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # ans = 0
        #
        # for i in range(0, len(nums), 2):
        #     ans += nums[i]
        #
        # return ans
        return sum(nums[::2])


a =Solution().arrayPairSum([6,2,6,5,1,2])
print(a)