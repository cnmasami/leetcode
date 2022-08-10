# 给定一个包含n + 1 个整数的数组nums ，其数字都在[1, n]范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，返回这个重复的数 。
#
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
from typing import List


class Solution:
    # 没有理解题意，不一定只重复一次
    # 不满足空间复杂度的要求
    def findDuplicate(self, nums: List[int]) -> int:
        ret_set = set()

        for num in nums:
            if num in ret_set:
                return num
            else:
                ret_set.add(num)

    # 定义cnt[i]表示nums数组中小于等于i的数有多少个，
    # 假设我们重复的数是target，那么[1, target-1]里的所有数满足cnt[i]<=i
    # [target, n]里面的所有数满足cnt[i] > n, 且满足单调性
    # 如果知道cnt[]数组随数字i逐渐增大具有单调性
    # （即target前cnt[i] <=i, target后cnt[i]>i），
    # 那么我们就可以直接利用二分查找来找到重复的数
    # 对于所有的用例，可能有两种情况：
    # 1. 测试用例的数组中target出现了两次，其余的数各出现了一次
    # 这个时候肯定满足上文提及的性质，因为小于target的数i满足cnt[i] = i
    # 大于等于target的数j满足cnt[j] = j +1
    # 2. 如果测试用例的数组中target出现了三次及以上，
    # 那么必然有一些数不在nums数组中了，这个时候相当于我们用target去替换了这些数
    # 如果替换的数i小于target，那么[i, target -1]的cnt值均减一，其他不变，满足条件
    # 如果替换的数j大于等于target，那么[target, j-1]的cnt值均加一，其他不变，亦满足条件
    def bs_findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n -1
        ans = -1

        while left <= right:
            mid = (left + right) >> 1
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid -1
                ans = mid
        return ans

    # 快慢指针环形链表
    # 因为n+1个元素的list，list里的值在1-n，所以list里的值肯定都包含在数组下标里
    # 所以可以组成一个元素和下标之间的映射关系，
    # 比如0->1 1->3 2->4 3->2
    # 我们从下标为 0 出发，根据 f(n)f(n) 计算出一个值，以这个值为新的下标，再用这个函数计算，以此类推，直到下标超界。这样可以产生一个类似链表一样的序列。
    # 0->1->3->2->4->null
    # 如果数组中有重复的数，以数组[1, 3, 4, 2, 2] 为例, 我们将数组下标n和数nums[n]建立一个映射关系f(n)
    # 其映射关系 n->f(n)为：
    # 0->1 1->3 2->4 3->2 4->2
    # 同样的，我们从下标为 0 出发，根据 f(n) 计算出一个值，以这个值为新的下标，再用这个函数计算，以此类推产生一个类似链表一样的序列。
    # 0->1->3->2->4->2->4->2->……
    def findDuplicate3(self, nums: List[int]) -> int:
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        # 快慢指针使得在环中相遇
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 根据快慢指针在环相遇的地方找环入口
        # https://leetcode.cn/problems/linked-list-cycle-ii/solution/142-huan-xing-lian-biao-ii-jian-hua-gong-shi-jia-2/
        # 这个题解写的很清晰
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow







a = Solution().bs_findDuplicate([3,2,3,3,3])
print(a)