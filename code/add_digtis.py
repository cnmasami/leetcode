# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        res = 0

        while num:
            num, remainder = divmod(num, 10)
            res += remainder

        while res >= 10:
            res = self.addDigits(res)

        return res

    # 官方解法 模拟
    def offical(self, num):
        while num >= 10:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum

        return num

    # num 有一个数学公式xxxx，Σai * 10的i次方=Σai * (10的i次方 -1 +1) = Σai *（10的i次方 -1） + Σai
    # 当i=0时，10的i次方-1是9的倍数，
    # 当i是正整数时，10的i次方-1是由i位9组成的整数，也是9的倍数
    # 因此对于任意非负数i，10的i次方-1都是9的倍数
    # 由此可得num与其各位相加的结果模9同余。
    # 重复计算各位相加的结果直到结果为一位数时，该一位数即为num的树根，num与其树根模9同余

    # 所以，num不是9的倍数时，其树根即为num除以9的余数
    # num是9的倍数时： 如果num=0，则树根是0
    # 如果num > 0, 则各位相加的结果大于0，其根数也大于0，因此其树根是9

    # 根据上述分析，当num>0时，其树根的结果在范围1-9内
    # 因此可以想到计算num-1 除以9的余数然后加1
    # 由于当num>0时，num -1 >= 0,非负数除以9的余数一定也是非负数
    # 因此计算num -1 除以9的余数然后加1的结果是正确的

    # 通俗来说
    # 数字：xyz=100*x+10*y+z=99*x+x+9*y+z=(99*x+9*y)+(x+y+z)，
    # 也就是说xyz和（x+y+z）对于9来说是同模的,即xyz%9=（x+y+z）%9，
    # 这里假设（x+y+z）=ab，同理（ab%9=(a+b)%9），可以一直递归下去直到一位数字，
    # 也就是说我们可以得到模9的结果，但是我们需要的是模10的结果，
    # num%10=((num-1)%9+1)%10=(num-1)%9+1,这里需要注意的是，1<=num<=9，然后写代码即可

    # 数学上提到：
    # 能够被9整除的整数，各位上的数字加起来也必然能被9整除，所以，连续累加起来，最终必然就是9。
    # 不能被9整除的整数，各位上的数字加起来，结果对9取模，和初始数对9取摸，是一样的，所以，连续累加起来，最终必然就是初始数对9取摸。
    def mathematical(self, num):
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9

        return num % 9


a = Solution().addDigits(999)
print(a)
