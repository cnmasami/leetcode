# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：
#
# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。
#
# 叶节点 是指没有子节点的节点。

# 输入：root = [1, 2, 3]
# 输出：25
# 解释：
# 从根到叶子节点路径
# 1->2
# 代表数字
# 12
# 从根到叶子节点路径
# 1->3
# 代表数字
# 13
# 因此，数字总和 = 12 + 13 = 25


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        tree_sum = 0

        def dfs(node, cur_sum):
            nonlocal tree_sum
            if not node:
                return

            cur_sum = cur_sum * 10 + node.val

            if not node.left and not node.right:
                tree_sum += cur_sum
                return

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

        dfs(root, 0)

        return tree_sum

    # 官方的递归，没有用全局变量
    def dfs_sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal:int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val

            if not root.left and root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)


node2 = TreeNode(2)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)

a = Solution().sumNumbers(node1)
print(a)