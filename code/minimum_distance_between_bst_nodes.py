# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mini_diff = float('inf')
        stack = [root]
        node_list = []

        while stack:
            node_cur = stack.pop()

            for node in node_list:
                mini_diff = min(mini_diff, abs(node.val - node_cur.val))

            if node_cur.left:
                stack.append(node_cur.left)

            if node_cur.right:
                stack.append(node_cur.right)

            node_list.append(node_cur)

        return mini_diff


    # 对升序数组a求任意两个元素之差的最小值，一定是相邻元素之差的最小值，
    # 而对二叉搜索树，中序遍历得到的值序列是递增有序的。
    # 所以只要中序遍历，比较当前节点和前驱遍历节点的差值就可以了
    def inorder_minidiff(self, root: Optional[TreeNode]) -> int:
        mini_diff = prev = float('inf')

        def dfs(node):
            nonlocal mini_diff, prev
            if not node:
                return

            dfs(node.left)

            mini_diff = min(mini_diff, abs(node.val - prev))
            prev = node.val

            dfs(node.right)

        dfs(root)

        return mini_diff




node5 = TreeNode(48)
node6 = TreeNode(88)
node3 = TreeNode(69, node5, node6)
# node2 = TreeNode(2)
node4 = TreeNode(52)
node1 = TreeNode(90, node3)
node5.left = node4

a = Solution().minDiffInBST(node1)
print(a)



