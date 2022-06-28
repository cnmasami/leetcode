# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
#
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
#


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            return TreeNode(nums[1], TreeNode(nums[0]))
        else:
            root = len(nums) // 2

            left = self.sortedArrayToBST(nums[:root])
            right = self.sortedArrayToBST(nums[root+1:])

            return TreeNode(nums[root], left, right)


a = Solution().sortedArrayToBST([-10,-3,-2,0,5,9])
print(a.val)
left = a.left
while left:
    print('left', left.val)
    left = left.left

right = a.right
while right:
    print('right', right.val)
    right = right.right