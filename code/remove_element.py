# 给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        slow = fast = 0

        while fast < len(nums):
            if nums[slow] == val and nums[fast] == val:
                fast += 1
            elif nums[slow] == val and nums[fast] != val:
                break
            else:
                slow += 1
                fast += 1

        ans = slow + (len(nums) - fast)

        nums[slow: fast] = nums[fast:]
        return ans

    # 左右指针，如果右指针指向当前要处理的元素，左指针指向下一个将要被赋值的元素
    # 如果右指针指向的元素不等于val，一定是输出数组的一个元素，将右指针指向的元素复制到做指针的位置，将左右指针同时右移
    # 如果右指针指向的元素等于val，不能在输出数组里，左指针不动，右指针右移一位
    def other_method(self, nums: List[int], val:int) ->int:
        slow = fast = 0

        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            elif nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        return slow

    # 如果要移出的元素正好在数组开头，则需要把每一个元素都左移一位
    # 由于题目【元素顺序可以改变】，只需要将最后一个元素移到开头，得到新的序列即可
    # 使用双指针，初始时分别位于首位，往中间遍历
    # 如果左指针left指向的元素等于val，此时右指针指向的元素复制到左指针left的位置，然后右指针right左移一位
    # 如果赋值过来的元素也恰好等于val，可以继续把右指针right指向的元素的值赋值过来，直到左指针指向的元素的值不等于val为止
    # 当左右指针重合的时候，遍历结束
    def double_pointer_opt(self, nums: List[int], val:int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return left




a = Solution().double_pointer_opt([0,1,2,2,3,0,4,2], 2)
print(a)


