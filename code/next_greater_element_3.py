# 下一个更大元素 III

# 给你一个正整数n ，请你找出符合条件的最小整数，其由重新排列 n中存在的每位数字组成，
# 并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
#
# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
#


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = []
        tmp = []

        while n:
            n, mod = divmod(n, 10)
            # 当当前元素小于栈顶元素
            if stack and mod < stack[-1]:
                # 先弹出栈顶元素
                # 如果当前值比栈顶元素小，并且栈顶元素依旧有值
                while stack and mod < stack[-1]:
                    top = stack.pop()
                    tmp.append(top)

                ans = n
                # 如果stack里还有值，说明栈顶元素比当前元素小，tmp里的元素都比当前元素大
                if tmp:
                    ans = n * 10 + tmp.pop()

                while stack:
                    tmp.append(stack.pop())

                while tmp and tmp[-1] < mod:
                    ans = ans * 10 + tmp.pop()

                ans = ans * 10 + mod

                while tmp:
                    ans = ans * 10 + tmp.pop()

                return ans if ans < 2 ** 31 else -1
            # 大于栈顶的元素，将元素入栈，保持栈顶元素最小
            elif stack and mod > stack[-1]:
                stack.append(mod)
            else:
                stack.append(mod)

        return -1

    # 官方解法 下一个排列，同样的思路，但是不用在栈里倒来倒去
    def nextGreaterElement2(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2
        while i > 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            return -1

        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i+1:][::-1]
        ans = int(''.join(nums))

        return ans if ans < 2 ** 31 else -1

    # 还是同样的思路，数学方法，o(1)复杂度
    # 不断比较其最低位数字和次低位数字的大小，
    # 如果次低位数字不低于最低位数字，则移除最低位数字，不断循环
    # 循环结束后的n，就是nums的前i+1个不用处理的字符
    def nextGreaterElement3(self, n: int) -> int:
        x, cnt = n, 1
        while x >= 10 and x // 10 % 10 >= x % 10:
            cnt += 1
            x //= 10
        x //= 10
        if x == 0:
            return -1

        targetDigit = x % 10
        x2, cnt2 = n, 0
        while x2 % 10 <= targetDigit:
            cnt2 += 1
            x2 //= 10
        x += x2 % 10 - targetDigit

        MAXINT = 2 ** 31 -1
        for i in range(cnt):
            d = n % 10 if i != cnt2 else targetDigit

            if x > MAXINT // 10 or x == MAXINT // 10 and d > 7:
                return -1
            x = x * 10 + d
            n //= 10

        return x


a = Solution().nextGreaterElement3(2147483486)
print(a)


