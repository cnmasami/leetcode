# 罗马数字包含以下七种字符：I，V，X，L，C，D和M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：
#
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
# 给你一个整数，将其转为罗马数字。

class Solution:
    def intToRoman(self, num: int):
        roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        num_list = []

        while num:
            num, remainder = divmod(num, 10)
            num_list.append(remainder)

        reman_str = ''

        for i, sub_num in enumerate(num_list):
            if sub_num in roman_dict:
                reman_str = roman_dict[sub_num * (10 ** i)] + reman_str
            else:
                if sub_num < 4:
                    reman_str = sub_num * roman_dict[1 * (10 ** i)] + reman_str
                else:
                    reman_str = roman_dict[5 * (10 ** i)] + (sub_num - 5) * roman_dict[1 * (10 ** i)] + reman_str

        return reman_str

    def offical_sim(self, num):
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman = []

        for value, symbol in VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)

            if num == 0:
                break

        return ''.join(roman)


# 还有一种，硬编码，比我自己写的还离谱，就是列出每一种可能性在字典里，然后直接从字典取值去拼结果


a = Solution().intToRoman(3)
print(a)
