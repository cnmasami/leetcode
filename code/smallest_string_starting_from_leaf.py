# 给定一颗根结点为root的二叉树，树中的每一个结点都有一个[0, 25]范围内的值，分别代表字母'a' 到'z'。
#
# 返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
#
# 注：字符串中任何较短的前缀在 字典序上 都是 较小 的：
#
# 例如，在字典序上"ab" 比"aba"要小。叶结点是指没有子结点的结点。
# 节点的叶节点是没有子节点的节点。

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # 这个可以替换成~ ，比z大的任意字符串，下面就可以不用判断smallest是否为空了
        smallest = ''


        def dfs(root, cur_str):
            nonlocal smallest
            if not root:
                return

            cur_str += chr(root.val + 97)
            print(cur_str)

            if not root.left and not root.right:
                if smallest:
                    smallest = min(smallest, cur_str[::-1])
                else:
                    smallest = cur_str[::-1]

            dfs(root.left, cur_str)
            dfs(root.right, cur_str)

        dfs(root, '')

        return smallest


node3l = TreeNode(3)
node4l = TreeNode(4)
node3r = TreeNode(3)
node4r = TreeNode(4)
node1 = TreeNode(1, node3l, node4l)
node2 = TreeNode(2, node3r, node4r)
node0 = TreeNode(0, node1, node2)

a = Solution().smallestFromLeaf(node0)
print(a)




