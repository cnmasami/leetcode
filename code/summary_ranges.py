# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        range_start = nums[0]

        for idx, num in enumerate(nums):
            if (num - nums[idx -1]) > 1:
                if nums[idx-1] == range_start:
                    ans.append(str(range_start))
                else:
                    ans.append('{}->{}'.format(range_start, nums[idx-1]))

                range_start = num

        if nums[-1] == range_start:
            ans.append(str(range_start))
        else:
            ans.append('{}->{}'.format(range_start, nums[-1]))

        return ans

    # 一样的思路，另一种写法
    def summaryRangesii(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []

        a, b = 0, 0
        while b < n:
            if b < n - 1 and nums[b + 1] == nums[b] + 1:
                b += 1
            else:
                res.append((nums[a], nums[b]))
                a = b + 1
                b = b + 1

        def p(x):
            a, b = x
            if a == b:
                return str(a)
            else:
                return str(a) + '->' + str(b)

        return list(map(p, res))




a = Solution().summaryRanges([0,1,2,4,5,7])
print(a)