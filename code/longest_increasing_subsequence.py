# 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
from typing import List


class Solution:
    # 动态规划
    # 定义dp[i]为考虑前i个元素，以第i个数字结尾的最上升子序列的长度，注意nums[i]必须被选取
    # 从小到大计算dp数组的值，在计算dp[i]之前，已经计算出dp[0...i-1]的值
    # 则状态转移方程为dp[i] = max(dp[j]) + 1, 其中0 <= j < i 且 num[j] < num[i]
    # 即考虑往dp[0...i-1]中最长的上升子序列后面再加一个nums[i]
    # 由于dp[j]代表nums[0...j]中以nums[j]结尾的最长上升子序列
    # 所以如果能从dp[j]这个状态转移过来，那么nums[i]必然要大于nums[j]
    # 才能将nums[i]放在nums[j]后面以形成更长的上升子序列
    # 最后整个数组的最长上升子序列即所有dp[i]中的最大值
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    # 贪心 + 二分查找
    def lengthOfLIS2(self, nums: List[int]) -> int:
        size = len(nums)

        if size < 2:
            return size

        # 为了防止后序逻辑发生数组索引越界，先把第一个数放进去
        tail = [nums[0]]
        for i in range(1, size):
            # 【逻辑1】比tail数组实际有效的末尾的那个元素大
            # 先尝试是否可以接在末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            # 下面是比tail数组实际有效的末尾元素小的情况
            # 使用二分查找，在有序数组tail中
            # 找到第一个大于等于nums[i]的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left < right:
                # 选左中位数
                # mid = left + (right - left) // 2
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    # 中位数肯定不是要找的数，把它写在分支的前面
                    left = mid + 1
                else:
                    right = mid
            #  走到这里是因为【逻辑1】的反面，因此一定能找到第一个大于等于nums[i]的元素
            # 因此无需再单独判断
            tail[left] = nums[i]

        return len(tail)





a =Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
print(a)
