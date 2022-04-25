# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root, ans):
        if not root:
            return

        ans.append(root)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.preorder(root, ans)

        return ans

    # 迭代
    def iter_method(self, root):
        ans = []
        stack = []

        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left

            root=stack.pop()
            root = root.right

        return ans

    # morris
    # morris的整体思路就是将以某个根节点开始，找到它左子树的最右侧节点之后与这个根节点进行连接
    def morris(self, root):
        ans = []

        while root:
            left = root.left
            if left:
                while left.right and left.right != root:
                    left = left.right

                if not left.right:
                    ans.append(root.val)
                    left.right = root
                    root = root.left
                    continue
                else:
                    left.right = None
            else:
                ans.append(root.val)

            root = root.right

        return ans


    def my_morris(self, root):
        ans = []

        while root:
            ans.append(root.val)

            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = root.right

                root = root.left
            else:
                root = root.right

        return ans


nod7 = TreeNode(8)
nod5 = TreeNode(5)
nod4 = TreeNode(4, left=nod7)
nod1 = TreeNode(3, left=nod4, right=nod5)
nod2 = TreeNode(2, left=nod1)
nod3 = TreeNode(1, right=nod2)
a = Solution().my_morris(nod3)
print(a)
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/
