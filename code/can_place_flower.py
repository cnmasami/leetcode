# 种花问题
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。
# 可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#
# 给你一个整数数组flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，
# 1 表示种植了花。另有一个数n ，能否在不打破种植规则的情况下种入n朵花？能则返回 true ，不能则返回 false
#
from typing import List


class Solution:
    # 这个解法不行
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        real_n = 0

        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 0:
        #         return True
        #     else:
        #         return False

        for idx, flower in enumerate(flowerbed):
            if flower == 0:
                if idx == 0:
                    if flowerbed[idx + 1] == 1:
                        continue
                elif idx == len(flowerbed) -1:
                    if flowerbed[idx -1] == 1:
                        continue
                elif flowerbed[idx -1] == 1 or flowerbed[idx+1] == 1:
                    continue

                real_n += 1
                flowerbed[idx] = 1

        if real_n >= n:
            return True
        else:
            return False

    # 贪心
    # 能否在不打破种植规则的情况下在花坛内种入n朵花，从贪心的角度考虑，应该在不打破种植规则的情况下
    # 种入尽可能多的花，然后判断可以种入的花的最多数量是否大于或等于n
    # 假设i和j都种了花，并且j-i>=2,并且在[i+1,j-1]范围内没有种花，则，只有当j-i>=4的时候
    # 才可以在i和j之间种更多的花，且可以种花的下标范围是[i+2, j-2].
    # 可以种花的位置数p是j-i-3，
    # 当p是奇数时最多可以在该范围内种 (p+1)/2朵花
    # 当p时偶数时最多可以种p/2朵花。p是偶数的时候，p/2 和 (p+1)/2相等
    # 因此无论p是奇数还是偶数，都是最多种(p+1)/2朵花，即最多种(j-i-2)/朵花
    # 上面的情况是在已有两朵花中间种花的情况，假设l是最左边已经种的花，r是最右边已经中的花
    # l左边有l个位置，当l<2时无法在l左边种花，当l>=2时在0，l-2范围内可以种花，
    # 可以种花的位置数时l-1，最多种l/2朵
    # 假设数组长度m，同样右侧可以种(m-r-1)/2朵
    # 如果花坛没有任何花，最多可种(m+1)/2朵
    # 所以：
    # 维护prev表示赏一朵已经种花的位置，初始prev=-1，表示还未遇到花
    # 从左往右遍历数组，遇到flower【i】==1时，根据prev和i的值计算上一个区间内可以种花的数量
    # 然后令prev=i，继续遍历剩余元素
    # 遍历数组结束，根据prev和长度m的值计算最后一个区间内可以种花的数量
    # 判断是否大于等于n
    def offical(self, flowerbed: List[int], n: int) -> bool:
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev <0:
                    count += i // 2
                else:
                    count += (i - prev -2) // 2

                if count >=n:
                    return True

                prev = i

        if prev < 0 :
            count += (m+1)//2
        else:
            count += (m - prev - 1) // 2

        return count >= n

    # 题解区看到的别人的题解
    # 当遍历到1的时候，说明有花，必然从index+2才可能有花，因此碰到1直接跳过下一格
    # 当遇到0的时候，由于1时挑两格，因此前一格必定是0，只需要判断下一格是不是1即可得到这一格能不能种花
    # 如果能种，n-1，然后这个位置按照1处理，挑两格，
    # 如果下一格是1，说明这个位置不能种，之后两格也不能种，直接跳过3格
    # 当n减为0，返回True，否则到遍历结束，都没有减到0，返回false
    def otherMethod(self, flowerbed: List[int], n: int) -> bool:
        i,m = 0, len(flowerbed)

        while i < m:
            if flowerbed[i] == 1:
                i += 2
            elif i == m -1 or flowerbed[i+1] == 0:
                n -=1
                i += 2
            else:
                i += 3

        return n <= 0

    # 我的情况就是没有考虑特殊情况和边界判断太复杂了，这个直接在边界加了两个值，解决了边界判断的问题，一下就简化了好多
    # 记得之前做链表类题目的时候也有类似的，为了不对边界特殊处理，加了dummpy节点
    def ootherMethod(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) -1):
            if flowerbed[i] == 0 and flowerbed[i -1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1

            if count >= n:
                return True

        return False


a = Solution().canPlaceFlowers([0], 1)
print(a)