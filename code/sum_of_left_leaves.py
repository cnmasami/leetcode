# 左子叶之和

# 给定二叉树的根节点root，返回所有左子叶之和

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        right_sum = self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val
        else:
            left_sum = self.sumOfLeftLeaves(root.left)

        return left_sum + right_sum

    def dfs_sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        is_leaf_node = lambda node: not node.left and not node.right

        def dfs(node):
            ans = 0
            if node.left:
                ans += node.left.val if is_leaf_node(node.left) else dfs(node.left)
            if node.right and not is_leaf_node(node.right):
                ans += dfs(node.right)
            return ans

        return dfs(root) if root else 0

    def bfs_sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        is_leaf_Node = lambda node: not node.left and not node.right
        q = collections.deque([root])
        ans = 0

        while q:
            node = q.popleft()
            if node.left:
                if is_leaf_Node(node.left):
                    ans += node.left.val
                else:
                    q.append(node.left)
            if node.right:
                if not is_leaf_Node(node.right):
                    q.append(node.right)

        return ans


node_9 = TreeNode(9)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, node_15, node_7)
node_3 = TreeNode(3, node_9, node_20)

a = Solution().sumOfLeftLeaves(node_3)
print(a)

