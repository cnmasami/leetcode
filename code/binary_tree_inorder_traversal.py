# 给定一个二叉树的根节点，返回它的中序遍历

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归
    def inorderTree(self, root: Optional[TreeNode], ans: List):

        if not root:
            return

        self.inorderTree(root.left, ans)

        ans.append(root.val)

        self.inorderTree(root.right, ans)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.inorderTree(root, ans)

        return ans

    # 迭代
    def iter_method(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # stack.pop()
            ans.append(root.val)
            root = root.right

        return ans

    # morris中序遍历
    # 它能将非递归的中序遍历空间复杂度降为O(1)
    # Morris遍历整体步骤：（假设当前遍历到的节点为x）
    # 1. 如果x无左孩子，先将x的值加入答案数组，再访问x的右孩子，即x=x.right
    # 2. 如果x有左孩子，找到x左子树上最右的节点，（即左子树中序遍历的最后一个节点，x在中序遍历中的前驱节点）
    # 我们记为predecessor，根据predecessor的右孩子是否为空，进行如下操作：
    # - 如果predecess的右孩子为空，则将其右孩子指向x，然后访问x的左孩子，即x=x.left
    # - 如果predecessor的右孩子不为空，则此时其右孩子指向x，说明，我们已经遍历完x的左子树
    # 将predecessor的右孩子置空，将x的值加入答案数组，然后访问x的右孩子，即x=x.right
    # 重复上述直到访问完整棵树
    # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
    def morris(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left:
                # find out predecessor
                # # 如果左节点不为空，就将当前节点连带右子树全部挂到
                # 			# 左节点的最右子树下面
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                # link predecessor to root
                # # 将root指向root的left
                predecessor.right = root
                # set left child of root to None
                temp = root
                root = root.left
                temp.left = None
            # # 左子树为空，则打印这个节点，并向右边遍历
            else:
                res.append(root.val)
                root = root.right

        return res


nod1 = TreeNode(3)
nod2 = TreeNode(2, left=nod1)
nod3 = TreeNode(1, right=nod2)
# a = Solution().inorderTraversal(nod3)
a = Solution().iter_method(nod3)
print(a)
