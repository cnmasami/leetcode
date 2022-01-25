# 给你两个按 非递减顺序 排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
from typing import List


class Solution:
    # 这个解法是错误的
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1

        # num1此时的元素个数已经改变了
        # 但是这种是不行的，如果num2全部比num1小，就会多出来额外的num1原来后面的0
        if j < n:
            nums1[m+n-1-j:] = nums2[j:]

        print(nums1)


    # 官方居然直接用了排序
    def offical_sort(self, num1, m, num2, n):
        num1[:] = num2
        num1.sort()


    # 官方居然用了另一个数组来存，但是这样还能算是nums1 in place吗
    def double_pointer(self, num1, m, num2, n):
        sorted = []
        p1 = p2 = 0

        while p1 < m or p2 <n:
            if p1 == m:
                sorted.append(num2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(num1[p1])
                p1 += 1
            elif num1[p1] < num2[p2]:
                sorted.append(num1[p1])
                p1 += 1
            else:
                sorted.append(num2[p2])
                p2 += 1

        num1[:] = sorted

    # 和上面双指针一样的思路，这次确实是nums1 in place
    # 因为nums1后面的都是0，使用双指针比较最大的放进来覆盖原来是0的元素
    # 在遍历的过程中，任意一个时刻，nums1数组中有m-p1-1个元素被放进nums1的后半部分，
    # nums2数组中有n - p2-1个元素被放入nums1的后半部分，而在指针p1的后面，nums1数组有m+n-p1-1个位置
    # 由于 m+n -p1 -1 >= m -p1 - 1 + n - p2 -1 等价于p2 >= -1永远成立，所以p1后面的位置永远足够容纳被插入的元素
    # 不会产生p1的元素被覆盖的情况
    def reverse_double_pointer(self, nums1, m, num2, n):
        p1, p2 = m-1, n -1
        tail = m + n -1

        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = num2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > num2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = num2[p2]
                p2 -= 1

            tail -= 1



a = Solution().merge([2,0],1,[1], 1 )
# print(a)
