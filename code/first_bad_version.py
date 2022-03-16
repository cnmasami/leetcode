#你是产品经理，目前正在带领一个团队开发新的产品。
# 不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

# 你可以通过调用bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。
# 实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2

            if isBadVersion(middle) and not isBadVersion(middle -1):
                return middle
            elif isBadVersion(middle) and isBadVersion(middle -1):
                right = middle -2
            elif not isBadVersion(middle):
                left = middle + 1

        return left


    def offical(self, n):
        left = 1
        right = n

        # 循环直至区间左右端点相同
        while left < right:
            # middle = (left + right) // 2
            # 防止计算时溢出
            middle = left + (right - left) // 2

            if isBadVersion(middle):
                # 答案在区间[left, mid]中
                right = middle
            else:
                # 答案在区间[middld+1, right]中
                left = middle + 1
        # 此时有left == right，区间缩为一个点，即为答案
        return left

