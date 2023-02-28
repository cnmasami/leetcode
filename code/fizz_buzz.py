# fizz buzz
# 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，
# 并用字符串数组 answer（下标从 1 开始）返回结果，其中：
# answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
# answer[i] == "Fizz" 如果 i 是 3 的倍数。
# answer[i] == "Buzz" 如果 i 是 5 的倍数。
# answer[i] == i （以字符串形式）如果上述条件全不满足。
#
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))

        return ans

    def fizzBuzz2(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n+1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            if not s:
                s = str(i)
            a.append(s)

        return ans

    # 素数筛
    def fizzBuzz3(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            ans[i] = str(i+1)

        for i in range(3, n, 3):
            ans[i-1] = 'Fizz'

        for i in range(5, n, 5):
            ans[i -1] = 'Buzz'

        for i in range(15, n, 15):
            ans[i-1] = 'FizzBuzz'

        return ans





a = Solution().fizzBuzz(15)
print(a)