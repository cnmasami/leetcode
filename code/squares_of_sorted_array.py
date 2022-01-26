# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list = []

        for num in nums:
            square_list.append(num * num)

        square_list.sort()

        return square_list

        # return sorted(num * num for num in nums)

    # 非负数平方后，数组仍然是升序
    # 负数平方后，数据是降序
    # 找到数组中负数与非负数的分界线，之后可以用【归并排序】的方法
    # 也就是说，0到分界单调递减，分解到结尾单调递增
    # 由于已经得到了两个有序的子数组，可以使用归并的方法进行排序，具体地，使用两个指针分别指向位置neg和neg+1
    # 每次比较两个指针对应的数，选择较小的那个放入答案并移动指针，当某一指针移动到边界时，将另一指针还未遍历到的数依次放入答案。
    def doublePointer(self, nums: List[int]) -> List[int]:
        n = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break

        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0 :
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i]* nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1

        return ans


    # 使用两个指针分别指向位置0和n-1，每次比较两个指针对应的数，选择较大的那个逆序放入答案并移动指针
    # 这种方法无需处理某一指针移动至边界的情况
    def otherDoublePointer(self, nums: List[int]):
        n = len(nums)
        ans = [0] * n
        i, j, pos = 0, n-1, n-1

        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i +=1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1

            pos -= 1

        return ans



a = Solution().sortedSquares([-7,-3,2,3,11])
print(a)