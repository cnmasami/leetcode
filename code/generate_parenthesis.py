# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
import collections
import random
from functools import lru_cache
from typing import List


class Solution:
    def generate(self, n):
        # 之前的思路是这样的，在s里找位置插入，但是不知道怎么确定次数，在答案里看到了别人的解法,使用递归。。。只需要再想深一步。。
        # s = '()'
        # s_len = 2*n
        #
        # res = []
        #
        # # while len(s) < s_len:
        # #     for i in range(len(s)):
        # # while len(s) < s_len:
        # for i in range(len(s)):
        #     s = s[:i] + '()' + s[i:]
        #     print(s)
        #
        # res.append(s)
        #
        # return res

        # 别人差不多思路的解法
        if n == 1:
            return ['()']

        res = set()

        for i in self.generate(n-1):
            for j in range(len(i) + 2):
                res.add(i[:j] + '()' + i[j:])

        return list(res)


    # 这个解法不对，看官方的解法吧
    def generateParenthesis(self, n: int) -> List[str]:
        # 一共的可能性有：
        possible = pow(2, 2*n)

        res = []

        while possible:
            whole = ['('] * n + [')'] * n
            s = ''

            while whole:
                # 这种解法不对，虽然是从whole里随机选择，但是在尝试2的2n平方次之和不一定能枚举出所有可能，
                # 导致每次运行得到的结果可能不一样。
                a = random.choice(whole)
                s = s + a
                whole.remove(a)
                # print('after remove', whole)

                counter = collections.Counter(whole)

                if counter['('] > counter[')']:
                    break

                # print(s)

            if not whole and s not in res:
                res.append(s)

            possible -= 1

        return res


    # 解法一：暴力法
    def offical(self, n: int):
        # 使用递归，长度为n的序列就是在长度为n-1的序列前加一个）或者（
        # 为了检查序列是否有效，使用变量blance来表示左括号的数量减去右括号的数量
        # 如果在遍历的过程中，blance的值小于0，后者结束时，balance的值不为0，那么改序列就是无效的，否则有效
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else:bal -= 1

                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans

    # 回溯法
    # 只在序列仍然有效时才添加‘）’或者‘（’，而不是像方法一那样每次添加，
    # 通过跟踪到目前放置的左括号或者右括号的数目来做到这一点
    # 如果左括号的数量不大于n，可以放一个左括号，如果右括号的数量小于左括号的数量，可以放一个右括号
    def offical2(self, n:int):
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2*n:
                ans.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(s, left+1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s, left, right+1)
                s.pop()

        backtrack([], 0, 0)
        return ans

    @lru_cache(None)
    def offical3(self, n:int):
        if n == 0:
            return ['']
        ans = []

        for c in range(n):
            for left in self.offical3(c):
                for right in self.offical3(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


# 别人的范例题解
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtracking(n, result, 0, 0, "")
        return result

    def backtracking(self, n, result, left, right, s):
        if right > left:
            return
        if (left == n and right == n):
            result.append(s)
            return
        if left < n:
            self.backtracking(n, result, left + 1, right, s + "(")
        if right < left:
            self.backtracking(n, result, left, right + 1, s + ")")


# a = Solution().offical(3)
a = Solution().generate(3)
print(a)


