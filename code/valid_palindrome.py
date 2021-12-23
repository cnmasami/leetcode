# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            # 这里不能写成while循环，就这样老老实实的写吧，
            # 因为如果“，。”这样，不会执行上面大的while前提，会导致left超出索引范围
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            left_val = s[left]
            right_val = s[right]

            if left_val.lower() != right_val.lower():
                return False

            left += 1
            right -= 1

        return True

a = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(a)


# 其他的速度很快的解法，要不就是遍历字符串，把数字或者字母放入list，然后反转list比较
# 这个也是一样，只是上面放入list的过程不一样，上面是for循环，这个用的是''.join(filter(str.isalnum, s))
