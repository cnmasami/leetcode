# 根据字符出现频率排序

# 给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。
# 一个字符出现的 频率 是它出现在字符串中的次数。
#
# 返回 已排序的字符串。如果有多个答案，返回其中任何一个。
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        s = collections.Counter(s)
        sorted_s = sorted(s.items(), key=lambda x: x[1], reverse=True)

        ans = ''
        for ch, count in sorted_s:
            ans += ch * count

        return ans


a = Solution().frequencySort("Aabb")
print(a)