# 下一个更大元素

# nums1中数字x的 下一个更大元素 是指x在nums2 中对应位置 右侧 的 第一个 比x大的元素。
#
# 给你两个 没有重复元素 的数组nums1 和nums2 ，下标从 0 开始计数，其中nums1是nums2的子集。
#
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
# 并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
#
# 返回一个长度为nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
#
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            idx = nums2.index(num)
            for n2 in nums2[idx + 1:]:
                if n2 > num:
                    ans.append(n2)
                    break
            else:
                ans.append(-1)

        return ans

    # 单调栈 + 哈希
    # 预先处理nums2，使查询nums1中的每个元素在nums中的第一个更大元素时不再需要遍历nums2
    # 所以，可以使用单调栈来解决高效地计算nums2中每个元素右边的第一个更大的值
    # 倒叙遍历nums2，并用单调栈中维护当前位置右边的更大的元素列表，从栈底到栈顶的元素是单调递减的
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []

        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)

        return [res[num] for num in nums1]


a = Solution().nextGreaterElement2([4,1,2], [1,3,4,2])
print(a)

