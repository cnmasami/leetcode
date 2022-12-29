# 两个数组的交集 II
# 给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。
# 返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
#
import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        len1 = len(nums1)
        len2 = len(nums2)
        index1 = index2 = 0
        intersection = []

        while index1 < len1 and index2 < len2:
            num1 = nums1[index1]
            num2 = nums2[index2]

            if num1 == num2:
                intersection.append(num1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1

        return intersection

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)

        num = num1 & num2
        return list(num.elements())

    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect3(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            count = m.get(num, 0)
            if count > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection


a = Solution().intersect2([1, 2, 3,2,4], [2, 5, 2])
print(a)