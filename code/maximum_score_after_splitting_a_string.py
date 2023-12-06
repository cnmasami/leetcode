# 分割字符串的最大得分
# 给你一个由若干 0 和 1 组成的字符串 s ，
# 请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。
#
# 「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。


class Solution:
    def maxScore(self, s: str) -> int:
        # max_count = 0
        #
        # for i in range(1, len(s)):
        #     cur_count = s[:i].count('0') + s[i:].count('1')
        #     max_count = max(max_count, cur_count)
        #
        # return max_count
        return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))

    # 先统计1的个数，然后从左向右遍历，遇到0加一，遇到1减1
    def dy_maxScore(self, s: str) -> int:
        cnt = s.count('1')
        ans = 0
        for c in s[:-1]:
            ans = max(ans, cnt + 1 if c == '0' else cnt -1)

        return ans

    # 前缀和动态规划
    # 很容易想到利用前缀和，分别统计左边0和右边1，然后枚举答案
    # 但是本题字符串只有0和1，那么0和1的个数就是对称的，有多少个0就有多少个1，
    # 两者加起来永远是字符串长度
    # 假设字符串总长度为n，当前位置为i
    # 假如知道总共0的个数final_presum,和当前分割位置左侧0的个数pre_sum
    # 可以计算出右侧1的个数为 (n-i) - (final_presum - pre_sum)
    # 将常量和变量分别抽出来，于是每个位置的得分可以简化为：
    # pre_sum + (n-i) - (final_presum - pre_sum) = pre_sum * 2 - i + (n-final_presum)
    # 只需要找到i，使得presum*2 -i最大即可
    def pre_sum_maxScore(self, s: str) -> int:
        n, presum, ans = len(s), 0, float('-inf')
        for i in range(n):
            if i:
                ans = max(ans, presum * 2 - i)
            presum += s[i] == '0'

        return ans + n - presum


a = Solution().maxScore("010001")
print(a)
