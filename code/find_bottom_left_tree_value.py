# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
#
# 假设二叉树中至少有一个节点。

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        most_left = None
        index = 0

        def dfs(root, level):
            nonlocal most_left, index

            if not root:
                return

            if level > index:
                most_left = root.val
                index = level

            dfs(root.left, level+1)
            dfs(root.right, level +1)

        dfs(root, 1)

        return most_left

    def bfs_findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        most_left = None

        q = collections.deque([[root]])

        while q:
            level = []
            node_list = q.popleft()
            most_left = node_list[0].val

            for node in node_list:
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            if level:
                q.append(level)

        return most_left

    # 官方的广度优先，遍历每一层节点，但是因为想要的是最左边的节点
    # 所以官方遍历每一层节点的时候是从右到左，
    # 所以pop的时候，保证最后一个pop出来的是最下面一层的最左边节点
    def offical_bfs(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        most_left = None

        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

            most_left = node.val

        return most_left

