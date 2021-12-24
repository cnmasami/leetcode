# 最接近的三数之和
# 给一个长度为n的整数数组nums和一个目标值target，请你从nums中选出三个整数
# 使它们的和与target最接近
# 返回这三个数的和
# 假定每组输入只存在恰好一个解
from typing import List

# 这个其实还是枚举了所有的可能，不在中途和上次计算的结果比较，仅仅和保存的极值做比较
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)

        if nums_len == 3:
            return sum(nums)

        nums.sort()

        first_three_closest = abs(sum(nums[:3]) - target)
        last_three_closest = abs(sum(nums[-3:]) - target)

        if first_three_closest <  last_three_closest:
            closest = first_three_closest
            res = sum(nums[:3])
        else:
            closest = last_three_closest
            res = sum(nums[-3:])

        for idx, num in enumerate(nums):

            if idx > 0 and nums[idx] == nums[idx -1]:
                continue

            left = idx + 1
            right = nums_len -1

            while left < right:
                this_sum = num + nums[left] + nums[right]

                if this_sum == target:
                    return this_sum

                this_closest = abs(this_sum - target)

                if this_closest < closest:
                    closest = this_closest
                    res = this_sum

                if this_sum < target:
                    left_move = left + 1

                    while left_move < right and nums[left] == nums[left_move]:
                        left_move += 1

                    left = left_move

                elif this_sum > target:
                    right_move = right - 1

                    while right_move > left and nums[right_move] == nums[right]:
                        right_move += 1

                    right = right_move

        return res

a = Solution().threeSumClosest([-1,2,1,-4, 834, 24, 232,9, 10, -834], 50)
print(a)