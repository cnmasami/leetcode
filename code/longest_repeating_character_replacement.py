# 替换后的最长重复字符

# 给你一个字符串 s 和一个整数 k 。
# 你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。
# 该操作最多可执行 k 次。
# 在执行上述操作后，返回包含相同字母的最长子字符串的长度。
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counter = collections.Counter()
        max_count = 0

        while right < len(s):
            counter[s[right]] += 1
            # 计算出这个子串中替换掉的字符数量
            while right - left + 1 - counter.most_common(1)[0][1] > k:
                counter[s[left]] -= 1
                left += 1

            max_count = max(max_count, right - left + 1)
            right += 1

        return max_count

    #  right - left在整个过程是非递减的。
    #  只要right 的值加进去不满足条件，left和right就一起右滑，
    #  因为长度小于right - left的区间就没必要考虑了，所以right - left一直保持为当前的最大值
    # 如果k够用来替换的话，right右移1步，窗口变大（当前维护的最大值变大，不消耗k；当前维护的最大值不变，将消耗k）；
    # 如果k不够用来替换的话，left和right都右移一步，窗口不变（我们已经不关心比当前小的情况了）。
    # 从这个角度来说，也不难理解最后答案是right-left（最后窗口的大小，可扩充的最大窗口）。
    def characterReplacement2(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord('A')] += 1
            maxn = max(maxn, num[ord(s[right]) - ord('A')])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord('A')] -= 1
                left += 1

            right += 1

        return left - right
    

a = Solution().characterReplacement('AABABBA', 2)
print(a)

