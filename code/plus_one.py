# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        holder = 1
        for i in range(len(digits), 0, -1):
            # if i == len(digits)-1:
            holder, digits[i-1] = divmod((digits[i-1] + holder), 10)

            #我觉得可以加这个,
            # 结果加了这个执行用时也没有减少，反而内存消耗增加了0.1m
            if holder == 0:
                return digits

        if holder == 1:
            digits.insert(0, 1)

        return digits


# 官方题解：
# 找出数组末尾有没有出现9，
# 如果没有9，就直接在末尾加1
# 如果末尾有若干个9，只要找到末尾第一个不是9的元素，加一，然后将末尾的9置为0
# 如果所有的元素都是9，只要构造一个长度比digits多1位的新数组，将首元素置为1，其余元素为0

class SolutionOffical:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + [0] * n

a = Solution().plusOne([9,9])
print(a)
