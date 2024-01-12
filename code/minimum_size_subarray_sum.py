#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其总和大于等于 target 的长度最小的
# 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。
import bisect
from typing import List


class Solution:
    # 滑动窗口双指针
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        left = right = 0
        cur_sum = sum(nums[left:right+1])

        while right < len(nums):
            if cur_sum >= target:
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            elif target > cur_sum:
                right += 1
                if right == len(nums):
                    break
                cur_sum += nums[right]

        return 0 if res == len(nums) + 1 else res

    # 前缀和+二分查找
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        # sums前缀和，nums是一个正数的数组，
        # 所以它的前缀和是递增的
        # 只需要找到sums[j] - sum[i] >= target
        # 那么[j-i]就是满足的连续子数组，也就是sum[j] >= sum[i] + target
        for i in range(1, n+1):
            s = target + sum([i-1])
            bound = bisect.bisect_left(sums, s)
            if bound != len(sums):
                ans = min(ans, bound - (i -1))

        return 0 if ans == n+1 else ans



a = Solution().minSubArrayLen(11, [1,2,3,4,5])
print(a)