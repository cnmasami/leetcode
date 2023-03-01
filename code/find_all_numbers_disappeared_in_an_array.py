# 找到所有数组中消失的数字
# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
#
from typing import List


class Solution:
    # 鸽笼原理，1-n的位置表示1-n个笼子，如果出现过，相应位置的笼子就会被被占掉
    # 因为数字范围在1-n之间，所以用不在这个范围内的数字表示被占，
    # 给所有的对应鸽笼位置上的对应的数字加上n，增加后这些数字必然大于n
    # （题解有个办法是相对位置的数字取反，最终判断是否是正值）
    # 遍历到某个位置，这个位置可能被占过，
    # 使用值 模 n，获得原本的数字的值就是正确的需要占的鸽笼的位置
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            nums[(num -1) % n] += n

        return [idx+1 for idx, num in enumerate(nums) if num <= n]


a = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(a)

