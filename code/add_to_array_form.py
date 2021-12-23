# 对于非负整数X而言，X的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果X = 1231，那么其数组形式为[1,2,3,1]。
#
# 给定非负整数 X 的数组形式A，返回整数X+K的数组形式。
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # holder = 0
        #
        # for i in range(len(num), 0, -1):
        #     k, adder = divmod(k, 10)
        #
        #     holder, num[i-1] = divmod((num[i-1] + adder + holder), 10)
        #
        #     if k == 0 and holder == 0:
        #         return num
        #
        # if holder:
        #     num.insert(0, holder)
        #
        # return num

        # num_value = 0
        #
        # for i in num:
        #     num_value = num_value * 10 + i
        #
        # sum_value = num_value + k
        # res = []
        #
        # while sum_value:
        #     sum_value, res_value = divmod(sum_value, 10)
        #     res.insert(0, res_value)
        #
        # return res
        count = len(num) - 1
        holder = 0

        while k:
            k, adder = divmod(k, 10)

            if count >= 0:
                diveder = num[count] + adder + holder
                holder, num[count] = divmod(diveder, 10)
            else:
                if holder :
                    diveder = adder+ holder
                    holder, adder = divmod(diveder, 10)
                    # num.insert(0, adder)

                num.insert(0, adder)

            count -= 1

        if holder:
            while count >= 0:
                diveder = num[count]  + holder
                holder, num[count] = divmod(diveder, 10)
                if not holder:
                    return num
                count -= 1

            num.insert(0, holder)

        return num

    # 思路一样，但是别人比我写的简单很多
    # 但是效率没有上面的高，上面的运行时间是这个一半多一点
    def otherMethod(self, num: List[int], k:int):
        count = len(num) - 1
        holder = 0

        while count >= 0 or k != 0:
            x = num[count] if count >=0 else 0
            # y = k % 10 if k != 0 else 0
            k, y = divmod(k, 10)

            holder, answer = divmod((x + y + holder), 10)
            if count >= 0:
                if holder == 0:
                    return num
                num[count] = answer
            else:
                num.insert(0, answer)

            count -= 1
            # k = k // 10

        if holder:
            num.insert(0, 1)

        return num



# a = Solution().addToArrayForm([9], 805)
a = Solution().otherMethod([9], 805)
print(a)