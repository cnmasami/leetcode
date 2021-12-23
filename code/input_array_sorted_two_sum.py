# 给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
# 如果有有序数组，就考虑双指针
from typing import List

# [2, 3, 5, 7] 10


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    if not numbers:
        return []

    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1

    return []