# 最长递增子序列的个数
# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
#
# 注意 这个数列必须是 严格 递增的。
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        max_len = 0
        ans = 0

        for i in range(n):
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    cur_dp = dp[j] + 1

                    if cur_dp > dp[i]:
                        dp[i] = cur_dp
                        count[i] = count[j]
                    elif cur_dp == dp[i]:
                        count[i] += count[j]

                j += 1

            if dp[i] > max_len:
                max_len = dp[i]
                ans = count[i]
            elif dp[i] == max_len:
                ans += count[i]

        return ans

a = Solution().findNumberOfLIS([3,1,3,5,4,7])
print(a)







