# 电话号码的字母组合
# 给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return alpha_dict[digits]

        res = []

        for alpha in self.letterCombinations(digits[:-1]):
            for digit_alpha in alpha_dict[digits[-1]]:
                ans = alpha + digit_alpha
                res.append(ans)

        return res

    # 官方解法 回溯
    def offical(self, digits: str) -> List[str]:
        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append(''.join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = []
        combinations = []
        backtrack(0)
        return combinations


# a = Solution().letterCombinations('2345')
a = Solution().offical('234')
print(a)




