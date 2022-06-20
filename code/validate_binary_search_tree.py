# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 根据搜索二叉树中序遍历递增特性，判断是不是二叉搜索树
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        is_valid = True

        def dfs(node):
            nonlocal prev, is_valid
            if not is_valid:
                return

            if node.left:
                dfs(node.left)

            if node.val <= prev:
                is_valid = False

            prev = node.val

            if node.right:
                dfs(node.right)


        dfs(root)

        return is_valid

    # 迭代中序遍历
    def iter_isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True

    # 二叉搜索树左子树不为空，则左子树上所有节点的值均小于它的根节点的值
    # 右子树不为空，则右子树上所有节点的值均大于它的根结点的值
    # 设计一个带参数的递归函数来判断，low，upper，如果root节点的值不在l，r的范围内说明不满足条件，直接返回
    # 根据二叉搜索树的性质，在递归调用左子树的时候，把上界upper改为root.val
    # 右子树的时候，把下界改为root.val
    # 递归的调用入口 l，r为-inf和inf
    def rec_isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, uppper):
            if not node:
                return True

            if node.val <= lower or node.val >= uppper:
                return False

            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, uppper):
                return False

            return True

        return helper(root, float('-inf'), float('inf'))



node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2, node1, node3)

a = Solution().isValidBST(node2)
print(a)