
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
#
# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

""""""
# Definition for a Node.
import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []

        q = collections.deque([root])

        while q:
            level = []
            node_num = len(q)

            for _ in range(node_num):
                node = q.popleft()
                level.append(node.val)
                if node.children:
                    for child_node in node.children:
                        q.append(child_node)

            ans.append(level)

        return ans

    def dfs_levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []

        ans = []

        def dfs(level, node):
            if level > len(ans):
                ans.append([])

            ans[level-1].append(node.val)

            if node.children:
                for child_noe in node.children:
                    dfs(level+1, child_noe)

        dfs(1, root)

        return ans



