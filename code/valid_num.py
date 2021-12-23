# 有效数字（按顺序）可以分成以下几个部分：
#
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 小数（按顺序）可以分成以下几个部分：
#
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：
#
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 部分有效数字列举如下：
#
# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 部分无效数字列举如下：
#
# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
# =====================这个状态是错误的===========================
# 这题使用自动机
# 自动机的本质就是状态和输入
# 状态\输入  ’‘                   +/-     .      e
# 开始      开始                  符号     小数   结束
# 符号      错误                  结束     小数   结束
# 整数      正确（return true）    结束     小数   小数
# 小数      正确（return true）    结束     结束   小数
# 结束      结束                  结束     结束
# ==============================================================

# 自动机在计算机科学领域有着广泛的应用。在算法领域，它与大名鼎鼎的字符串查找算法「KMP 算法」有着密切的关联；在工程领域，它是实现「正则表达式」的基础。
# 符号位，即 ++、-− 两种符号
# 整数部分，即由若干字符 0-90−9 组成的字符串
# 小数点
# 小数部分，其构成与整数部分相同
# 指数部分，其中包含开头的字符 \text{e}e（大写小写均可）、可选的符号位，和整数部分
#

# 用当前处理到字符串的哪个部分当作状态的表达。
# 0 初始状态
# 1 符号位
# 2 整数部分
# 3 左侧有整数的小数点
# 4 左侧无整数的小数点
# 5 小数部分
# 6 字符e
# 7 指数部分的符号位
# 8 指数部分的整数部分

# 初始状态0
# 接受状态2， 3， 5， 8换言之，字符串的末尾要么是空格，要么是数字，要么是小数点，但前提是小数点的前面有数字



class AutoMaton():
    def __init__(self):
        self.state = 'start'
        self.table = {
            'start': ['sign', 'int', 'point_without_int', False, False],
            'signed': [False, 'int', 'point_without_int', False, False],
            'int': [False, 'int', 'point', 'exp', False],
            'point': [False, 'fraction', False, 'exp', False],
            'point_without_int':[False, 'fraction', False, False, False],
            'fraction': [False, 'fraction', False, 'exp', False],
            'exp': ['exp_sign', 'exp_num', False, False, False],
            'exp_sign':[False, 'exp_num', False, False, False],
            'exp_num':[False, 'exp_num', False, False, False]
        }

    def get_col(self,c):
        if c == '+' or c == '-':
            return 0
        elif c.isdigit():
            return 1
        elif c == '.':
            return 2
        elif c == 'e' or c == 'E':
            return 3
        else:
            return 4

    def get(self, c):
        state_index = self.get_col(c)
        self.state = self.table[self.state][state_index]
        # if self.state is True:
        #     return True
        # elif self.state is False:
        #     return False

        return self.state


class Solution():
    def myAtoi(self, str:str) -> int:
        automaton = AutoMaton()
        is_num = ['int', 'point', 'fraction', 'exp_num']

        for c in str:
            state = automaton.get(c)
            if state is False:
                return False

        if state in is_num:
            return True
        else:
            return False


# 官方题解
from enum import Enum


class Solution2():
    def isNumber(self, s:str) -> bool:
        State = Enum("State",[
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])

        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == '-':
                return Chartype.CHAR_SIGN
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN:{
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER:{
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
        }



a = Solution().myAtoi('53.5e93')
print(a)


