# 下一个更大元素 II

# 给定一个循环数组nums（nums[nums.length - 1]的下一个元素是nums[0]），返回nums中每个元素的 下一个更大元素 。
#
# 数字 x的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，
# 这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums)
        res = []
        stack = []

        for num in reversed(nums):
            while stack and num >= stack[-1]:
                stack.pop()
            if stack:
                res.insert(0, stack[-1])
            else:
                res.insert(0, -1)
            stack.append(num)

        return res[:n]

    # 上面那个是倒叙遍历双重数组
    # 这个是正序遍历双重数组
    # 倒叙遍历中，栈中保存的是数组元素，正序遍历中，栈中保存的是数组下标，存下标是为了不显式地把数组拉直
    # 每移动到新的位置，把栈中所有保存的数组下标对应的值小于当前值的下标弹出栈，
    # 并且当前值是所有被弹出的位置的数据的对应的下一个最大值
    # 否则把当前下标入栈
    # （因为是正序，栈中元素的下标肯定是小于当前遍历的位置的，如果当前值大于之前的值，当前值就是之前值的最大值）
    # 但是只遍历一次是不够的，需要两次遍历，为了这两次遍历，不需要显性地将该循环数组「拉直」，
    # 而只需要在处理时对下标取模即可。
    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)

        return res



a = Solution().nextGreaterElements2([1,2,3,4,3])
print(a)