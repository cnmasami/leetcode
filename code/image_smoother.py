# 图片平滑器

# 图像平滑器 是大小为3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
#
# 每个单元格的 平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
#
# 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
#
from itertools import product
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])

        res = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                sum = 0
                count = 0

                for x in range(max(0, i-1), min(i+2, row)):
                    for y in range(max(0, j-1), min(col, j+2)):
                        sum += img[x][y]
                        count += 1

                res[i][j] = sum // count

        return res

    # 前缀和
    def imageSmoother2(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])

        sum = [[0] * (col + 10) for _ in range(row + 10)]

        for i, j in product(range(1, row+1), range(1, col + 1)):
            sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + img[i-1][j-1]

        ans = [[0] * col for _ in range(row)]

        for i, j in product(range(row), range(col)):
            a, b = max(0, i-1), max(0, j-1)
            c, d = min(row-1, i+1), min(col-1, j+1)
            cnt = (c-a+1) * (d-b+1)
            tot = sum[c+1][d+1] - sum[a][d+1] - sum[c+1][b] + sum[a][b]
            ans[i][j] = tot // cnt

        return ans


a = Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]])
print(a)
