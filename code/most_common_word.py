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