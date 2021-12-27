# 四数之和
# 给你一个由n个整数组成的数组nums，和一个目标值target
# 请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
# 若两个四元组元素一一对应，则认为两个四元组重复
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_len = len(nums)

        if nums_len < 4:
            return []
        elif nums_len == 4:
            if sum(nums) == target:
                return [nums]

        nums.sort()
        res = []

        # for idx, num in enumerate(nums[:-1]):
        for first in range(nums_len -1):

            for second in range(first + 1, nums_len):

                left = second + 1
                right = nums_len - 1

                while left < right:
                    sum = nums[first] + nums[second] + nums[left] + nums[right]
                    if sum == target:
                        if [nums[first], nums[second], nums[left], nums[right]] not in res:
                            res.append([nums[first], nums[second], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1

        return res

    # 官方，也是排序双指针，不过官方写了跳过了重复值和特殊边界判断，
    # 其实我写的时候也想过要不要跳过重复值，犹豫了一下没写
    def offical(self, nums: List[int], target: int):
        quadruplets = []
        if len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)

        for i in range(length -3):
            if i < 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[length -3] + nums[length - 2] + nums[length -1] < target:
                continue

            for j in range(i +1, length - 2):
                if j > j +1 and nums[j] == nums[j -1]:
                    continue

                if nums[i] + nums[j] + nums[j +1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length -1] < target:
                    continue

                left, right = j+1, length -1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets


a = Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11)
print(a)