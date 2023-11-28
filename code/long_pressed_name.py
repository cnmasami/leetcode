# 长按键入
# 你的朋友正在使用键盘输入他的名字name。
# 偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1次或多次。
#
# 你将会检查键盘输入的字符typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j and typed[j] == typed[j -1]:
                j += 1
            else:
                return False

        if i < len(name):
            return False

        while j < len(typed):
            if typed[j] == typed[j-1]:
                j += 1
            else:
                return False

        return True


a = Solution().isLongPressedName('alex', 'aaleexa')
print(a)
