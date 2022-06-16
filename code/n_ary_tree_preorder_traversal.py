# 给定一个 n叉树的根节点 root，返回 其节点值的 前序遍历 。
#
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

""""""
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def helper(self, node, ans):
        if not node:
            return

        ans.append(node.val)

        for child in node.children:
            self.helper(child, ans)

    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        self.helper(root, ans)

        return ans

    def iter_preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        stack = []
        ans = []

        stack.append(root)

        while stack:
            node = stack.pop()
            ans.append(node.val)
            # 因为先序从左到右遍历，而要入栈，所以根据栈的特性，从右到左将子节点入栈
            for child in reversed(node.children):
                stack.append(child)

        return ans

