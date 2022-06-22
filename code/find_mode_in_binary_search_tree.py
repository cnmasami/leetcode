# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
#
# 如果树中有不止一个众数，可以按 任意顺序 返回。
#
# 假定 BST 满足如下定义：
#
# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树


# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 利用搜索二叉树中序遍历是升序数组的特性，
    # 如果有重复的元素，中序遍历的时候一定是连续出现的，
    # 记录当前这个节点的count，和maxCount比较，更新最终的返回列表
    def findMode(self, root: TreeNode) -> List[int]:
        prev = float('-inf')
        max_count = 0
        cru_count = 0
        final = []

        def dfs(root):
            nonlocal prev, cru_count, max_count
            if not root:
                return

            dfs(root.left)

            if root.val == prev:
                cru_count += 1
            else:
                cru_count = 1

            if cru_count > max_count:
                final.clear()
                final.append(root.val)
                max_count = cru_count
            elif cru_count == max_count:
                final.append(root.val)

            prev = root.val

            dfs(root.right)

        dfs(root)

        return final

node4 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node1 = TreeNode(1, node4, node2)
node2.left = node3


a = Solution().findMode(node1)
print(a)


