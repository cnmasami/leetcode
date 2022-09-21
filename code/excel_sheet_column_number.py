# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for idx, title in enumerate(columnTitle[::-1]):
            ans += (ord(title) - 64) * 26 ** idx

        return ans


a = Solution().titleToNumber('ZY')
print(a)

