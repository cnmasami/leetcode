# 有界数组中指定下标处的最大值

# 给你三个正整数 n、index 和 maxSum 。
# 你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
#
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。
#
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
#
from math import floor


class Solution:
    # 贪心 + 二分查找
    # 根据题意，需要构造一个长度为n的数组nums，所有元素均为正整数，
    # 元素之和不超过maxSum，相邻元素之差不超过1，且需要最大化nums[index]
    # 根据贪心的思想，可以使nums[index]成为数组最大的元素，并使其他元素尽可能小
    # 既从nums[index]开始，往左和往右，下标每相差1，元素值就减少1
    # 直到到达数组边界，或者减少到仅为1后保持为1不变
    # 根据这个思路，一旦nums[index]确定后，这个数组的和numsSum也就确定了
    # 并且nums[index]越大，数组和numsSum也越大。
    # 据此，可以使用二分搜索来找出最大的使得numsSum <= maxSum成立的nums[index]
    # 二分搜索的左边界为1, 右边界为maxSum
    # numsSum由三部分组成,nums[index], nums[index]左边的部分之和
    # 和nums[index]右边的部分之和
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.valid(mid, n, index, maxSum):
                left = mid
            else:
                right = mid - 1

        return left

    def valid(self, mid: int, n: int, index: int, maxSum: int) -> bool:
        # 左边的元素个数
        left = index
        # 右边的元素个数
        right = n - index - 1
        # numsSum由三部分组成,nums[index], nums[index]左边的部分之和, 和nums[index]右边的部分之和
        return mid + self.cal(mid, left) + self.cal(mid, right) <= maxSum

    # cal 用来计算单边的元素和，需要考虑边界元素是否早已下降到 1 的情况。
    def cal(self, big: int, length: int) -> int:
        if length + 1 < big:
            small = big - length
            return ((big - 1 + small) * length) // 2
        else:
            # 边界已经下降到1了
            ones = length - (big - 1)
            return (big -1 + 1) * (big -1) // 2 + ones



class Soultion_bin():
    # 根据题目描述，如果我们确定了 nums[index] 的值为 x，此时我们可以找到一个最小的数组总和。
    # 也就是说，在index 左侧的数组元素从 x-1每次递减 1，如果减到 1 后还有剩余元素，那么剩余的元素都为 1；
    # 同样的，在index 及右侧的数组元素从 x 也是每次递减 1，如果减到 1 后还有剩余元素，那么剩余的元素也都为 11。
    #
    # 这样我们就可以计算出数组的总和，如果总和小于等于maxSum，那么此时的x是合法的。
    # 随着 x的增大，数组的总和也会增大，因此我们可以使用二分查找的方法，找到一个最大的且符合条件的 x。
    #
    # 为了方便计算数组左侧、右侧的元素之和，我们定义一个函数 sum(x,cnt)，表示一共有cnt个元素，且最大值为 x 的数组的总和。
    # 函数 sum(x,cnt) 可以分为两种情况：
    # 如果 x≥cnt，那么数组的总和为 ((x + x - cnt + 1) * cnt) / 2
    # 如果 x<cnt，那么数组的总和为 ((x+1) * x) / 2 + cnt -x

    # 接下来，定义二分的左边界 left=1，右边界 right = maxSum，然后二分查找nums[index] 的值 mid，
    # 如果 sum(mid−1,index)+sum(mid,n−index)≤maxSum，那么此时的 midmid 是合法的，
    # 我们可以将 left 更新为 mid，否则我们将right更新为mid−1。
    # 最后将 left 作为答案返回即可。
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum(x, cnt):
            return (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x +1) * x // 2 + cnt -x

        left, right = 1, maxSum

        while left < right:
            mid = (left + right + 1) >> 1
            if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid -1

        return left



class Solution2():
    # 仍然按照方法一的贪心思路，根据方法一的推导，nums[index]左边或者右边的元素和，要分情况讨论。
    # 记nums[index]为 big，它离数组的某个边界的距离为length。
    # 当big≤length+1时，还未到达边界附近时，元素值就已经降为 1，并保持为 1 直到到达数组边界，
    # 此时这部分的元素和为 (big的平方 - 3big) / 2 + length + 1
    # 否则，元素会呈现出梯形的形状，此时这部分的元素和为 ((2big - length -1 ) * length) / 2
    # numsSum 由三部分组成，nums[index]，nums[index] 左边的部分之和，
    # 和 nums[index] 右边的部分之和。
    # 记 nums[index] 左边的元素个数为 left=index，
    # 右边的元素个数为 right=n−1−index。
    # 根据对称性，不妨设 left≤right。
    # 这样一来，numsSum 的组成可以用三种情况来表示。即:
    # big <= left +1:
    #    numsSum = (big的平方 - 3big) / 2 + left +1 + big + (big的平方 - 3big) / 2 + right +1
    # left +1 < big <= right +1
    #    numsSum = ((2big - left -1) * left) / 2 + big + (big的平方 - 3big) / 2 + right +1
    # right + 1 < big
    #    numSum = ((2big - left -1) * left) / 2 + big + ((2big - right -1) * right) / 2
    #
    # 对于前两种情况，我们可以分别求出上限，如果上限不超过maxSum，
    # 则可以通过解一元二次方程来求出 big。
    # 否则需要根据第三种情况解一元一次方程来求 big。
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = index
        right = n - index - 1
        if left > right:
            left, right = right, left

        upper = ((left + 1) ** 2 - 3 * (left + 1)) // 2 + left + 1 + (left + 1) + (
                    (left + 1) ** 2 - 3 * (left + 1)) // 2 + right + 1
        if upper >= maxSum:
            a = 1
            b = -2
            c = left + right + 2 - maxSum
            return floor(((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))

        upper = (2 * (right + 1) - left - 1) * left // 2 + (right + 1) + (
                    (right + 1) ** 2 - 3 * (right + 1)) // 2 + right + 1
        if upper >= maxSum:
            a = 1 / 2
            b = left + 1 - 3 / 2
            c = right + 1 + (-left - 1) * left / 2 - maxSum
            return floor(((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))

        else:
            a = left + right + 1
            b = (-left ** 2 - left - right ** 2 - right) / 2 - maxSum
            return floor(-b / a)



a = Solution().maxValue(6, 1, 10)
print(a)
