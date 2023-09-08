# 最长湍流子数组

# 给定一个整数数组 arr ，返回 arr 的 最大湍流子数组的长度 。
#
# 如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 湍流子数组 。
#
# 更正式地来说，当 arr 的子数组 A[i], A[i+1], ..., A[j] 满足仅满足下列条件时，我们称其为湍流子数组：
#
# 若 i <= k < j ：
# 当 k 为奇数时， A[k] > A[k+1]，且
# 当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j ：
# 当 k 为偶数时，A[k] > A[k+1] ，且
# 当 k 为奇数时， A[k] < A[k+1]。
from typing import List


class Solution:
    # 滑动窗口
    # 设数组arr的长度为n，窗口[left, right] 0 <= left <= right <= n-1为当前的窗口
    # 窗口内构成了一个湍流子数组，随后，需要考虑下一个窗口的位置
    # 根据湍流子数组的定义，当0< right < n -1的时候
    # 如果arr[right-1] < arr[right]且arr[right] > arr[right] + 1，
    # 则[left, right+1]也构成[湍流子数组], 因此需要将right右移一个单位
    # 同理，><也构成湍流子数组，right右移
    # 否则，[right -1, right+1]无法构成子数组，因此需要将left移到right,令left=right
    # 此外，我们还需要特殊考虑窗口长度为1即left与right相等的情况，只要arr[right]!= arr[right+1]
    # 就可以将right右移一个单位，否则left和right都要同时右移
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        left = right = 0

        while right < len(arr) -1:
            if left == right:
                if arr[left] == arr[right + 1]:
                    left += 1

                right += 1
            else:
                if arr[right-1] < arr[right] > arr[right+1]:
                    right += 1
                elif arr[right -1] > arr[right] < arr[right+1]:
                    right += 1
                else:
                    left = right

            res = max(res, right - left + 1)

        return res

    # 动态规划
    # 状态定义： increased[i]：以arr[i]结尾，并且arr[i-1] < arr[i]的湍流子数组的长度
    # decreased[i]：以arr[i]结尾，并且arr[i-1] > arr[i]的湍流子数组的长度
    # 状态转移方程
    # increased[i] = decreased[i-1] + 1 if arr[i-1] < arr[i] for i > 0
    # decreased[i] = increased[i-1] + 1 if arr[i-1] > arr[i] for i > 0
    def maxTurbulenceSize2(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        increased = [0] * n
        decreased = [0] * n

        increased[0] = 1
        decreased[0] = 1
        res = 1

        for i in range(1, n):
            if arr[i-1] < arr[i]:
                increased[i] = decreased[i-1] + 1
                decreased[i] = 1
            elif arr[i-1] > arr[i]:
                decreased[i] = increased[i-1] + 1
                increased[i] = 1
            else:
                increased[i] = 1
                decreased[i] = 1

            res = max(res, increased[i], decreased[i])

        return res
    
    # 动态规划 空间优化版
    def dp2(self, arr: List[int]) -> int:
        down, up = 1, 1
        res = 1

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                down = up + 1
                up = 1
            elif arr[i -1] < arr[i]:
                up = down + 1
                down = 1
            else:
                down = up = 1

            res = max(res, up, down)

        return res




a = Solution().maxTurbulenceSize([9,9])
print(a)
