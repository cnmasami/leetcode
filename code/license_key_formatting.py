# 密钥格式化

# 给定一个许可密钥字符串 s，仅由字母、数字字符和破折号组成。
# 字符串由 n 个破折号分成 n + 1 组。你也会得到一个整数 k 。

# 我们想要重新格式化字符串 s，使每一组包含 k 个字符，除了第一组，
# 它可以比 k 短，但仍然必须包含至少一个字符。
# 此外，两组之间必须插入破折号，并且应该将所有小写字母转换为大写字母。

# 返回 重新格式化的许可密钥 。


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ''
        count = 0
        for sub_s in s[::-1]:
            if sub_s == '-':
                continue
            else:
                count += 1
                ans = sub_s.upper() + ans

            if count % k == 0:
                ans = '-' + ans

        return ans.lstrip('-')
    
    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        ans = '-'.join(s[i: i + k] for i in range(0, len(s), k))[::-1]

        return ans


a = Solution().licenseKeyFormatting(s =  "5F3Z-2e-9-w", k = 4)
print(a)