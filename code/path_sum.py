# 给你二叉树的根节点root 和一个表示目标和的整数targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和targetSum 。
# 如果存在，返回 true ；否则，返回 false 。
#
# 叶子节点 是指没有子节点的节点。

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum- root.val)

    # 核心思想是一次遍历, 在遍历时记录从根节点到当前节点的路径和,以防止重复计算
    # 使用广度优先, 记录从根节点到当前节点的路径和,以防止重复计算
    # 使用两个队列, 分别存储将要遍历的节点, 以及根节点到这些节点的路径和
    def bfs(self, root:Optional[TreeNode], targetSum: int):
        if not root:
            return False

        que_node = collections.deque([root])
        que_val = collections.deque([root.val])

        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == targetSum:
                    return True
                continue

            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)

            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)

        return False

