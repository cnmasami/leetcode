# 第三大的数

# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)
        else:
            return sorted(nums)[-3]

    # 若 num>a，我们将 c 替换为 b，b 替换为 a，a 替换为num，这模拟了将num 插入有序集合，并删除有序集合中的最小值的过程；
    # 若 a>num>b，类似地，我们将 c替换为b，b替换为num，a保持不变；
    # 若 b>num>c，类似地，我们将 c替换为num，a和 b保持不变；
    # 其余情况不做处理。
    def thirdMax2(self, nums: List[int]) -> int:
        a, b, c = None, None, None
        for num in nums:
            if a is None or num > a:
                a, b, c = num, a, b
            elif a > num and (b is None or num > b):
                b, c = num, b
            elif b is not None and b > num and (c is None or c < num):
                c = num

        return a if c is None else c


a = Solution().thirdMax([2, 2, 3, 1])
print(a)