# 至少是其他数字两倍的最大数

# 给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。
#
# 请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。
# 如果是，则返回 最大元素的下标 ，否则返回 -1 。
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1 = m2 = -1
        index_num = -1

        for idx, num in enumerate(nums):
            if num > m1:
                m1, m2, index_num = num, m1, idx
            elif num > m2:
                m2 = num

        return index_num if m1 >= m2 * 2 else -1


a = Solution().dominantIndex([0,2,3,0])
print(a)