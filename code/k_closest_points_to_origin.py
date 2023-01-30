# 最接近原点的 K 个点

# 给定一个数组 points，其中points[i] = [xi, yi]表示 X-Y 平面上的一个点，
# 并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。
#
# 这里，平面上两点之间的距离是欧几里德距离（√(x1- x2)2+ (y1- y2)2）。
#
# 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。
#
import heapq
import math
import random
from typing import List


class Solution:
    # 因为欧式距离要开根号有误差，所以我们都用平方和直接表示
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 维护一个长度为k的小根堆
        q = [(-x ** 2 - y **2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)

        # 遍历剩余的元素
        for i in range(k, len(points)):
            dist = - points[i][0] ** 2 - points[i][1] ** 2
            # 先push进去再把最小的pop出来
            heapq.heappushpop(q, (dist, i))

        return [points[i] for _, i in q]

    # 借鉴快速排序的快速选择
    # 快速排序中的划分操作每次执行完之后，都能将数组分成两个部分
    # 其中小于等于分界值pivot的元素会被放到左侧部分
    # 而大于pivot元素都会被放到右侧部分
    # 与快排不同的是，在本题中我们可以根据k与pivot下标的位置关系，
    # 只处理划分结果的某一部分(而不是像快排一样需要处理两个部分)
    # 定义random_select(left, right, k)表示划分数组points的[left, right]区间
    # 并且需要找到其中第k个距离最小的点
    # 在一次划分操作完成后，设pivot的下标为i
    # 即区间[left, i -1]中的点的距离都小于等于pivot
    # 区间[i+1, right]的点的距离都大于pivot，此时会有三种情况
    # 如果k=i - left + 1 那么说明pivot就是第k个距离最小的点，我们可以结束整个过程
    # 如果k < i - left + 1， 那么说明第k个距离最小的点在pivot左侧，
    # 因此递归调用random_select(left, i-1, k)
    # 如果k > i - left + 1,那么说明第k个距离最小的点在pivot右侧
    # 因此递归调用random_select(i+1, right, k - (i- left + 1))
    # 在整个过程结束之后，第k个距离最小的点恰好就在数组points中的第k个位置，
    # 并且其左侧的所有点的距离都小于它。此时，我们就找到了前k个距离最小的点。

    def kClosest3(self, points: List[List[int]], k: int) -> List[List[int]]:
        def random_select(left: int, right: int, k: int):
            idx = random.randint(left, right)
            pivot = points[idx][0] ** 2 + points[idx][1] ** 2
            points[right], points[idx] = points[idx], points[right]

            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]

            if k < i - left + 1:
                random_select(left, i -1, k)
            elif k > i - left + 1:
                random_select(i + 1, right, k - (i - left + 1))

        n = len(points)

        random_select(0, n -1, k)
        return points[:k]

a = Solution().kClosest3(points = [[3,3],[5,-1],[-2,4]], k = 2)
print(a)