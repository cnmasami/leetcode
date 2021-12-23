# 请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
#
# 函数myAtoi(string s) 的算法如下：
#
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−231, 231− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231− 1 的整数应该被固定为 231 − 1 。
# 返回整数作为最终结果。
# 注意：
#
# 本题中的空白字符只包括空格字符 ' ' 。
# 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = {"+": 1, "-": -1}
        s = s.strip()
        ans_list = []
        if s[0] in sign or s[0].isdigit():
            ans_list.append(s[0])
        else:
            return 0

        for sub_s in s[1:]:
            if sub_s.isdigit():
                ans_list.append(sub_s)
            else:
                break

        if len(ans_list) > 1:
            if ans_list[0] in sign:
                res_num = sign[ans_list[0]] * int(''.join(ans_list[1:]))
            else:
                res_num = int(''.join(ans_list))
        else:
            if ans_list[0].isdigit():
                return int(ans_list[0])
            else:
                return 0

        if res_num < pow(-2, 31):
            return pow(-1, 31)
        elif res_num > (pow(2, 31) -1):
            return pow(2, 31) -1
        else:
            return res_num



# 官方题解 自动机
# 程序在每个时刻有一个状态S，每次从序列中输入一个字符c，并根据字符c转移到下一个状态s‘,
# 这样，只需要建立一个覆盖所有情况的从s与c映射到s'的表格即可解决题目中的问题

# 状态s： start， signed， in_number, end
# 字符c： ’‘， +/c,  number, other

# 另外自动机也需要记录当前已经输入的数字，只要在s'为in_number时，更新输入的数字，即可得到最终输入的数字
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans*10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution2():
    def myAtoi(self, str:str) -> int:
        automaton = Automaton()

        for c in str:
            automaton.get(c)

        return automaton.sign * automaton.ans


a = Solution().myAtoi("+-1")
print(a)