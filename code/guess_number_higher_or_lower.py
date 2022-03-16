# 猜数字大小
# 猜数字游戏的规则如下：
#
# 每轮游戏，我都会从1到n 随机选择一个数字。 请你猜选出的是哪个数字。
# 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1或 0）：
#
# -1：我选出的数字比你猜的数字小 pick < num
# 1：我选出的数字比你猜的数字大 pick > num
# 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
# 返回我选出的数字。
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 1:
                low = mid + 1

        return low



