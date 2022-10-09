# 存在重复元素III
# 给你一个整数数组 nums 和两个整数k 和 t 。
# 请你判断是否存在 两个不同下标 i 和 j，使得abs(nums[i] - nums[j]) <= t ，
# 同时又满足 abs(i - j) <= k 。
#
# 如果存在则返回 true，不存在返回 false。
import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    # 滑动窗口 有序数组 二分
    # 根据题意，对于【任意】一个位置i，假设其值为u，
    # 希望在下标范围为[max(0, i-k),i]内找到值范围在[u-t, u+t]的数
    # 不能每个遍历，然后往后检查k个元素，这样复杂度是O(nk)会超时
    # 需要优化  检查后面K个元素 这一过程
    # 希望使用一个 有序集合 去维护长度为K的滑动窗口内的数，该数据结构最好支持高效 查询 与 插入/删除操作
    # 查询：能够在 有序集合 中应用 二分查找，快速找到 小于等于u的最大值 和 大于等于u的最小值 即 有序集合中最接近u的数
    # 插入/删除： 在往 有序集合 添加或删除元素时，能够在低于线性的复杂度内完成 维持有序特性
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > indexDiff:
                window.remove(nums[i - 1 - indexDiff])
            window.add(nums[i])
            # idx是最接近nums[i]的值的坐标位置
            idx = bisect.bisect_left(window, nums[i])
            # 这是一个有序数组，比较查找到的这个值的左右两边的数据有没有符合要求的数据
            if idx > 0 and abs(window[idx] - window[idx-1]) <= valueDiff:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= valueDiff:
                return True

        return False

    # 上述解法无法做到线性的原因是，我们需要在大小为K的滑动窗口所在的 有序集合 中找到与u接近的数
    # 如果我们能够将k个数字分到k个桶的话，那么我们就能O(1)的复杂度确定是否有[u-t, u+t]的数字
    # 检查目标桶是否有元素
    # 具体做法为：令桶的大小为size=t+1，根据u计算所在桶编号
    # 如果已经存在该桶，说明前面已经有[u-t, u+t]范围的数字，返回true
    # 如果不存在该桶，则检查相邻两个桶的元素是有[u-t, u+t]范围的数字，如有 返回true
    # 建立目标桶，并删除下标范围不在[max(0, i-k), i]内的桶
    def bin_containsNear(self, nums, indexDiff, valueDiff):
        def getIdx(u):
            return ((u+1) // size) - 1 if u < 0 else u // size

        map = {}
        size = valueDiff + 1

        for i , u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在(桶不为空)， 说明前面已有[u-t, u+t]范围的数字
            if idx in map:
                return True

            l, r = idx -1, idx + 1

            if l in map and abs(u - map[1]) <= valueDiff:
                return True
            if r in map and abs(u - map[r]) <= valueDiff:
                return True
            # 建立目标桶
            map[idx] = u
            # 维护个数为K
            if i >= indexDiff:
                map.pop(getIdx(nums[i-indexDiff]))

        return False




a = Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)
print(a)