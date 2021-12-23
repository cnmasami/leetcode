# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
#
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
#
# 以这种方式修改数组后，返回数组 可能的最大和 。


# 示例 1：
#
# 输入：nums = [4,2,3], k = 1
# 输出：5
# 解释：选择下标 1 ，nums 变为 [4,-2,3] 。
# 示例 2：
#
# 输入：nums = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
# 示例 3：
#
# 输入：nums = [2,-3,-1,5,-4], k = 2
# 输出：13
# 解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
from collections import Counter
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        max_sum = 0

        # sorted_nums = sorted(nums)
        nums.sort()

        i = j = 0
        while j < k:
            if i >= len(nums):
                return self.largestSumAfterKNegations(nums, j)
            if nums[i] < 0:
                nums[i] = -nums[i]
                i += 1
                j += 1
            elif nums [i] == 0:
                j += 1
            elif nums[i] > 0:
                # if sorted_nums[i-1] < 0:
                if i == 0:
                    nums[i] = -nums[i]
                else:
                    if nums[i-1] > nums[i]:
                        nums[i] = - nums[i]
                    else:
                        nums[i-1] = -nums[i-1]
                j+=1

        return sum(nums)


    def faster(self, nums: List[int], k:int):
        i = 0
        nums.sort()
        # 但是我看题解，这个如果变成for循环nums，效率会快很多
        # 有另一个比我快很多的题解，也是遍历的K，但是他在有的break的地方直接return了
        while k > 0:
            if i >= len(nums):
                nums.sort()
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                # 然后这里，判断了i == k-1 的话也直接return了，总之，这个方法还可以啦
                i += 1
                k -= 1

            elif nums[i] == 0:
                # 比如这里，直接return了
                k = 0
                break
            elif nums[i] > 0:
                nums.sort()
                break

        if k > 0 and k % 2 != 0:
            nums[0] = -nums[0]

        return sum(nums)

    def fasteeer(self, nums: List[int], k: int):
        nums.sort()

        for index in range(len(nums)):
            if k == 0:
                break

            if nums[index] < 0 :
                nums[index] = -nums[index]
                k -=1
            else:
                break

        if k % 2 == 0:
            return sum(nums)
        else:
            nums.sort()
            return sum(nums) - 2* nums[0]


# 桶排序
class Solution2:
    def largestSumAfterKNegations(self, nums: List[int], k:int):
        freq = Counter(nums)
        print(freq)
        ans = sum(nums)

        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break

        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i *2
                    break
        return ans


a = Solution().faster([8,-7,-3,-9,1,9,-6,-9,3], 8)
# a = Solution().largestSumAfterKNegations([-4,-2,-3], 4)
# a = Solution2().largestSumAfterKNegations([-4,-2,-3], 4)
print(a)


