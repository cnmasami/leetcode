#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 克隆图
# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
#
# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }


# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    # 遍历整个图，遍历的时候要记录已经访问的节点，用一个字典记录
    # DFS和BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        lookup = {}

        def dfs(node):
            if not node: return

            if node in lookup:
                return lookup[node]

            clone = Node(node.val, [])

            lookup[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)

    def cloneGraph_bfs(self, node: Optional['Node']) -> Optional['Node']:
        lookup = {}

        def bfs(node):
            if not node: return

            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.appendleft(node)

            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])

            return clone

        return bfs(node)

