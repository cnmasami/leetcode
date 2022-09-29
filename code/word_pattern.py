# 单词规律
# 给定一种规律pattern和一个字符串s，判断s是否遵循相同的规律
# 这里的遵循指完全匹配，例如，pattern里的每个字母和字符串s中的每个非空单词之间存在着双向连接的对应规律


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        p2s = {}
        s2p = {}

        for idx, pat in enumerate(pattern):
            if pat in p2s and p2s[pat] != s_list[idx]:
                return False
            elif pat not in p2s:
                p2s[pat] = s_list[idx]
            if s_list[idx] in s2p and s2p[s_list[idx]] != pat:
                return False
            elif s_list[idx] not in s2p:
                s2p[s_list[idx]] = pat

        # 上面这段代码更简洁写法
        # for ch, word in zip(pattern, s_list):
        #     if (word in s2p and s2p[word] != ch) or (ch in p2s and p2s[ch] != word):
        #         return False
        #     s2p[word] = ch
        #     p2s[ch] = word

        return True

a = Solution().wordPattern("abba","dog cat cat dog")
print(True)
