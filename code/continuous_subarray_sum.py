# 连续的子数组和

# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
#
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 如果存在，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # pre_sum_map = {nums[0] % k: 0}
        #
        # pre_sum = nums[0]
        #
        # for idx, num in enumerate(nums[1:], 1):
        #     pre_sum += num
        #     mod = pre_sum % k
        #
        #     if mod in pre_sum_map:
        #         if idx - pre_sum_map[mod] >= 2:
        #             return True
        #         continue
        #     else:
        #         pre_sum_map[mod] = idx
        #
        # return False
        prefix_sum = {0: -1}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            remainder = curr_sum % k

            if remainder in prefix_sum and i - prefix_sum[remainder] >= 2:
                return True

            if remainder not in prefix_sum:
                prefix_sum[remainder] = i

        return False



a = Solution().checkSubarraySum([23,2,4,6,6], 7)
print(a)

