# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# 官方题解方法一 hashset
class Solution:
    def find(self, root, k, tree_set):
        if not root:
            return False
        if (k - root.val) in tree_set:
            return True

        tree_set.add(root.val)

        return self.find(root.left, k, tree_set) or self.find(root.right, k, tree_set)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        tree_set = set()
        return self.find(root, k, tree_set)


# 广度优先搜索查找
# class Solution:
#     def findTarget(self, root: TreeNode, k: int) -> bool:
#         tree_set = set()
#
#         tree_list = []
#         tree_list.append(root)
#
#         while len(tree_list):
#             if tree_list.pop(0)

# 中序遍历然后使用双指针
class Solution:
    def inorder(self, root: TreeNode, tree_list):
        if not root:
            return
        self.inorder(root.left, tree_list)
        tree_list.append(root.val)
        self.inorder(root.right, tree_list)

    def findTarget(self, root: TreeNode, k: int):
        tree_list = []
        self.inorder(root, tree_list)
        left = 0
        right = len(tree_list) - 1
        while left < right:
            sum = tree_list[left] + tree_list[right]

            if sum == k:
                return True
            if sum < k:
                left += 1
            else:
                right -= 1

        return False
