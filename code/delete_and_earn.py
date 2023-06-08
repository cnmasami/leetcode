# 删除并获得点数

# 给你一个整数数组nums，你可以对它进行一些操作。
#
# 每次操作中，选择任意一个nums[i]，删除它并获得nums[i]的点数。之后，你必须删除 所有 等于nums[i] - 1 和 nums[i] + 1 的元素。
#
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
#
from typing import List


class Solution:
    # 选择当前点数，就不能选隔壁的点数，可以转换成打家劫舍，偷了这间房，就不能偷隔壁的钱
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        earn = []
        prev = None

        i = 0
        while i < len(nums):
            this_earn = 0
            j = i
            while j < len(nums):
                if nums[j] == nums[i]:
                    this_earn += nums[i]
                else:
                    break
                j += 1

            if prev and nums[i] - prev == 1:
                if not earn:
                    earn.append(this_earn)
                elif len(earn) == 1:
                    earn.append(max(earn[0], this_earn))
                else:
                    earn.append(max(earn[-1], earn[-2]+ this_earn))
            else:
                if not earn:
                    earn.append(this_earn)
                else:
                    earn.append(earn[-1] + this_earn)

            prev = nums[i]
            i = j

        return earn[-1]

    # 用数组统计每个数对应的和：
    # 2,2,3,3,3,4 -> 4为最大值，统计1~4
    # 1出现0次，2出现2次，3出现3次，4出现1次 -> sum = 0, 4, 9, 4
    # 然后打家劫舍即可
    def deleteAndEarn2(self, nums: List[int]) -> int:
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val

        def rob(nums: List[int]) -> int:
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)

            return second

        return rob(total)


a = Solution().deleteAndEarn([3,1])
print(a)


