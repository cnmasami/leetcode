# 颜色分类

# 给定一个包含红色、白色和蓝色、共n 个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
#
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
#
import random
from typing import List


class Solution:
    # 双指针 循环不变量
    # 双指针，一个指针指0，一个指针指2
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # all in [0, zero] = 0
        # all in (zero, i) = 1
        # all in (two, len - 1] = 2
        def swap_pos(left, right):
            nums[left], nums[right] = nums[right], nums[left]

        i = 0
        zero = 0
        two = len(nums) - 1
        # 由于第 2 个区间 (zero, i) 是右边开区间，
        # 第 3 个区间 (two, len - 1] 左边也是开区间，
        # 所以 i 这个位置两个区间都没有包含到，因此，在 while 里面需要写成 i <= two
        while i <= two:
            if nums[i] == 0:
                swap_pos(zero, i)
                i += 1
                zero += 1
            elif nums[i] == 2:
                swap_pos(i, two)
                two -= 1
            else:
                i += 1

    # 单指针，二次遍历
    # 第一次遍历的时候，将数组中所有的0交换到数组头部
    # 二次遍历的时候，将数组中的1交换到头部0之后
    # 此时所有的2都出现在数组尾部，完成排序
    # 使用一个指针ptr表示[头部]的范围，ptr中存储一个整数
    # 表示数组nums从位置0到位置ptr-1都属于头部
    # ptr的初始值为0，表示还没有数处于头部
    def sortColors2(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

    # 所有数都≤2，那么索性把所有数组置为2，
    # 然后遇到所有≤1的，就再全部置为1，，覆盖了错误的2，
    # 这时候所有2的位置已经正确，最后所有≤0的全部置为0，也就覆盖了一些错误的1，
    # 这时候，0和1的位置都正确。最重要的就是需要两个指针指向下一个1或0的位置
    def sortColors3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0  # 分别统计0，0+1的出现数量
        for i in range(len(nums)):
            # 先都设定成2
            buf, nums[i] = nums[i], 2
            if buf == 1 or buf == 0:
                # 设1，统计0或1是因为优先放0,0放完才放1
                nums[p1] = 1
                p1 += 1
            if buf == 0:
                # 置0在置1之后，这是因为优先放0，会有错误的1被0替换掉
                # 没被替换的就是正确的1
                nums[p0] = 0
                p0 += 1

    # 双指针，p0来交换0，p1来交换1. 指针初始值都为0
    # 如果找到了1，将其与nums[p1]交换，并将p1向后移动一个位置
    # 找到了0，因为连续的0之后是连续的1，
    # 因此如果我们将0与nums[p0]交换，那么我们可能也会把1交换出去。
    # 当p0<p1时，我们已经将一些1连续地放在头部，此时一定会把一个1交换出去，导致答案错误
    # 因此，如果 p0<p1，那么我们需要再将 nums[i] 与 nums[p1] 进行交换，
    # 其中 i 是当前遍历到的位置，在进行了第一次交换后，
    # nums[i] 的值为 1，我们需要将这个 1 放到「头部」的末端。
    # 在最后，无论是否有p0<p1，我们需要将p0和p1均向后移动一个位置，
    # 而不是仅将p0 向后移动一个位置。
    def sortColors4(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1




nums = [1,2,0,2,1,0]
Solution().sortColors(nums)
print(nums)


