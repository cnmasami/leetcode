# 检查整数及其两倍数是否存在
# 给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。
#
# 更正式地，检查是否存在两个下标 i 和 j 满足：
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visted = set()

        for num in arr:
            if num * 2 in visted or num / 2 in visted:
                return True
            visted.add(num)

        return False


a = Solution().checkIfExist([10,2,5,3])
print(a)