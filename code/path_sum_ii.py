# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        path = []

        def dfs(root, targetSum):
            if not root:
                return

            path.append(root.val)
            targetSum -= root.val

            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])

            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        dfs(root, targetSum)

        return ret

    def bfs_pathSum(self, root:TreeNode, targetSum: int) -> List[List[int]]:
        ret = []
        parent = collections.defaultdict(lambda: None)

        def getPath(node: TreeNode):
            tmp = []
            while node:
                tmp.append(node.val)
                node = parent[node]
            ret.append(tmp[::-1])

        if not root:
            return ret

        que_node = collections.deque([root])
        que_total = collections.deque([0])

        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val

            if not node.left and not node.right:
                if rec == targetSum:
                    getPath(node)
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append(node.left)
                    que_total.append(rec)

                if node.right:
                    parent[node.right] = node
                    que_node.append(node.right)
                    que_total.append(rec)

        return ret




node7 = TreeNode(7)
node2 = TreeNode(2)
node11 = TreeNode(11, node7, node2)
node5 = TreeNode(5)
node1 = TreeNode(1)
node13 = TreeNode(13)
node4 = TreeNode(4, node11)
node8 = TreeNode(8, node13, node4)
node5root = TreeNode(5, node4, node8)

a = Solution().pathSum(node5root, 22)
print(a)


