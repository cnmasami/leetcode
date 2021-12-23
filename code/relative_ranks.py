# 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。
#
# 运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：
#
# 名次第 1 的运动员获金牌 "Gold Medal" 。
# 名次第 2 的运动员获银牌 "Silver Medal" 。
# 名次第 3 的运动员获铜牌 "Bronze Medal" 。
# 从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
# 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = list(range(1, len(score)+1))
        answer[:3] = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        # score.sort(reverse=True)
        aaa = sorted(score, reverse=True)
        a = zip(aaa, answer)
        dict_score = {k:v for k, v in a}
        print(dict_score)
        for idx, s in enumerate(score):
            answer[idx] = dict_score[s]

        return answer

# 相对名次，有名次，肯定要排序，然后还要和index结合起来，所以，sort enumerate
class Solution2:
    def findRelativeRanks(self, score: List[int]):
        desc = ("Gold Medal", "Silver Medal", "Bronze Medal")
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        print(arr)
        for i ,(idx, _) in enumerate(arr):
            ans[idx] = i + 1

        return ans

a = Solution().findRelativeRanks([10,3,8,9,4])
print(a)
