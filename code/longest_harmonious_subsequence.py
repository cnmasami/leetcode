# 最长和谐子序列

# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
#
# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
#
# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
#
import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        max_len = 0

        left = right = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            elif nums[right] - nums[left] == 1:
                max_len = max(max_len, right - left + 1)
                right += 1
            elif nums[right] - nums[left] > 1:
                left += 1
                while nums[left] == nums[left - 1]:
                    left += 1

        return max_len

    # 哈希
    def hash_findLHS(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)

        return max((val + cnt[key + 1] for key, val in cnt.items() if key + 1 in cnt), default=0)


a = Solution().findLHS([1,1,1,1])
print(a)

