# 字符串中的第一个唯一字符

# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。
# 如果不存在，则返回 -1 。
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = collections.Counter(s)
        for idx, c in enumerate(s):
            if s_counter[c] == 1:
                return idx

        return -1

    def firstUniqChar2(self, s: str) -> int:
        position = dict()
        n = len(s)
        for i, c in enumerate(s):
            if c in position:
                position[c] = -1
            else:
                position[c] = i

        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos

        if first == n:
            first = -1

        return first
    
    def firstUniqChar3(self, s: str) -> int:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((ch, i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()

        return -1 if not q else q[0][1]


a = Solution().firstUniqChar('aabb')
print(a)

