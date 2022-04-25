# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def postorder(self, root: Optional[TreeNode], ans):
        if not root:
            return

        self.postorder(root.left, ans)
        self.postorder(root.right, ans)
        ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.postorder(root, ans)

        return ans

    # 可以用prev来记录访问历史，在回溯到父节点时，可以由此来判断，上一个访问的节点是否为右子树
    def iterate_method(self, root: Optional[TreeNode]):
        ans = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                # if root.left:
                root = root.left

            # 从栈中弹出元素，此时左子树一定时访问完的
            root = stack.pop()
            # 现在需要确定的是是否有右子树，或者右子树是否是访问过的
            # 如果没有右子树，或者右子树访问完了，也就是上一个访问的节点是右子树的死活
            # 说明可以访问当前节点
            if not root.right or prev == root.right:
                ans.append(root.val)
                prev = root
                root = None
            else:
                # 如果右子树没有被访问，就将当前的节点压入栈中
                # 并且访问右子树
                stack.append(root)
                root = root.right

        return ans

    def morris(self, root: Optional[TreeNode]):
        def addPath(node: TreeNode):
            count = 0
            while node:
                count += 1
                res.append(node.val)
                node = node.right

            i, j = len(res) - count, len(res) -1
            while i < j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1

        if not root:
            return []

        res = []
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right

                if not p2.right:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
                    addPath(p1.left)
            p1 = p1.right

        addPath(root)
        return res

nod7 = TreeNode(8)
nod5 = TreeNode(5)
nod4 = TreeNode(4, left=nod7)
nod1 = TreeNode(3, left=nod4, right=nod5)
nod2 = TreeNode(2, left=nod1)
nod3 = TreeNode(1, right=nod2)
a = Solution().morris(nod3)
print(a)

# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/bang-ni-dui-er-cha-shu-bu-zai-mi-mang-che-di-chi-t/




