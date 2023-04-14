# 自除数
# 自除数是指可以被它包含的每一位数整除的数。
#
# 例如，128 是一个 自除数 ，因为128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
# 自除数 不允许包含 0 。
#
# 给定两个整数left和right ，返回一个列表，列表的元素是范围[left, right]内所有的 自除数 。
#
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_selfdivid(num):
            d = num
            while d:
                d, mod = divmod(d, 10)
                if not mod or num % mod != 0:
                    return False
            else:
                return True

        ans = []
        for i in range(left, right + 1):
            if is_selfdivid(i):
                ans.append(i)

        return ans


a = Solution().selfDividingNumbers(47, 85)
print(a)

