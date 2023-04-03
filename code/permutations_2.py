# 全排列 II

# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, size, path, res, used):
            if index == size and path not in res:
                res.append(path.copy())

            for i in range(size):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True

                    dfs(nums, index+1, size, path, res, used)

                    path.pop()
                    used[i] = False

        size = len(nums)
        used = [False for _ in nums]
        res = []

        dfs(nums, 0, size, [], res, used)

        return res

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, size, path, res, used):
            if index == size :
                res.append(path.copy())

            for i in range(size):
                if not used[i]:
                    # 剪枝 重复数字不考虑
                    # 考虑重复元素要优先排序，将重复的都放在一起，便于找到重复元素和剪枝
                    # 遇到第一个重复元素才需要考虑剪枝
                    # 但是考虑剪枝的时候还要考虑跟它重复的元素有没有被使用过
                    # 如果前一个重复元素没有使用过，那么在当前重复元素下一层的可选项中一定会存在，
                    # 那么一定会重复，则整体剪枝，且提前剪枝（感觉这个应该是上个重复的元素没有使用
                    # 是因为状态刚刚被撤销，正是因为刚被撤销，下面的搜索中还会使用到，因此会产生重复
                    # 剪掉的就是这样的分支。）
                    # 因为假设到了当前元素b，那么前一个元素a一定是处理过的，它的 used[a]==true 理应成立
                    # 但如果 used[a]==false 说明什么
                    # 说明 nums[a] 已经被从当前组合集合中撤销掉了，这个false肯定是我们手动把它又重置为了false所导致的。
                    # 既然说 nums[a] 被撤销，而现在 nums[b] 被选择，那也就是说：
                    # 现在 nums[b] 被顶替在了之前 nums[a] 的位置上。
                    # 如果 nums[a]==nums[b] ，那么当前组合结果和之前不撤销nums[a]的那个组合有什么区别？
                    # 是没有区别的，这样就导致两个组合是重复的！这也就是我们需要剪枝去重的情况！
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    path.append(nums[i])
                    used[i] = True

                    dfs(nums, index+1, size, path, res, used)

                    path.pop()
                    used[i] = False

        size = len(nums)
        nums.sort()
        used = [False for _ in nums]
        res = []

        dfs(nums, 0, size, [], res, used)

        return res


a = Solution().permuteUnique([1,2,3])
print(a)
