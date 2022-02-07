# 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        # intervals = sorted(intervals, key=lambda k: k[0])
        # prev = intervals[0]
        # idx, n = 1, len(intervals)
        #
        # while idx < n:
        #     current = intervals[idx]
        #     # 这里过于冗余了，主要是因为最开始的时候没有排序，排序是后来改的，如果排序了只需要比较prev[1]和current的关系就可以了
        #     is_lo = max(prev[0], current[0])
        #     is_hi = min(prev[1], current[1])
        #
        #     if is_lo <= is_hi:
        #
        #         lo = min(prev[0], current[0])
        #         hi = max(prev[1], current[1])
        #
        #         prev = [lo, hi]
        #     else:
        #         ans.append(prev)
        #         prev = current
        #
        #     idx += 1
        #
        # ans.append(prev)
        #
        # return ans
        # 根据官方题解优化我的代码
        intervals.sort(key=lambda k: k[0])
        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] < interval[0]:
                ans.append(prev)
                prev = interval
            else:
                lo = min(prev[0], interval[0])
                hi = max(prev[1], interval[1])

                prev = [lo, hi]

        ans.append(prev)

        return ans



    # 思路差不多吧，但是官方的代码简洁的多
    def offical(self, intervals: List[List[int]]):

        intervals.sort(key=lambda x:x[0])

        merged = []

        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 这里这样因为方法开头已经按照嵌套list的[0]排过序了，只关系end端
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

a = Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
print(a)



