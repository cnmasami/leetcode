# 和可被 K 整除的子数组

# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。
#
# 子数组 是数组的 连续 部分。
from typing import List


class Solution:
    # 普通前缀和，会超时
    def subarraySum(self, nums: List[int], k: int) -> int:

        dp = [0] * (len(nums) +1)

        count = 0

        for i in range(len(nums)):
            dp[i+1] = dp[i] + nums[i]
            if dp[i+1] % k == 0:
                count += 1
            for j in range(1, i+1):
                if (dp[i+1] - dp[j]) % k == 0:
                    count += 1

        return count

    # 前缀和 + 哈希表 +  逐一统计
    # p[i]表示前缀和
    # 判断子数组的和能否被k整除就等价于判断(p[i]-p[j]) mod k ==0
    # 根据同余定理？只要p[j] mod k == p[i] mod k 就可以保证上面的等式成立
    # 模的分配率： (a + b) mod c = (a mod c + b mod c) mod c
    # 同余定理 给定一个正整数m，如果两个整数a和b满足a-b能够被m整除，即(a-b)/m得到一个整数，
    # 那么就称整数a与b对模m同余，记作a≡b(mod m)。对模m同余是整数的一个等价关系
    # 维护一个以前缀和模k的值为键，出现次数为值的哈希表
    # 需要注意的一个边界条件是，我们需要对哈希表初始化，记录record[0] = 1
    # 这样就考虑了前缀和本身被k整除的情况
    def subarraySum2(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        total = ans = 0
        for num in nums:
            total += num
            modulus = total % k
            same = record.get(modulus, 0)
            ans += same
            # 并不关心前缀和本身的值
            record[modulus] = same + 1

        return ans

    # 前缀和 + 哈希表 + 单次统计
    # 此方法延续上面的思路，只是不再边遍历边计算答案，而是从排列组合的角度考虑如何统计答案
    # 考虑上面的思路，我们可以在遍历的时候只维护哈希表，在遍历结束后，再遍历哈希表，用排列组合的方法来统计答案
    # 对于哈希表中的每个键值对(x, cx)，它表示前缀和x(在模k的意义下)出现了c次
    # 那么这些出现的位置两两之间都可以构成可被k整除的连续子数组，数量即为(cx(cx-1))/2个可被k整除的连续子数组
    # 例如当c=5的时候，那么两两组合共有5*4/2 = 10个子数组
    # 举一个具体的例子，给定数组为 nums=[4,5,0,−2,−3,1]以及 k=5，
    # 那么前缀和 P=[4,9,9,7,4,5]，对 k取模即为 [4,4,4,2,4,0]，
    # 那么可以哈希表中包含的键值对为 (0,2),(2,1),(4,4)。以 (4,4) 为例：
    # 对于 c=4，对应的前缀和为 P[0],P[1],P[2],P[4]，那么一共有{4}{2} = 6 个和能被 k 整除的连续子数组，
    # 分别是 nums[1:1],nums[1:2],nums[1:4],nums[2:2],nums[2:4],nums[4:4],
    # 其中nums[i:j] 表示下标从 i 到 j 的子数组。
    def subarraySum3(self, nums: List[int], k: int) -> int:
        record = {0:1}
        total = 0

        for num in nums:
            total += num
            modulus = total % k
            record[modulus] = record.get(modulus, 0) + 1

        ans = 0
        for x, cx in record.items():
            ans += cx * (cx -1) // 2

        return ans





a = Solution().subarraySum(nums=[4,5,0,-2,-3,1], k=5)
print(a)
