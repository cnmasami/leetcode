# 检查句子中的数字是否递增

# 句子是由若干 token 组成的一个列表， token 间用 单个 空格分隔，
# 句子没有前导或尾随空格。每个 token 要么是一个由数字 0-9 组成的不含前导零的 正整数，
# 要么是一个由小写英文字母组成的 单词 。
#
# 示例，"a puppy has 2 eyes 4 legs" 是一个由 7 个 token 组成的句子："2" 和 "4" 是数字，
# 其他像"puppy" 这样的 tokens 属于单词。
# 给你一个表示句子的字符串 s ，你需要检查 s 中的 全部 数字是否从左到右严格递增
# （即，除了最后一个数字，s 中的 每个 数字都严格小于它 右侧 的数字）。
#
# 如果满足题目要求，返回 true，否则，返回 false 。
#
import itertools


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')
        prev = float('-inf')

        for token in s:
            if token.isdigit():
                if int(token) <= prev:
                    return False
                prev = int(token)
            else:
                continue

        return True

    def areNumberAscending2(self, s: str) -> bool:
        # itertools.pairwise 用来获取连续的重叠对 比如[1,2,3,4] 则输出12 23 34
        # map()两个参数 第一个参数为函数 第二个参数为序列 针对序列每个元素调用函数 返回新列表
        # int.__call__(x)  等同于int(x)
        # filter() 第一个参数为判断函数，第二个参数为可迭代对象，用来过滤掉不符合条件的元素，返回一个列表
        return all(
            a < b for a, b in itertools.pairwise(
                map(
                    int.__call__,
                    filter(
                        str.isdigit,
                        s.split()
                    )
                )
            )
        )


a = Solution().areNumbersAscending('hello world 5 x 5')
print(a)