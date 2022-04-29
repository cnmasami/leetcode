# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    # 深度优先
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 广度优先，广度优先搜索的队列里存放的是当前层的所有结点
    # 每次扩展下一层的时候，不同于广度优先搜索的每次只从队列里拿出一个结点，
    # 我们需要将队列里的所有结点都拿出来进行扩展
    # 这样能保证每次扩展完的时候，队列里存放的是当前层的所有结点，即我们是一层一层地进行扩展
    # 最后我们用一个ans来维护扩展的次数，该二叉树的最大深度即为ans
    def breadth_first(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        deque = collections.deque([root])
        len = 0
        while deque:
            for _ in range(len(deque)):
                tmp = deque.popleft()
                if tmp.left:
                    deque.append(tmp.left)
                if tmp.right:
                    deque.append(tmp.right)
            len += 1

        return len
