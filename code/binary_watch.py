# 二进制手表顶部有4个led代表小时0-11，底部的6个led代表分钟0-59，每个led代表一个0或者1，最低位在右侧
# 给你一个整数 turned on，表示当前亮着的led的数量，返回二进制手表可以表示的所有可能时间，
# 可以按任意顺序返回答案，
# 小时不会以0开头
# 分钟必须由两位数组成，可能会以零开头
from typing import List


class Solution:
    # 枚举  枚举小时的所有可能值以及分钟的所有可能值，并计算二者中的二进制中1的个数之和
    # 若为turned on，则将其加入到答案中
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    ans.append(f'{h}:{m:02d}')
        return ans

    # 二进制枚举 另一种枚举方法是枚举所有2的10次方=1024种灯的开闭组合，即用一个
    # 二进制数表示等的开闭，其高4位是小时，低6位为分钟
    # 若小时和分钟的值均在合法范围内，且二进制中1的个数为turnedON，ze将其加入到答案
    def otherMethod(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(1024):
            # 用位运算取出高4位和低6位
            h, m = i >> 6, i & 0x3f
            if h < 12 and m < 60 and bin(i).count('1') == turnedOn:
                ans.append(f'{h}:{m:02d}')

        return ans


# 递归回溯
# 由于我们不知道具体n为几，所以用回溯算法。
# 题目中由于限定了顶部的四个代表了0-11小时，底部的0-59代表分钟，所以不用考虑进位问题
# 当有超过这个限制的时候，需要进行剪枝，否则最后的结果就错了

# 递归结构
# r(n)=r(n−1)+w
# w 代表从 nums中选出一个数字。

# 递归边界
# if (n == step)

# 递归参数
# n：亮灯数量
# step：递归层数
# result：单次结果
# result_all：最终结果
# 其他处理
# 分别计算小时和分钟，若超过 0-11和 0-59 ，则进行剪枝，所以需要写一个函数，判断当前合不合理
# 将所有灯组成 nums = [1,2,4,8,1,2,4,8,16,32] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 写一个函数，将 nums 处理成正确的时间

class Soultion2:
    def __init__(self):
        self.result_all = None
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = None

    def readBinaryWatch(self, nums):
        self.result_all = []
        self.visited = [0 for _ in range(len(self.nums))]
        self.dfs(nums, 0, 0)
        return self.result_all

    def dfs(self, num, step, start):
        if step == num:
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start, len(self.nums)):
            self.visited[i] = 0
            if not self.calc_sum(self.visited):
                self.visited[i] = 0
                continue
            self.dfs(num, step + 1, i + 1)
            self.visited[i] = 0
        return

    def calc_sum(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        return 0 <= sum_h <= 11 and 0 <= sum_m <= 59

    def handle_date(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        result = "" + str(sum_h) + ":"
        if sum_m < 10:
            result += "0" + str(sum_m)
        else:
            result += str(sum_m)
        return result



