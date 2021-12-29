# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        parentheses_list = []

        # 官方题解也是同样的思路，但是代码比较简洁
        # for sub_s in s:
        #     if sub_s in parentheses_dict:
        #         top_ele = parentheses_list.pop() if parentheses_list else '#'
        #
        #         if top_ele != parentheses_dict[sub_s]:
        #             return False
        #     else:
        #         parentheses_list.append(sub_s)
        #
        # return not parentheses_list

        for sub_s in s:
            if sub_s in parentheses_dict:
                if len(parentheses_list) == 0:
                    return False

                if parentheses_list.pop() == parentheses_dict[sub_s]:
                    continue
                else:
                    return False
            else:
                parentheses_list.append(sub_s)

        if not parentheses_list:
            return True
        else:
            return False

    # 官方题解也是栈，在题解评论区看到的别的解法
    def other(self, s: str):
        while '{}' in s or '[]' in s or '()' in s:
            if '{}' in s:
                s = s.replace('{}', '')
            if '()' in s:
                s = s.replace('()', '')
            if '[]' in s:
                s = s.replace('[]', '')

        return not s

a = Solution().isValid("{[]}]")
print(a)