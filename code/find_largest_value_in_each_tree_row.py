# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        largest = []

        q = collections.deque([[root]])

        while q:
            larg = float('-inf')
            level = []
            node_list = q.popleft()

            for node in node_list:
                larg = max(node.val, larg)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            if level:
                q.append(level)
            largest.append(larg)

        return largest


    def dfs_largestValue(self, root:Optional[TreeNode]) -> List[int]:
        largest = []

        def dfs(root, level):
            if not root:
                return
            if level > len(largest):
                largest.append(root.val)
            else:
                largest[level -1] = max(largest[level-1], root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)

        return largest


node5 = TreeNode(5)
node3 = TreeNode(3)
node9 = TreeNode(9)
node53 = TreeNode(3, node5, node3)
node2 = TreeNode(2, None, node9)
node1 = TreeNode(1, node53, node2)

l = Solution().largestValues(node1)
print(l)

