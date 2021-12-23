# 给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
#
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符串转换为整数形式。

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_count = len(num1) - 1
        num2_count = len(num2) - 1

        sum = ''
        holder = 0

        while num1_count >= 0 or num2_count >= 0:
            num1_value = int(num1[num1_count]) if num1_count >= 0 else 0
            num2_value = int(num2[num2_count]) if num2_count >= 0 else 0

            holder, answer = divmod((num1_value + num2_value + holder), 10)

            sum = str(answer) + sum

            if holder == 0 and num2_count < 0:
                return num1[:num1_count] + sum
            elif holder == 0 and num1_count < 0:
                return num2[:num2_count] + sum

            num1_count -= 1
            num2_count -= 1

        if holder:
            sum = '1' + sum

        return sum

a = Solution().addStrings('1', '9')
print(a)

