# 数组的度
# 给定一个非空且只包含非负数的整数数组nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。

# 你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。
import collections
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree_dict = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            degree_dict[num].append(idx)

        degree_num = 0
        min_lenth = len(nums)

        for num in degree_dict:
            if len(degree_dict[num]) > degree_num:
                degree_num = len(degree_dict[num])
                min_lenth = degree_dict[num][-1] - degree_dict[num][0] + 1
            elif len(degree_dict[num]) == degree_num:
                min_lenth = min(degree_dict[num][-1] - degree_dict[num][0] + 1, min_lenth)

        return min_lenth



a = Solution().findShortestSubArray([1,2,2,3,1])
print(a)