# 最大三角形面积


#给你一个由 X-Y 平面上的点组成的数组 points ，
# 其中 points[i] = [xi, yi] 。从其中取任意三个不同的点组成三角形，返回能组成的最大三角形的面积。
# 与真实值误差在 10-5 内的答案将会视为正确答案。
from typing import List


class Solution:
    # 把三个点A(X1, Y1), B(X2, Y2), C(X3, Y3)分别向x轴投影，分别得到点EDF
    # 会得到几个梯形，然后计算几个梯形的面积相加相减得到三角形的面积
    # 三角形ABC的面积=梯形BDEA的面积+梯形AEFC的面积−梯形BDFC的面积 =
    # [(y1+y2)∗(x1−x2)]/2+[(y3+y1)∗(x3−x1)]/2−[(y2+y3)∗(x3−x2)]/2=
    # [(y1 + y2) * (x1 - x2)]/2 + [(y3 + y1) * (x3 - x1)]/2 - [(y2 + y3) * (x3 - x2)]/2=
    # [(y1+y2)∗(x1−x2)]/2+[(y3+y1)∗(x3−x1)]/2−[(y2+y3)∗(x3−x2)]/2 =
    # 1/2∗[x1(y2−y3)+x2(y3−y1)+x3(y1−y2)]=
    # 1/2 * [x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)]=
    # 1/2∗[x1(y2−y3)+x2(y3−y1)+x3(y1−y2)]
    # 使用三重for循环，从题目给出的二维坐标中取出3个点，根据面积公式求组成的三角形面积
    # 官方题解给出的三角形面积公式：
    # 向量
    # x1 y1
    # x2 y2
    # x3 y3
    # = 1/2 *(x1y2 + x2y3 + x3y1 - x1y3 - x2y1 -x3y2)
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        n = len(points)

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    res = max(res, 0.5 * abs(x1 * (y2 -y3) + x2 * (y3 - y1) + x3 * (y1 -y2)))

        return res

