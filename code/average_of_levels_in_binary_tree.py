# 二叉树的层平均值
# 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。
# 与实际答案相差 10-5 以内的答案可以被接受


# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        que = collections.deque([root])
        res = []

        while que:
            node_num = len(que)
            temp = []
            for _ in range(node_num):
                node = que.popleft()

                temp.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.append(sum(temp) / len(temp))

        return res

    def dfs_averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        ans = []

        def dfs(node, level):
            if len(ans) < level:
                ans.append([])

            ans[level-1].append(node.val)

            if node.left:
                dfs(node.left, level+1)

            if node.right:
                dfs(node.right, level+1)

        dfs(root, 1)

        return [sum(temp) / len(temp) for temp in ans]