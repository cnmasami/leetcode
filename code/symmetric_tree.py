# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def symmetric(self, p: Optional[TreeNode], q:Optional[TreeNode]):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.symmetric(p.left, q.right) and self.symmetric(p.right, q.left)

    # 递归
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.symmetric(root.left, root.right)


    # 迭代
    # 首先引入一个队列，这是把递归程序改成迭代程序的常用方法
    # 初始化时把根节点入队两次，每次提取两个结点并比较它们的值
    # （队列中每两个连续的结点应该是相等的，而且它们的子树互为镜像）
    # 然后将两个结点的左右子节点按相反的顺序插入队列中
    # 当队列为空时，或者我们检测到树不对称
    # 即从队列中取出两个不相等的连续结点时，该算法结束
    def iteration(self, root: Optional[TreeNode]):
        queue = [root, root]
        while queue:
            left = queue.pop()
            right = queue.pop()

            if left is None and right is None:
                continue

            if left is None or right is None or left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True











