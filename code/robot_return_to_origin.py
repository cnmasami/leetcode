# 机器人能否返回原点

# 在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在(0, 0) 处结束。
#
# 移动顺序由字符串moves表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有R（右），L（左），U（上）和 D（下）。
#
# 如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
#
# 注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = collections.Counter(moves)

        return counter['U'] == counter['D'] and counter['L'] == counter['R']


a = Solution().judgeCircle('LL')
print(a)