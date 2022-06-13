# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []

        def dfs(level, root):
            if len(ans) < level:
                ans.insert(0, [])

            ans[len(ans) - level].append(root.val)

            if root.left:
                dfs(level+1, root.left)

            if root.right:
                dfs(level+1, root.right)

        dfs(1, root)
        return ans

    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        q = collections.deque([root])

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans[::-1]


node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)

a = Solution().levelOrderBottom(node1)
print(a)
