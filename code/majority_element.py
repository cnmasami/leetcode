# 给定一个大小为n的数组nums，返回其中的多数元素，
# 多数元素是指在数组中出现次数大于[n/2]的元素
# 可以假设数组非空，并且给定的数组总是存在多数元素
import collections
import random
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        return max(counter, key=counter.get)

    # 因为多数元素是出现次数大于n/2的元素
    # 所以在n/2处取值取到的一定是这个元素
    def sort_majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) // 2]

    # 理论上最坏情况下的时间复杂度是正无穷
    def random_majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candiate = random.choice(nums)
            if sum(1 for elem in nums if elem == candiate) > majority_count:
                return candiate

    # 如果数a是数组nums的众数，那么如果将nums分成两部分，那么a必定是至少一部分的众数
    # 可以使用反证法来证明这个结论，假设a既不是左半部分的众数，也不是右半部分的众数
    # 那么a出现的次数少于l/2 + r/2次，其中l和r分别是左半部分和右半部分的长度
    # 由于l/2 + r/ 2 <= (l+r) / 2 说明a也不是数组nums的众数，因此出现了矛盾，所以这个结论是正确的
    # 这样以来，我们可以用分治法解决这个问题，将数组分成左右两部分，分别求出左半部分的众数a1
    # 以及右半部分的众数a2，随后在a1和a2中选出正确的众数
    # 使用分治算法递归求解，直到所有的子问题都是长度为1的数组，
    # 长度为1的子数组中唯一的数显然是众数，直接返回即可
    # 如果回溯后某区间的长度大于1，我们必须将左右子区间的值合并。
    # 如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
    # 否则需要比较两个众数在整个区间内出现的次数来决定该区间的众数
    def divide_majorityElement(self, nums: List[int]) -> int:

        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) -1)

    # 如果把众数记为1，其他数记为-1，那么全部加起来和一定大于0
    # 这个算法的本质和分治十分类似
    # 维护一个候选众数candidate和它出现的次数count，初始时candidate可以为任意值，count为0
    # 我们遍历数组nums中的所有元素，对于每个元素x，在判断x之前，如果count的值为0
    # 我们先将x的值赋予candiate，随后我们判断x
    # 如果x与candidate相等，那么计数器count的值增加1
    # 如果x与candidate不相等，那么计数器count的值减少1
    # 遍历完成后，candidate即为整个数组的众数
    # 由于多数超过50 %, 比如100个数，那么多数至少51个，剩下少数是49个。
    #
    # 第一个到来的士兵，直接插上自己阵营的旗帜占领这块高地，此时领主winner
    # 就是这个阵营的人，现存兵力count = 1。
    #
    # 如果新来的士兵和前一个士兵是同一阵营，则集合起来占领高地，领主不变，winner
    # 依然是当前这个士兵所属阵营，现存兵力count + +；
    #
    # 如果新来到的士兵不是同一阵营，则前方阵营派一个士兵和它同归于尽。 此时前方阵营兵力count - -。（即使双方都死光，这块高地的旗帜
    # winner依然不变，因为已经没有活着的士兵可以去换上自己的新旗帜）
    #
    # 当下一个士兵到来，发现前方阵营已经没有兵力，新士兵就成了领主，winner
    # 变成这个士兵所属阵营的旗帜，现存兵力count + +。
    #
    # 就这样各路军阀一直以这种以一敌一同归于尽的方式厮杀下去，直到少数阵营都死光，那么最后剩下的几个必然属于多数阵营，winner
    # 就是多数阵营。（多数阵营51个，少数阵营只有49个，死剩下的2个就是多数阵营的人）
    def boyer_moore_vote(self, nums: List[int]):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate




a = Solution().majorityElement([3, 2, 3])
print(a)

