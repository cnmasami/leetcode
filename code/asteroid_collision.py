# 给定一个整数数组 asteroids，表示在同一行的行星。
#
# 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。
# 每一颗行星以相同的速度移动。
#
# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
# 如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
from typing import List


class Solution:
    # 左 负数
    # 右 正数
    # 只有左边是正数， 右边是负数的情况会发生碰撞
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for asteroid in asteroids:
            if asteroid < 0:

                while True:
                    if not ans :
                        ans.append(asteroid)
                        break
                    else:
                        prev = ans.pop()
                        if prev < 0:
                            ans.append(prev)
                            ans.append(asteroid)
                            break
                        elif prev + asteroid == 0:
                            break
                        elif prev > abs(asteroid):
                            ans.append(prev)
                            break
                        elif prev < abs(asteroid):
                            continue

            else:
                ans.append(asteroid)

        return ans

    # 还是思路一样，官方题解的代码要简洁很多
    def offical(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)

        return ans



a = Solution().asteroidCollision([5,10,-5])
print(a)




