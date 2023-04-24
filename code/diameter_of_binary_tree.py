# 二叉树的直径
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(root):
            nonlocal res
            if not root:
                return 0

            max_left = helper(root.left)
            max_right = helper(root.right)

            res = max(res, max_left + max_right)

            return max(max_left, max_right) + 1

        return max(helper(root.left) + helper(root.right), res)


node6 = TreeNode(6)
node4 = TreeNode(4)
node5 = TreeNode(5, node6)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)
a = Solution().diameterOfBinaryTree(node1)
print(a)