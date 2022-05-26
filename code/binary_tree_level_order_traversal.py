# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        que = collections.deque([[root]])
        ans = [[root.val]]

        while root and que:
            node_list = que.popleft()
            child_list = []
            nodes = []

            for node in node_list:
                if node.left:
                    child_list.append(node.left.val)
                    nodes.append(node.left)
                if node.right:
                    child_list.append(node.right.val)
                    nodes.append(node.right)

            if child_list:
                ans.append(child_list)
                que.append(nodes)

        return ans

    def levelOrder2(self, root):
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            # 获取当前队列长度，相当于这一层的节点数
            node_num = len(queue)
            temp = []
            # 将队列中的元素都拿出来（也就是获取这一层的节点），放到临时list中
            # 如果节点的左/右子树不为空，也放入队列中
            for _ in range(node_num):
                r = queue.pop(0)
                temp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            # 将临时list加入最终返回结果中
            res.append(temp)

        return res


    def dfs_levelOrder(self, root):
        if not root:
            return []

        res = []

        def dfs(index, r):
            # 假设res是[[1],[2,3]]，index是3，就再插入一个空list放入res中
            if len(res) < index:
                res.append([])

            res[index-1].append(r.val)

            if r.left:
                dfs(index+1, r.left)

            if r.right:
                dfs(index + 1, r.right)

        dfs(1, root)

        return res


node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
node5 = TreeNode(3, node4, node3)

a = Solution().levelOrder(node5)

print(a)
