# 和为 K 的子数组

# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
from typing import List


class Solution:
    # 前缀和，但会超时
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp_sum = [0] * (len(nums) + 1)
        ans = 0

        for i in range(len(nums)):
            dp_sum[i + 1] = dp_sum[i] + nums[i]
            if dp_sum[i + 1] == k:
                ans += 1

            for j in range(1, i + 1):
                if dp_sum[i + 1] - dp_sum[j] == k:
                    ans += 1

        return ans

        # for left in range(len(nums)):
        #     for right in range(left, len(nums)):
        #         if dp_sum[right + 1] - dp_sum[left] == k:
        #             ans += 1

        # return ans

    # 暴力
    def subarraySum2(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_sum = sum(nums[i:j+1])

                if sub_sum == k:
                    count += 1

        return count

    # 暴力优化
    def subarraySum3(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1

        return count

    # 前缀和+哈希优化
    def subarraySum4(self, nums: List[int], k: int) -> int:
        # key:前缀和 val:对应的数量
        # 初始化 前缀和为0的个数为1
        pre_sum_map = {0: 1}

        # 记录自首个元素累计的前缀和
        pre_sum = 0
        count = 0

        # 遍历所有元素：计算前缀和，寻找k，更新map
        for num in nums:
            # 累计前缀和
            pre_sum += num

            # 根据pre - (pre-k) = k, 寻找连续数组为pre -k 的数量，即连续数组的和为k的数量
            # 说明： pre为自首个元素开始累计的连续数组
            # pre - k  为包含在连续数组pre中的一个连续子数组(自首个元素开始累计)
            # 连续数组 - 连续子数组 = 连续子数组，对应pre - (pre -k) = k
            # 则连续数组的和为pre-k的数量，即为连续数组的和为k的数量
            if pre_sum - k in pre_sum_map:
                # 因为pre_sum_map里存的是前缀和，而pre_sum也是前缀和，
                # pre_sum_map[pre_sum - k]和当前元素一定是连续的
                count += pre_sum_map[pre_sum - k]

            if pre_sum in pre_sum_map:
                pre_sum_map[pre_sum] += 1
            else:
                pre_sum_map[pre_sum] = 1

        return count






a = Solution().subarraySum4([1,1,1], 2)
print(a)
