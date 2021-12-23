# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

class Solution:
    def singleMultiply(self, num_val, num2, num2_idx):
        sum = 0
        for idx in range(num2_idx, -1, -1):
            sum += (int(num2[idx]) * int(num_val) * pow(10, (num2_idx - idx)))

        return sum


    def multiply(self, num1: str, num2: str) -> str:
        num1_idx = len(num1) - 1
        num2_idx = len(num2) - 1

        res = 0

        for idx in range(num1_idx, -1, -1):
            res += (pow(10, (num1_idx - idx)) * self.singleMultiply(num1[idx], num2, num2_idx))

        return str(res)


class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        nums = [0 for _ in range(len1 + len2)]

        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                nums[i + j + 1] += digit1 * digit2

        for i in range(len1 + len2 - 1, 0, -1):
            nums[i - 1] += nums[i] // 10
            nums[i] %= 10

        if nums[0] == 0:
            ans = "".join(str(digit) for digit in nums[1:])
        else:
            ans = "".join(str(digit) for digit in nums[:])
        return ans


a = Solution2().multiply("125", "23")
print(a)