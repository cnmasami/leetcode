# 数据流中的第 K 大元素
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
#
# 请实现 KthLargest类：
#
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
#
import heapq
import random
from typing import List


class KthLargest:
    # 使用大小为K的小根堆，在初始化的时候，保证堆中的元素个数不超过K
    # 在每次add的时候，将新元素push到堆中，如果此时堆中的元素超过了K
    # 那么需要把队中的最小元素既堆顶pop出来
    # 此时堆中的最小元素既堆顶就是整个数据流中的第K大元素
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


kth_Largest = KthLargest(1, [])

a = kth_Largest.add(-3)
a = kth_Largest.add(5)
a = kth_Largest.add(10)
a = kth_Largest.add(9)
a = kth_Largest.add(4)

print(a)
