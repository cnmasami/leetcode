# 两个整数的汉明距离 指的是这两个数字的二进制数对应位不同的数量。
#
# 给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        def hammingDistance(num1: int, num2: int) -> int:
            hd = num1 ^ num2
            count = 0
            while hd:
                hd = hd & (hd -1)
                count += 1

            return count

        sum = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum += hammingDistance(nums[i], nums[j])

        return sum

    # 逐位统计
    # 考虑同一比特位上的值是否不同
    # 对于数组nums中的某个元素val，若其二进制的第i位为1
    # 只需要统计nums中有多少元素的第i位为0，即计算出了val与其他元素在第i位上的汉明距离之和
    # 若长度为n的数组nums的所有元素二进制位的第i位共有c个1，n-c个0，
    # 则这些元素在二进制的第i位上的汉明距离之和为c*(n-c)
    # 可以从二进制的最低位到最高位，逐步统计汉明距离，将每一位上得到的汉明距离累加即为答案
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n -c)

        return ans



a = Solution().totalHammingDistance([4, 14, 4])
print(a)