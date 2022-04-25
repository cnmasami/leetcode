# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and not q:
            return False
        if not p and q:
            return False

        if not p and not q:
            return True

        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False

    # 深度优先
    def offical(self, p: TreeNode, q: TreeNode) ->  bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def breadth_first(self, p: TreeNode, q: TreeNode) ->bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False

            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2

    def breadth_other(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]

        while queue:
            nodep, nodeq = queue.pop(0)

            if not nodep  and not nodeq:
                continue
            elif not nodeq or not nodep:
                return False
            elif nodeq.val != nodep.val:
                return False
            else:
                queue.append((nodep.left, nodeq.left))
                queue.append((nodep.right, nodeq.right))

        return True
