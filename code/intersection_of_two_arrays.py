# 两个数组的交集
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。
# 输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
#
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1).intersection(set(nums2)))
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [num for num in nums1 if num in nums2]


    def sort_double_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        len1, len2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0

        while index1 < len1 and index2 < len2:
            num1 = nums1[index1]
            num2 = nums2[index2]

            if num1 == num2:
                if not intersection or num1 != intersection[-1]:
                    intersection.append(nums1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1

        return intersection