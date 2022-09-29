# 存在重复元素2
# 给你一个整数数组nums 和一个整数k ，
# 判断数组中是否存在两个 不同的索引i和j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
# 如果存在，返回 true ；否则，返回 false 。
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited_dict = {}

        for idx, num in enumerate(nums):
            # if num not in visited_dict:
            #     visited_dict[num] = idx
            # else:
            #     if abs(idx - visited_dict[num]) <= k:
            #         return True
            #     else:
            #         visited_dict[num] = idx
            if num in visited_dict and idx - visited_dict[num] <= k:
                return True
            visited_dict[num] = idx

        return False

    # 滑动窗口
    # 假设有一个k+1长度的滑动窗口在数组中，则这个滑动窗口内的任意两个下标差的绝对值不超过k
    # 如果存在一个滑动窗口，其中有重复元素，则存在两个不同的下标i和j满足nums[i] = nums[j]，且i-j的绝对值小于k
    # 如果所有滑动窗口中都没有重复元素，则不存在符合要求的下标。
    # 因此，只要遍历每个滑动窗口，判断滑动窗口是否有重复元素即可
    def slid_window(self, nums: List[int], k: int) -> bool:
        s = set()

        for idx, num in enumerate(nums):
            if idx > k:
                s.remove(nums[idx - k - 1])

            if num in s:
                return True
            s.add(num)

        return False