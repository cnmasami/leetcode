# 532. 数组中的 k-diff 数对

# 给你一个整数数组nums 和一个整数k，请你在数组中找出 不同的k-diff 数对，并返回不同的 k-diff 数对 的数目。
#
# k-diff数对定义为一个整数对 (nums[i], nums[j]) ，并满足下述全部条件：
#
# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# 注意，|val| 表示 val 的绝对值。
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = j = 0
        length = len(nums)
        ans = 0

        while i < length and j < length:
            if i == j:
                j += 1
                continue

            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            if nums[j] - nums[i] == k:
                ans += 1
                i += 1
            elif nums[j] - nums[i] > k:
                i += 1
            elif nums[j] - nums[i] < k:
                j += 1

        return ans

    # 官方排序双指针代码
    def findParis2(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, y, res = len(nums), 0, 0
        for x in range(n):
            if x == 0 or nums[x] != nums[x-1]:
                while y < n and (nums[y] < nums[x] + k or y <= x):
                    y += 1
                if y < n and nums[y] == nums[x] + k:
                    res += 1

        return res

    # 哈希表
    # 遍历数组，找出符合条件的数对。因为是寻找不同的数对，
    # 所以可以将数对放入哈希表 res，完成去重的效果，最后返回哈希表的长度即可。
    # 遍历数组时，可以将遍历到的下标当作潜在的 j，判断 j 左侧是否有满足条件的 i 来构成 k-diff 数对，
    # 而这一判断也可以通过提前将下标  j 左侧的元素都放入另一个哈希表 visited 来降低时间复杂度。
    # 如果可以构成，则将数对放入哈希表 res。
    #
    # 代码实现时，由于 k 是定值，知道数对的较小值，也就知道了另一个值，
    # 因此我们可以只将数对的较小值放入 res，而不影响结果的正确性。
    # 判断完之后，再将当前元素放入  visited，作为后续判断潜在的 nums[i]。
    def findPairs3(self, nums: List[int], k: int) -> int:
        visited, res = set(), set()

        for num in nums:
            if num - k in visited:
                res.add(num - k)
            if num + k in visited:
                res.add(num)
            visited.add(num)

        return len(res)


a = Solution().findPairs([1, 3, 1, 5, 4], k=0)
print(a)