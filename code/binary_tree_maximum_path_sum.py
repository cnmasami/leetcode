# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0

            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            node_sum = left + right + node.val

            max_sum = max(max_sum, node_sum)

            return max(left + node.val, right + node.val)

        helper(root)

        return max_sum


leave = TreeNode(-1)
root = TreeNode(2, leave)

a = Solution().maxPathSum(root)
print(a)


