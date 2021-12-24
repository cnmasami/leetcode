# 给你一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c，使得a+b+c=0
# 请找出所有和为0且不重复的三元组

# 答案中不可以包含重复的三元组
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序加双指针
        if len(nums) < 3:
            return []

        # if len(nums) == 3 and sum(nums) == 0:
        #     return [nums]

        nums.sort()

        res = []

        for idx, num in enumerate(nums):
            # 说明之后的数字都比0大，相加结果不会为0了
            if num > 0:
                break

            # 如果在我的代码中加入去重
            if idx > 0 and nums[idx] == nums[idx -1]:
                continue

            target = 0 - num
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    if [num, nums[left], nums[right]] not in res:
                        res.append([num, nums[left], nums[right]])
                    # 如果这里用break，会漏掉解，因为结果并不唯一
                    # break
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1

        return res


    # 官方题解，我上面的题解运行出来耗时很久
    # 官方的思路也是排序然后双指针，但是官方会跳过重复值
    def offical(self, nums: List[int]):
        n = len(nums)
        nums.sort()
        ans = []

        # 枚举a
        for first in range(n):
            # 需要和上一次枚举的数不同
            if first > 0 and nums[first] == nums[first -1]:
                continue
            # c对应的指针初始指向数组的最右端
            third = n - 1
            target =- nums[first]
            # 枚举b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不同
                if second > first + 1 and nums[second] == nums[second -1]:
                    continue
                # 需要保证b的指针在c的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                # 如果指针重合，随着b后续的增加，就不会有满足a+b+c=0并且b<c的c了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


a = Solution().threeSum([0,0,0])
print(a)
