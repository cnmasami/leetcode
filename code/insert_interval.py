# 插入区间
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]

# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10]重叠。
#
from typing import List


class Solution:
    # 总的来说，就是思路还是有的，但是写不出更巧妙简洁的办法
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        inserted = []
        n = len(intervals)

        # a   [ ]
        # b [ ]       [  ]
        for i in range(n):
            interval = intervals[i]

            is_lo = max(newInterval[0], interval[0])
            is_hi = min(newInterval[1], interval[1])

            if is_lo <= is_hi:
                lo = min(newInterval[0], interval[0])
                hi = max(newInterval[1], interval[1])

                newInterval = [lo, hi]

            elif newInterval[0] < interval[0]:
                inserted.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                inserted.append(interval)

        # inserted.extend(intervals[i:])
        inserted.append(newInterval)

        return inserted

    def offical(self, intervals:List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = []

        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append(newInterval)
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])

        return ans

a = Solution().insert(intervals = [], newInterval = [5,7])
print(a)



