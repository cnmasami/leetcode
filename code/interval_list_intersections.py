# 区间列表的交集
# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而secondList[j] = [startj, endj] 。
# 每个区间列表都是成对 不相交 的，并且 已经排序 。
#
# 返回这 两个区间列表的交集 。
#
# 形式上，闭区间[a, b]（其中a <= b）表示实数x的集合，而a <= x <= b 。
#
# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
from typing import List


class Solution:

    def intersection(self, list1, list2):
        intersection_list = []

        if list1[0] == list2[1]:
            return [list1[0], list2[1]]
        if list2[0] == list1[1]:
            return [list2[0], list1[1]]


        if list1[0] >= list2[0] and list1[0] < list2[1]:
            if list1[1] > list2[1]:
                intersection_list = [list1[0], list2[1]]
            else:
                intersection_list = list1
        elif list2[0] >= list1[0] and list2[0] < list1[1]:
            if list2[1] > list1[1]:
                intersection_list = [list2[0], list1[1]]
            else:
                intersection_list = list2

        return intersection_list

    # 暴力法
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        ans = []

        for i in range(len(firstList)):
            for j in range(len(secondList)):
                union = self.intersection(firstList[i], secondList[j])
                if union:
                    ans.append(union)


        return ans

    # 思路： 称b为区间[a, b]的末端点，
    # 在两个数组给定的所有区间中，假设拥有最小末端点的区间是A[0],为了不失一般性，该区间出现在A数组中
    # 然后在数组B的区间中，A[0]只可能与数组B中的至多一个区间相交，如果B中存在两个区间均与A[0]相交
    # 那么他们将共同包含A[0]的末端点，但是B中的区间应该是不相交的，所以存在矛盾
    # 算法
    # 如果A[0]拥有最小的末端点，那么它只可能与B[0]相交，然后我们就可以删除区间A[0],因为它不能与其他任何区间相交了
    # 相似的，如果B[0]拥有最小的末端点，那么它只能与区间A[0]相交，然后我们就可以将B[0]删除，
    # 因为它无法再与其他区间相交了
    # 用两个指针i与j来模拟完成删除A[0]或B[0]的操作
    def offical(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            # 检查firstlist[i]与secondlist[j]是否有交集
            # lo---交集的起始位置
            # hi---交集的结束位置
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                ans.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans


a = Solution().intervalIntersection(firstList = [[3,10]], secondList = [[5,10]])
print(a)


