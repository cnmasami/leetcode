# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depthOfBinaryTree(self, root: TreeNode):
        if not root:
            return 0

        return max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right)) + 1

    def balanceNode(self, root:TreeNode):
        if not root:
            return True

        return abs(self.depthOfBinaryTree(root.left) - self.depthOfBinaryTree(root.right)) <= 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        node_list = collections.deque([root])

        while node_list:
            root = node_list.popleft()

            if self.balanceNode(root):
                node_list.append(root.left)
                node_list.append(root.right)
            else:
                return False

        return True

    # 递归，其实只需要修改上面的balancedNode，后面加上左右子树是否平衡的判断就可以了
    # 自顶向下的递归
    def is_balanced(self, root:TreeNode):
        if not root:
            return True

        return abs(self.depthOfBinaryTree(root.left) - self.depthOfBinaryTree(root.right)) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right)


    # 自底向上的递归
    # 在自顶向下的递归中，求二叉树度的函数会被重复调用，导致时间复杂度较高。
    # 如果使用自底向上的做法，对于每个节点，这个函数只会被调用一次
    # 自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树
    # 是否平衡。
    # 如果一颗子树是平衡的，则返回其高度（高度一定是非负整数）， 否则返回-1，如果存在一颗子树不平衡，则整个二叉树一定不平衡
    def from_bottom_to_top(self, root: TreeNode):
        def height(root: TreeNode) -> int:
            if not root:
                return 0

            lefHeight = height(root.left)
            rightHeight = height(root.right)

            if lefHeight == -1 or rightHeight == -1 or abs(lefHeight - rightHeight) > 1:
                return -1
            else:
                return max(lefHeight, rightHeight) + 1

        return height(root) >= 0
