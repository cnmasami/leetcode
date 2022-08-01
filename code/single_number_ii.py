# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
import collections
import random
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()

        for num in nums:
            num_set.add(num)

        return (3 * sum(num_set) - sum(nums)) // 2


    def singleNumberHash(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)

        ans = [num for num, ooc in freq.items() if ooc==1][0]
        return ans

    # 通过快速选择算法得到空间复杂度O（1）, 时间复杂度O（n）的算法
    # 每次迭代随机选择一个元素x，将满足y <= x的元素y放到数组前半，满足y > x 的元素y放到数组后半
    # 假设数组前半长度为K，由于唯一元素所在的部分长度一定为3*left+1，
    # 那么若k%3=1，说明唯一元素在数组前半，否则在数组后半，可以递归求解
    def singleNumberQuickSort(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            k = random.randint(left, right)
            nums[right], nums[k] = nums[k], nums[right]
            i, j = 1, right - 1
            while i <= j:
                while i < right and nums[i] <= nums[right]:
                    i += 1
                while j >= left and nums[j] > nums[right]:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[i], nums[right] = nums[right], nums[i]
            if (i - right + 1) % 3 != 0:
                right = i
            else:
                left = i + 1

        return nums[left]

    # 位数统计
    # 利用int类型固定为32位
    # 使用一个长度为32的list cnt 记录下所有数值的每一位共出现了多少次1
    # 再对cnt list的每一位进行mod 3 操作，得到的就是只出现一次的数字的二进制表示
    # 再将二进制转换为十进制数字得到答案
    def countBinary(self, nums: List[int]) -> int:
        # 因为n的范围是正负2*31次方，所以用32位的数组存二进制的和
        # 注意这里count左侧是较低位，右侧是较高位
        # 可以用最右侧存放正负号
        count = [0] * 33
        for x in nums:
            if x >= 0:
                # 最后一位存符号
                count[32] += 1
            else:
                # 如果为负，反为正数
                x = -x
            # 从0遍历到31
            for i in range(32):
                # 如果i位为1，则更新count
                if (x >> i) & 1 == 1:
                    count[i] += 1

        ans = 0
        for i in range(32):
            if count[i] % 3 == 1:
                ans += 1 << i
        sign = count[32] % 3
        return ans if sign  == 1 else -ans


    def offical_countBinary(self, nums: List[int]) -> int:
        ans = []
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans





a = Solution().singleNumber([0,1,0,1,0,1,99])
print(a)
