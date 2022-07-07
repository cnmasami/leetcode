# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        path_num = 0

        def dfs(root, targetSum):
            nonlocal path_num
            if not root:
                return

            if root.val == targetSum:
                path_num += 1

            dfs(root.left, targetSum - root.val)
            dfs(root.right, targetSum - root.val)

        node_queue = collections.deque([root])

        while node_queue:
            node = node_queue.popleft()

            dfs(node, targetSum)

            if node.left:
                node_queue.append(node.left)

            if node.right:
                node_queue.append(node.right)

        return path_num

    def rec_path_sum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)

            return ret

        if root is None:
            return 0

        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)

        return ret

    # 前缀和： 由根结点到当前节点的路径上所有节点的和
    # 先序遍历二叉树，记录下根节点root到当前节点p的路径上除当前节点以外所有节点的前缀和
    # 使用dfs遍历一次整棵树，实时地计算从root到当前结点的前缀和。
    # 在同一条路径上，更短的前缀和已经被计算出来了，
    # 为了对前缀和求差以查找是否存在pre_i - pre_j = targetSum（pre_i为当前结点前缀和，pre_j为当前路径上i节点之前的结点j的前缀和)，
    # 我们需要保存之前结点的前缀和。map是一个不假思索的选择，key保存前缀和，value保存对应此前缀和的数量。
    # 需要注意的是，前缀和求差的对象是同一条路径上的结点，因此在dfs遍历树的过程中，
    # 当到达叶子结点，之后向上返回时，路径退缩，使得当前结点将退出后续路径。
    # 对前缀和求差的前提是要保证map中所保存的前缀和均为同一路径上的结点的前缀和，因此需要删除返回前的节点所代表的前缀和。
    def prefix_path_sum(self, root, target_sum) -> int:
        # prefix[前缀和] = 数量
        prefix = collections.defaultdict(int)

        prefix[0] = 1

        def dfs(root, curr):
            # 对于每个节点
            # 往下遍历时,先更新prefix
            # 递归返回时, 还原prefix

            if not root:
                return 0

            ret = 0

            # 当前前缀和
            curr += root.val
            # 从字典中取出,前缀和为curr-targetnum的值的路径的个数,加上这个结果
            ret += prefix[curr - target_sum]
            # 前缀和为curr的路径个数加一
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            # 回溯
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)





