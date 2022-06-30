# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点指没有子节点的结点

# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path_list = []

        node_que = collections.deque([root])
        parent_que = collections.deque([str(root.val)])

        while node_que:
            node = node_que.popleft()
            cur_path = parent_que.popleft()

            if not node.left and not node.right:
                path_list.append(cur_path)

            if node.left:
                lcur_path = cur_path + '->' + str(node.left.val)
                node_que.append(node.left)
                parent_que.append(lcur_path)

            if node.right:
                rcur_path = cur_path + '->' + str(node.right.val)
                node_que.append(node.right)
                parent_que.append(rcur_path)

        return path_list

    def dfs_binaryTreePaths(self, root):
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)

        paths = []
        dfs(root, '')
        return paths

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node5

a = Solution().binaryTreePaths(node1)
print(a)

