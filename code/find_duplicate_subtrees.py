# 寻找重复的子树

# 给你一棵二叉树的根节点 root ，返回所有 重复的子树 。
#
# 对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。
#
# 如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。
#

# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 序列化
    # 每棵树都序列化成一个字符串
    # 递归的方法序列化，将一颗以x为根节点值的子树序列化为x(左子树序列化结果)(右子树序列化结果)
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def tree_seq(node):
            if not node:
                return ''

            serial = ''.join([str(node.val), '(', tree_seq(node.left), ')(', tree_seq(node.right), ')'])
            sub_tree = seen.get(serial, None)
            if sub_tree:
                repeat.add(sub_tree)
            else:
                seen[serial] = node

            return serial

        seen = dict()
        repeat = set()

        tree_seq(root)
        return list(repeat)

    def findDuplicateSubtrees2(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            if not node:
                return 0

            tri = (node.val, dfs(node.left), dfs(node.right))

            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx

        idx = 0
        seen = dict()
        repeat = set()
        dfs(root)
        return list(repeat)



node41 = TreeNode(4)
node42 = TreeNode(4)
node43 = TreeNode(4)
node21 = TreeNode(2, node41)
node22 = TreeNode(2, node42)
node3 = TreeNode(3, node22, node43)
node1 = TreeNode(1,node21, node3)

a = Solution().findDuplicateSubtrees(node1)
print(a)


