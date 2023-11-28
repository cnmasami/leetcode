# 最常见的单词
# 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。
#
# 题目保证至少有一个词不在禁用列表中，而且答案唯一。
#
# 禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。


import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para_dict = collections.defaultdict(int)

        word = ''
        for char in paragraph:
            if char.isalpha():
                word += char.lower()
            else:
                if word and word not in banned:
                    para_dict[word] += 1
                word = ''

        if word:
            para_dict[word] += 1

        para_dict = dict(sorted(para_dict.items(), key=lambda x: x[1], reverse=True))

        for word in para_dict.keys():
            if word not in banned:
                return word

    def mostCommandWord(self, paragraph: str, banned: List[str]) -> str:
        return collections.Counter(
            word.lower()
            for word in re.split(r'[^\w]+', paragraph)
            if word
            and word.lower() not in banned
        ).most_common(1)[0][0]


a = Solution().mostCommonWord("Bob", ["hit"])
print(a)