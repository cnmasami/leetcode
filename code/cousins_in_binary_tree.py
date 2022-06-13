# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
#
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
#
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
#
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_level = None
        y_level = None
        x_father = None
        y_father = None

        def dfs(level, node, father):
            nonlocal x_level, y_level, x_father, y_father

            if x_level and y_level:
                return

            if node.val == x:
                x_level = level
                x_father = father
            elif node.val == y:
                y_level = level
                y_father = father

            if node.left:
                dfs(level+1, node.left, node)

            if node.right:
                dfs(level+1, node.right, node)

        dfs(0, root, None)

        return x_level == y_level and x_father != y_father

    # 广度优先
    def is_cousions(self, root: TreeNode, x: int, y: int) -> bool:
        x_level = x_father = None
        y_level = y_father = None

        def update(node: TreeNode, parent: TreeNode, depth: int):
            nonlocal x_level, y_level, x_father, y_father

            if node.val == x:
                x_level = depth
                x_father = parent
            elif node.val == y:
                y_level = depth
                y_father = parent

        q = collections.deque([(root, 0)])
        update(root, None, 0)

        while q:
            node, depth = q.popleft()

            if node.left:
                q.append((node.left, depth + 1))
                update(node.left, node, depth +1)

            if node.right:
                q.append((node.right, depth + 1))
                update(node.right, node, depth +1)

            if x_level and y_level:
                break

        return x_level == y_level and x_father != y_father


