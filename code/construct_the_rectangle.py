# 构造矩形

# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
#
# 你设计的矩形页面必须等于给定的目标面积。
# 宽度 W不应大于长度 L ，换言之，要求 L >= W 。
# 长度 L 和宽度 W之间的差距应当尽可能小。
# 返回一个数组[L, W]，其中 L 和 W 是你按照顺序设计的网页的长度和宽度。
#
from math import sqrt
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]




a = Solution().constructRectangle(122122)
print(a)