# 二叉树中第二小的节点

# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。
# 如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
#
# 更正式地说，即root.val = min(root.left.val, root.right.val) 总成立。
#
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值 。
#
# 如果第二小的值不存在的话，输出 -1 。
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root.left and not root.right:
                return -1

            left_child = root.left.val
            right_child = root.right.val

            if left_child == root.val:
                left_child = dfs(root.left)

            if right_child == root.val:
                right_child = dfs(root.right)

            if left_child == -1:
                return right_child

            if right_child == -1:
                return left_child

            return min(left_child, right_child)

        return dfs(root)