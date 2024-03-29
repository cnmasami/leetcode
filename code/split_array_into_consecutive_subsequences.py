# 分割数组为连续子序列

# 给你一个按非递减顺序排列的整数数组nums
# 请你判断是否能在将nums分割成一个或者多个子序列的同时满足下述两个条件：
# 每个子序列都是一个连续递增序列 即， 每个整数恰好比前一个整数大1
# 所有子序列的长度至少为3
# 如果可以分割 nums 并满足上述条件，则返回 true ；否则，返回 false 。
import collections
import heapq
from typing import List


class Solution:
    # 哈希表+最小堆
    # 由于需要将数组分割成一个或多个由连续整数组成的子序列，
    # 因此只要知道子序列的最后一个数字和子序列的长度，就能确定子序列。
    #
    # 当x在数组中时，如果存在一个子序列以x−1 结尾，长度为k，则可以将x加入该子序列中，
    # 得到长度为 k+1 的子序列。
    # 如果不存在以 x−1 结尾的子序列，则必须新建一个只包含x 的子序列，长度为1。
    #
    # 当x 在数组中时，如果存在多个子序列以x−1 结尾，应该将 x 加入其中的哪一个子序列？
    # 由于题目要求每个子序列的长度至少为3，显然应该让最短的子序列尽可能长，
    # 因此应该将x 加入其中最短的子序列。
    #
    # 基于上述分析，可以使用哈希表和最小堆进行实现。
    #
    # 哈希表的键为子序列的最后一个数字，值为最小堆，用于存储所有的子序列长度，
    # 最小堆满足堆顶的元素是最小的，因此堆顶的元素即为最小的子序列长度。
    #
    # 遍历数组，当遍历到元素 x 时，可以得到一个以x 结尾的子序列。
    #
    # 如果哈希表中存在以x−1 结尾的子序列，则取出以 x−1 结尾的最小的子序列长度，将子序列长度加1
    # 之后作为以x 结尾的子序列长度。此时，以 x−1 结尾的子序列减少了一个，
    # 以x 结尾的子序列增加了一个。
    #
    # 如果哈希表中不存在以x−1 结尾的子序列，则新建一个长度为 1 的以 x 结尾的子序列。
    #
    # 由于数组是有序的，因此当遍历到元素 x 时，数组中所有小于 x 的元素都已经被遍历过，
    # 不会出现当前元素比之前的元素小的情况。
    #
    # 遍历结束之后，检查哈希表中存储的每个子序列的长度是否都不小于3，即可判断是否可以完成分割。
    # 由于哈希表中的每条记录的值都是最小堆，堆顶元素为最小的子序列长度（以当前的键为最后一个数字的子序列），
    # 因此只要遍历每个最小堆的堆顶元素，即可判断每个子序列的长度是否都不小于 3。
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for num in nums:
            queue = mp.get(num -1)
            if queue:
                prev_length = heapq.heappop(queue)
                heapq.heappush(mp[num], prev_length+1)
            else:
                heapq.heappush(mp[num], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())


    # 贪心
    # 对于数组中的元素 x，如果存在一个子序列以 x−1 结尾，则可以将  x 加入该子序列中。
    # 将 x 加入已有的子序列总是比新建一个只包含 x 的子序列更优，
    # 因为前者可以将一个已有的子序列的长度增加 1，
    # 而后者新建一个长度为  1 的子序列，
    # 而题目要求分割成的子序列的长度都不小于  3，因此应该尽量避免新建短的子序列。
    # 基于此，可以通过贪心的方法判断是否可以完成分割。

    # 使用两个哈希表，第一个哈希表存储数组中的每个数字的剩余次数，
    # 第二个哈希表存储数组中的每个数字作为结尾的子序列的数量。
    # 初始时，每个数字的剩余次数即为每个数字在数组中出现的次数，因此遍历数组，初始化第一个哈希表。
    # 在初始化第一个哈希表之后，遍历数组，更新两个哈希表。
    # 只有当一个数字的剩余次数大于 0 时，才需要考虑这个数字是否属于某个子序列。
    # 假设当前元素是x，进行如下操作
    # 首先判断是否存在以x-1结尾的子序列，即根据第二个哈希表判断x-1作为结尾的子序列的数量是否大于0
    # 如果大于0，则将元素x加入该子序列中，
    # 由于x被使用了一次，因此需要在第一个哈希表中将x的剩余次数减1
    # 又由于该子序列的最后一个数字从x-1变成了x，因此需要在第二个哈希表中将x-1作为结尾的子序列的数量减1
    # 以及将x作为结尾的子序列的数量加1
    # 否则，x为一个子序列的第一个数，为了得到长度至少为3的子序列，x+1和x+2必须在子序列中，
    # 因此需要判断在第一个哈希表中x+1和x+2的剩余次数是否都大于0
    # 当x+1和x+2的剩余次数都大于0时,可以新建一个长度为3的子序列[x, x+1, x+2],
    # 由于这三个数都被使用了一次,因此需要在第一个哈希表中将这三个数的剩余次数分别减1
    # 又由于该子序列的最后一个数字是x+2,因此需要在第二个哈希表中将x+2作为结尾的子序列的数量加1
    # 否则,无法得到长度为3的子序列[x, x+1, x+2], 因此无法完成分割,返回false
    def greedy_isPossible(self, nums: List[int]) -> bool:
        count_map = collections.Counter(nums)
        end_map = collections.Counter()

        for num in nums:
            if count_map[num] > 0:
                prev_end_count = end_map.get(num-1, 0)
                if prev_end_count > 0:
                    count_map[num] -= 1
                    end_map[num -1] = prev_end_count - 1
                    end_map[num] += 1
                else:
                    if count_map.get(num+1, 0) > 0 and count_map.get(num + 2, 0) > 0:
                        count_map[num] -= 1
                        count_map[num + 1] -= 1
                        count_map[num + 2] -= 1
                        end_map[num + 2] += 1
                    else:
                        return False

        return True

    def isPossible2(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            for v in res:
                if n == v[-1] + 1:
                    v.append(n)
                    break
            else:
                res.insert(0, [n])

        return all([len(v) >= 3 for v in res])


a = Solution().isPossible2(nums = [1,2,3,4,4,5])
print(a)