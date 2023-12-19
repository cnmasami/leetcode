#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 面试题 17.15. 最长单词

# 给定一组单词words，编写一个程序，找出其中的最长单词，
# 且该单词由这组单词中的其他单词组合而成。
# 若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。


from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            print(node.children)
            node = node.children[ch]
            print(node)

        node.isEnd = True

    def check(self, word):
        if word == '': return True
        node = self
        for i, ch in enumerate(word):
            if ch not in node.children:
                return False

            node = node.children[ch]
            if node.isEnd and self.check(word[i+1:]):
                return True

        return False


class Solution:
    # 字典树
    def longestWord(self, words: List[str]) -> str:
        # sorted_words = sorted(words, key=lambda x: (-len(x), x))
        #
        # for idx, word in enumerate(sorted_words):
        #     for other_word in sorted_words[idx + 1:]:
        #         print(word.replace(other_word, ''))
        #         if word.lstrip(other_word) in sorted_words[idx + 1:]:
        #             return word
        #
        # return ''
        trie = Trie()
        words.sort(key=lambda x:(len(x), x))
        ans = ''

        for word in words:
            if not word: continue
            if trie.check(word):
                if len(word) > len(ans):
                    ans = word
            else:
                trie.insert(word)

        return ans

    def dfs_longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x))

        def dfs(w, words):
            if not w: return True
            for i, nxt in enumerate(words):
                if nxt == w[:len(nxt)]:
                    if dfs(w[len(nxt):], words):
                        return True

            return False

        for i, word in enumerate(words):
            if dfs(word, words[i+1:]):
                return word

        return ''


a = Solution().longestWord(["cat","banana","dog","nana","walk","walker","dogwalker"])
print(a)




