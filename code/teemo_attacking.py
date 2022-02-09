# 提莫攻击
# 在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄。
# 他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。
#
# 当提莫攻击艾希，艾希的中毒状态正好持续duration 秒。
#
# 正式地讲，提莫在 t 发起发起攻击意味着艾希在时间区间 [t, t + duration - 1]（含 t 和 t + duration - 1）处于中毒状态。
# 如果提莫在中毒影响结束 前 再次攻击，中毒状态计时器将会 重置 ，
# 在新的攻击之后，中毒影响将会在 duration 秒后结束。
#
# 给你一个 非递减 的整数数组 timeSeries ，
# 其中 timeSeries[i] 表示提莫在 timeSeries[i] 秒时对艾希发起攻击，
# 以及一个表示中毒持续时间的整数 duration 。
#
# 返回艾希处于中毒状态的 总 秒数。
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_duration = 0
        prev_start = timeSeries[0]

        for time in timeSeries[1:]:
            prev_end = prev_start + duration -1

            if prev_end < time:
                total_duration += duration
            else:
                total_duration += (time - prev_start)

            prev_start = time

        total_duration += duration

        return total_duration

    # 官方的思路还是要再简洁一点，直接求出这次中毒的过期时间，拿过期时间和下次中毒开始时间比
    def offical(self, timeSeries: List[int], duration: int) -> int:
        ans, expired = 0, 0
        for time in timeSeries:
            if time >= expired:
                ans += duration
            else:
                ans += time + duration - expired

            expired = time + duration

        return ans

a = Solution().findPoisonedDuration(timeSeries = [1,4,5], duration = 5)
print(a)