# 区域和检索 - 数组和修改
# 给你一个数组 nums ，请你完成两类查询。
#
# 其中一类查询要求 更新 数组nums下标对应的值
# 另一类查询要求返回数组nums中索引left和索引right之间（包含）的nums元素的 和，其中left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组nums中索引left和索引right之间（包含）的nums元素的 和（即，nums[left] + nums[left + 1], ..., nums[right]）
#
from typing import List


class NumArray:
    # 从前缀和会超时，因为更新的时候要更新从index之后的每一个前缀和
    # 分块处理
    # 设数组大小为n，将数组分为多个块，每个块大小size，
    # 最后一个块的大小为剩余的不超过size的元素数目，那么块的总数为 n/size向上取整
    # 用一个数组sum保存每个块的元素和
    # sumRange看left和right在不在一个块内，
    # 如果在一个块内直接返回块内区间的元素之和
    # 假设left位于块b1的第i个元素，right位于块b2的第j个元素
    # 计算b1的[i, size -1]的元素和sum1，b2中[0, j]的元素之和sum2
    # 第b1个块到第b2-1个块的元素和sum3
    # 返回sum1+sum2+sum3
    def __init__(self, nums: List[int]):
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)  # n / size 向上取整

        for i, num in enumerate(nums):
            sums[i // size] += num

        self.nums = nums
        self.sums = sums
        self.size = size

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        m = self.size
        b1, b2 = left // m, right // m
        if b1 == b2:
            return sum(self.nums[left: right +1])

        return sum(self.nums[left:(b1+1) * m]) + sum(self.sums[b1 + 1:b2]) \
           + sum(self.nums[b2 * m:right + 1])


# 线段树
# 线段树是一个二叉树，每个结点保存数组nums在区间[s, e]的最小值，最大值或者总和等信息
# 线段树可以用数也可以用数组（堆式存储）来实现。
# 对于数组实现，假设根结点的下标为0，如果一个结点在数组的下标为node，
# 那么它的左子结点下标为node*2+1，右子结点下标为node*2+2
# 1.建树build函数
# 我们在结点node保存数组nums在区间[s,e]的总和
# s=e时，结点node是叶子结点，它保存的值等于nums[s]
# s<e时，结点node的左子结点保存区间[s, (s+e)地板除2]的总和，
# 右子结点保存区间[(s+e)地板除2+1, e]的总和
# 那么结点node保存的值等于它的两个子结点保存的值之和
# 假设nums的大小为n，我们规定根节点node=0保存区间[0,n-1]的总和，
# 然后自下而上递归地建树
# change函数
# 当我们要修改nums[index]的值时，我们找到对应区间[index, index]的叶子结点
# 直接修改叶子结点的值为val，并自下而上递归地更新父结点的值
# 范围求和range函数
# 给定区间[left, right]时，我们将区间[left, right]拆成多个结点对应的区间
# 如果结点node对应的区间与[left, right]相同，可以直接返回该结点的值，即当前区间和
# 如果结点node对应的区间与[left, right]不同，设左子结点对应的区间的右端点为m
# 那么将区间[left, right]沿点m拆成两个区间，分别计算左子结点和右子结点
# 我们从根结点开始递归地拆分区间[left, right]
class SegmentTreeNumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.seg = [0] * (n * 4)
        self.build(nums, 0, 0, n -1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return

        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return

        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m+1, e)

        self.seg[node] = self.seg[node * 2+1] + self.seg[node*2+2]

    def range(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]

        m = s + (e - s) // 2
        if right <= m:
            return self.range(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range(left, right, node * 2 + 2, m+1, e)

        return self.range(left, m, node * 2 +1, s, m) + \
               self.range(m+1, right, node*2+2, m+1, e)

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n-1)

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0, self.n-1)


# 树状数组
# 树状数组是一种可以动态维护序列前缀和的数据结构(序列下标从1开始)
# 它的功能是：
# 单点修改add(index, val)：把序列第index个数增加val
# 区间查询prefixSum(index)：查询前index个元素的前缀和
# 因为题目要求实现更新nums在某个位置的值
# 因此我们保存原始的nums数组
# 构造函数
# 树状数组初始对应一个零序列，因此我们遍历nums数组，调用add函数来更新树状数组
# update函数
# 获取nums在index的增加值，调用add函数更新树状数组，并更新nums[index]=val
# sumRange函数
# 区间和[left, right]可以转化为两个前缀和之差，
# 调用树状数组的prefixSum函数获取前right+1个元素的前缀和sum1
# 和前left个元素的前缀和sum2，返回sum1-sum2
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, index: int, val: int):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index

    def prefixSum(self, index) -> int:
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)




a = NumArray([1, 3, 5])
print(a.sumRange(0, 2))
a.update(1, 2)
print(a.sumRange(0, 2))