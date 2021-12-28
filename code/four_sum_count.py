# 四数相加2
# 给你四个整数数组nums1, nums2, nums3, nums4 数组长度都是n，请你计算有多少个元组(i,j,k,l)能满足
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
import collections
from typing import List


class Solution:
    # 使用了三数之和的解法思路，其实就是暴力穷举，结果超时
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # i = j = k = l = 0

        nums1.sort()
        nums2.sort()
        nums3.sort()
        nums4.sort()

        # res = []
        res = 0

        for i in range(len(nums1)):
            # 最小的数字加起来大于0， break
            if nums1[i] + nums2[0] + nums3[0] + nums4[0] > 0:
                break
            # 最大的数字加起来小于0，continue
            if nums1[i] + nums2[-1] + nums3[-1] + nums4[-1] < 0:
                continue
            for j in range(len(nums2)):
                # 最小的数字加起来大于0， break
                if nums1[i] + nums2[j] + nums3[0] + nums4[0] > 0:
                    break
                # 最大的数字加起来小于0，continue
                if nums1[i] + nums2[j] + nums3[-1] + nums4[-1] < 0:
                    continue
                for k in range(len(nums3)):
                    # 最小的数字加起来大于0， break
                    if nums1[i] + nums2[j] + nums3[k] + nums4[0] > 0:
                        break
                    # 最大的数字加起来小于0，continue
                    if nums1[i] + nums2[j] + nums3[k] + nums4[-1] < 0:
                        continue
                    for l in range(len(nums4)):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] > 0:
                            break
                        elif nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            # if [i,j,k,l] not in res:
                            #     res.append([nums1[i] , nums2[j] , nums3[k] , nums4[l]])
                            res += 1


        return res

    # 官方题解把数组分成两部分分别计算，前两个数组为一组，后两个数组为一组
    # 先遍历前两个数组，求和存入字典，对应的键值是这个和出现的次数
    # 然后遍历后两个数组，看后两个数组的和取反在不在字典中，如果在，将字典对应的键值累加到答案中
    def offical(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]):
        countAB = collections.Counter(u+v for u in nums1 for v in nums2)

        ans = 0

        for u in nums3:
            for v in nums4:
                if -u-v in countAB:
                    ans += countAB[-u-v]

        return ans


# 看了通过的范例，基本上都是使用分组+哈希的思路
# 但是官方题解的解答速度还是比较慢的，看了官方统计里给出的运行效率比较高的范例
# 高一点的使用collections.defaultdict(int)做哈希表存储，第一组两层for循环的时候直接在defaultdict上进行累加
# 更快一点的范例，对四个原始数组使用Counter，然后分组for循环遍历的时候遍历的counter之和字典的itemes，代码如下
def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    recount = 0
    n = len(nums1)
    if n == 1:
        if nums1[0] + nums2[0] + nums3[0] + nums4[0] == 0:
            recount += 1
        return recount
    else:
        dict1 = collections.Counter(nums1)
        dict2 = collections.Counter(nums2)
        dict3 = collections.Counter(nums3)
        dict4 = collections.Counter(nums4)
        dict12 = {}
        for i, numi in dict1.items():
            for j, numj in dict2.items():
                if i + j in dict12:
                    dict12[i + j] += numi * numj
                else:
                    dict12[i + j] = numi * numj
        for k, numk in dict3.items():
            for l, numl in dict4.items():
                m = -(k + l)
                if m in dict12:
                    recount += numk * numl * dict12[m]
    return recount


a = Solution().offical(nums1 = [0,0], nums2 = [0,0], nums3 = [0,0], nums4 = [0,0])
print(a)