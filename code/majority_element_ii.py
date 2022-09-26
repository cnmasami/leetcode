# 多数元素2
# 给定一个大小为n的整数数组，找出其中所有超过[n/3]次的元素
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj = []
        def helper(lo, hi):
            res = []
            if lo == hi:
                return [nums[lo]]

            mid = lo + (hi - lo) // 2
            left = helper(lo, mid)
            right = helper(mid + 1, hi)

            if left == right:
                return left

            for l in left:
                left_counter = sum(1 for num in nums[lo: hi + 1] if num == l)
                if left_counter > (hi - lo + 1) // 3 and l not in res:
                    res.append(l)

            for r in right:
                right_counter = sum(1 for num in nums[lo: hi + 1] if num == r)
                if right_counter > (hi - lo + 1) // 3 and r not in res:
                    res.append(r)

            return res

        re = helper(0, len(nums)-1)
        maj.extend(re)
        return maj

    def hash_majority_element(self, nums: List[int]) -> List[int]:
        ans = []

        counter = collections.Counter(nums)

        for k, v in counter.items():
            if v > len(nums) // 3:
                ans.append(k)

        return ans

    # 这个投票算法，依旧，如果存在n个数的个数大于三分之数组的长度
    # 那么这个n最多有两个
    # 所以，我们一开始就假设存在两个这样的数字
    # 然后用投票算法计算就可以了
    def vote_majority_element(self, nums: List[int]) -> List[int]:
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            if vote1 > 0 and num == element1:
                vote1 += 1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            else:
                # 如果三个元素都不相同，互相抵消1次
                vote1 -= 1
                vote2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 >0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1

        if vote1 > 0 and cnt1 > len(nums) // 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) // 3:
            ans.append(element2)

        return ans


a = Solution().vote_majority_element([3,2,3,4,3,5,4,4,3])
print(a)

