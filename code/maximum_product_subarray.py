# 乘积最大子数组
# 给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个32-位 整数。
#
# 子数组 是数组的连续子序列。
#
from typing import List


class Solution:
    # 动态规划
    # 用fmax(i)来表示以第i个元素结尾的乘积最大子数组的乘积，a表示输入参数nums
    # 那么，我们很容易推导出状态转移方程
    # fmax(i) = max(f(i-1) * ai, ai)
    # 表示以第i个元素结尾的乘积最大子数组的乘积可以考虑ai加入前面的fmax(i-1)对应的一段
    # 或者单独成为一段，这里两种情况下取最大值。求出所有的fmax(i)之后选取最大的一个作为答案
    # 但是在这里这种情况是错的，为什么呢
    # 因为如果有负数，比如a={5,6,−3,4,−3}，那么答案应该是所有数字的乘积
    # 但是前面的算法得到的答案是30，
    # 所以当前位置的最优解未必是由前一个位置的最优解转移得到的
    # 可以根据正负性分类讨论
    # 如果当前位置是一个负数，那么我们希望以它前一个位置结尾的某个段的积也是负数，这样就可以负负得正
    # 并且我们希望这个积尽可能负得更多，即尽可能小
    # 如果当前位置是一个正数，我们更希望以它前一个位置结尾的某个段的积也是个正数
    # 并希望它尽可能得大
    # 于是这样可以再维护一个fmin，表示以第i个元素结尾的乘积最小子数组的乘积，可以得到动态转移方程
    # fmax(i)= max{fmax(i−1)×ai, fmin(i−1)×ai,ai}
    # fmin(i)= max{fmax(i−1)×ai, fmin(i−1)×ai,ai}
    # 由于第 i 个状态只和第 i−1 个状态相关，根据「滚动数组」思想，
    # 我们可以只用两个变量来维护 i−1 时刻的状态，一个维护
    # f max，一个维护 f min
    # 简单版解释
    # 遍历数组时计算当前最大值，不断更新
    # 令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
    # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
    # 当负数出现时则imax与imin进行交换再进行下一步计算

    def maxProduct(self, nums: List[int]) -> int:
        max_f = min_f = ans = nums[0]
        for num in nums[1:]:
            mx = max_f
            mn = min_f
            max_f = max(mx * num, max(num, mn * num))
            min_f = min(mn * num, min(num, mx * num))
            ans = max(max_f, ans)

        return ans


    def maxProduct2(self, nums: List[int]) -> int:
        max_p = float('-inf')
        imax = imin = 1

        for num in nums:
            if num < 0:
                imax, imin = imin, imax

            imax = max(imax * num, num)
            imin = min(imin * num, num)

            max_p = max(max_p, imax)

        return max_p


a = Solution().maxProduct2([2,3,-2,4])
print(a)