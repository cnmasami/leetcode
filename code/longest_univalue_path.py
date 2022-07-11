# 给定一个二叉树的root，返回最长的路径的长度 ，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 两个节点之间的路径长度由它们之间的边数表示。

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def helper(node):
            nonlocal max_path
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            left_arrow = right_arrow = 0

            if node.left and node.left.val == node.val:
                left_arrow = left + 1

            if node.right and node.right.val == node.val:
                right_arrow = right + 1

            max_path = max(max_path, left_arrow + right_arrow)

            return max(left_arrow, right_arrow)

        helper(root)

        return max_path






node12 = TreeNode(2)
node22 = TreeNode(2)
node32 = TreeNode(2)
node42 = TreeNode(2)
node52 = TreeNode(2)
node62 = TreeNode(2)
node72 = TreeNode(2)
node1 = TreeNode(2, node12, node22)
node12.left = node32
node12.right = node42
node22.left = node52
node22.right = node62
node32.left = node72

a = Solution().longestUnivaluePath(node1)
print(a)