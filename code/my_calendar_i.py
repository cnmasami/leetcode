# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
#
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
#
# 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数x 的范围为， start <= x < end 。
#
# 实现 MyCalendar 类：
#
# MyCalendar() 初始化日历对象。
# boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。

from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for book in self.booked:
            max_start = max(start, book[0])
            min_end = min(end, book[1])

            if max_start < min_end:
                return False

        self.booked.append([start, end])

        return True


class MyCalendar_bisect:
    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        i = self.booked.bisect_left(end)
        if i == 0 or self.booked.items()[i-1][1] <= start:
            self.booked[start] = end
            return True

        return False


class MyCalendar_segmentTree:
    def __init__(self):
        self.tree = set()
        self.lazy = set()


    def query(self, start, end, l, r, idx) -> bool:
        if r < start or end < l:
            return False

        if idx in self.lazy:
            return True

        if start <= l and r <= end:
            return idx in self.tree
        mid = (l+r) // 2

        return self.query(start, end, l, mid, 2 * idx) or \
               self.query(start, end, mid+1, r, 2 * idx + 1)

    def update(self, start, end, l, r, idx):
        if r < start or end < l:
            return

        if start <= l and r <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, 2 * idx)
            self.update(start, end, mid +1, r, 2 * idx +1)
            self.tree.add(idx)

            if 2 * idx in self.lazy and 2 * idx +1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start, end) -> bool:
        if self.query(start, end -1, 0, 10 ** 9, 1):
            return False
        self.update(start, end -1, 0, 10 ** 9, 1)
        return True




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)