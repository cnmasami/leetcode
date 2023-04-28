# 另一棵树的子树

# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。
# 如果存在，返回 true ；否则，返回 false 。
#
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
#

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 这题还有KMP和树哈希的解法，但我都不会，就先这样吧，回来再看看那两个解法
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(root, subroot):
            if not root and not subroot:
                return True
            elif not root or not subroot:
                return False
            elif root.val != subroot.val:
                return False

            return is_identical(root.left, subroot.left) and is_identical(root.right, subroot.right)

        def dfs(root, subroot):
            is_sub = is_identical(root, subroot)

            if is_sub:
                return True
            else:
                is_left_sub = dfs(root.left, subroot) if root.left else False
                is_right_sub = dfs(root.right, subroot) if root.right else False

                return is_left_sub or is_right_sub

        return dfs(root, subRoot)









