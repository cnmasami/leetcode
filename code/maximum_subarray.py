# 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
from typing import List


class Solution:
    # 怎么感觉贪心和动态规划思路差不多啊
    # 贪心
    # 如果这个元素之前的所有元素的和小于0，舍弃，将当前计算和设置为当前元素，并及时更新最大和
    def maxSubArray(self, nums: List[int]) -> int:
        # 最大和设置为list第一个元素
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            # 这句如果换成 current_sum = max(num, current_sum+num)运行速度会更快
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num

            max_sum = max(max_sum, current_sum)

        return max_sum

    # 动态规划
    # 用fi代表以第i个数组结尾的【连续子数组的最大和】，
    # 那么只需要求出每个位置的fi，然后返回fi数组中的最大值即可
    def dynamic(self, nums: List[int]) -> int:

        for idx in range(1, len(nums)):
            if nums[idx -1] >= 0:
                nums[idx] += nums[idx -1]

        return max(nums)

    def binary(self, nums: List[int]) -> int:
        return self.__max_sub_array(nums, 0, len(nums) -1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = (left + right) >> 1

        return (max(self.__max_sub_array(nums, left, mid),
                    self.__max_sub_array(nums, mid +1, right),
                    self.__max_cross_array(nums, left, mid, right)))


    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含nums[mid]元素的最大连续子数组的和
        # 思路是看看左边”扩散到底“， 得到一个最大数， 右边扩散到底，得到一个最大时
        # 然后加上中间数
        left_max_sum = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_max_sum = max(left_max_sum, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1

        return left_max_sum + nums[mid] + right_sum_max





# a = Solution().maxSubArray([5,4,-1,7,8])
a = Solution().dynamic([5,4,-1,7,8,0,8,-9,10])
print(a)


