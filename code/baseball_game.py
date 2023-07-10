# 棒球比赛

# 你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。
#
# 比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：
#
# 整数 x - 表示本回合新获得分数 x
# "+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
# "D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
# "C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
# 请你返回记录中所有得分的总和。
#
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        real_point = []
        for op in operations:
            if op.isdigit() or op.startswith('-'):
                real_point.append(int(op))
            elif op == 'C':
                real_point.pop()
            elif op == 'D':
                real_point.append(2 * real_point[-1])
            elif op == '+':
                real_point.append(sum(real_point[-2:]))

        return sum(real_point)

    # python 3.10语法
    def calPoints2(self, ops: List[str]) -> int:
        stk = []
        for op in ops:
            match op:
                case 'C':
                    stk.pop()
                case 'D':
                    stk.append(stk[-1] * 2)
                case '+':
                    stk.append(stk[-1] + stk[-2])
                case _:
                    stk.append(int(op))
        return sum(stk)


a = Solution().calPoints(["5", "-2", "4", "C", "D","9", "+","+"])
print(a)