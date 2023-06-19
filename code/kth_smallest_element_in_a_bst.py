# 二叉搜索树中第K小的元素

# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，
# 请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = 0

        def dfs(root):
            nonlocal count, ans
            if not root:
                return

            dfs(root.left)

            count += 1
            if count == k:
                ans = root.val
                return

            dfs(root.right)

        dfs(root)
        return ans

    def kthSmallest2(self, root: TreeNode, k:int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    # 记录子树的结点数
    # 如果需要频繁地查找第K小的值，将如何优化算法
    # 可以记录下以每个结点为根节点的子树的结点数，并在查找第k小的值时，
    # 使用如下方法搜索：
    # 令node等于根结点，开始搜索
    # 对当前节点node进行如下操作：
    # 如果node的左子树的结点数left小于k-1，则第k小的元素一定在node的右子树中，
    # 令node等于其的右子树结点，k等于k-left-1，并继续搜索
    # 如果node的左子树的结点数left等于k-1，则第k小的元素即为node，结束搜索并返回node即可
    # 如果node的左子树的结点数left大于k-1，则第k小的元素一定在node的左子树中，
    # 令node等于其左子结点，并继续搜索。
    def kthSmallest3(self, root: TreeNode, k: int) -> int:
        bst = MyBst(root)
        return bst.kth_smallest(k)

#     方法三平衡二叉树


class MyBst:
    def __init__(self, root: TreeNode):
        self.root = root

        # 统计以每个结点为根结点的子树的结点数，并储存在哈希表中
        self._node_num = {}
        self._count_node_num(root)


    def kth_smallest(self, k: int):
        node = self.root
        while node:
            left = self._get_node_num(node.left)
            if left < k - 1:
                node = node.right
                k -= left + 1
            elif left == k - 1:
                return node.val
            else:
                node = node.left

    def _count_node_num(self, node) -> int:
        # 统计以node为根结点的子树的结点数
        if not node:
            return 0
        self._node_num[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node_num[node]

    def _get_node_num(self, node) -> int:
        return self._node_num[node] if node is not None else 0


node2 = TreeNode(2)
node1 = TreeNode(1, None, node2)
node4 = TreeNode(4)
node3 = TreeNode(3, node1, node4)
a = Solution().kthSmallest(node3, 1)
print(a)
