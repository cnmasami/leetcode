# 二叉搜索树的最小绝对差

# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二叉搜索树中序遍历是递增数组
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = float('inf')
        pre = -1

        def dfs(node):
            nonlocal pre, diff
            if not node:
                return

            dfs(node.left)

            if pre == -1:
                pre = node.val
            else:
                diff = min(diff, node.val - pre)
                pre = node.val

            dfs(node.right)

        dfs(root)
        return diff


