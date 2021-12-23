# 给定一个二叉树，计算 整个树 的坡度 。
#
# 一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。
# 如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。
#
# 整个树 的坡度就是其所有节点的坡度之和。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#
#     def treeTilt(self, root, tile_dict):
#         if not root:
#             # return 0
#             return 0
#
#         rv = root.val
#
#         if (not root.left) and (not root.right):
#             tile_dict[root] = 0
#         elif not root.left:
#             tile_dict[root] = self.treeTilt(root.right, tile_dict)
#             # return self.treeTilt(root.right, tile_list)
#         elif not root.right:
#             tile_dict[root] = self.treeTilt(root.left, tile_dict)
#             # return self.treeTilt(root.left, tile_list)
#         elif (root.left and root.right):
#             # tile_list.append(self.treeTilt(root.left, tile_list) - self.treeTilt(root.right, tile_list))
#             # return abs(self.treeTilt(root.left, tile_list) - self.treeTilt(root.right, tile_list))
#             self.treeTilt(root.left, tile_dict)
#             self.treeTilt(root.right, tile_dict)
#             tile_dict[root] = abs(tile_dict[root.left] - tile_dict[root.right])
#
#
#     def findTilt(self, root: TreeNode) -> int:
#         tile_dict = {}
#
#         self.treeTilt(root,tile_dict)
#
#         return sum(tile_dict.values())
#
#         return sum(tile_list)


class Solution:
    def __init__(self):
        self.ans = 0

    def findTilt(self, root:TreeNode):
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0

        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)

        return sum_left + sum_right + node.val

class Solution2:

    def subTreeSum(self, root):
        if not root:
            return 0

        return self.subTreeSum(root.left) + self.subTreeSum(root.right)

    def treetilt(self, root, tile_dict):

        # tile_dict = {}
        if not root:
            tile_dict[root] = 0

        # if (not root.left) and (not root.right):
        #     tile_dict[root] = 0
        # 这个节点的坡度是做左节点和减去右节点和
        tile_dict[root] = abs(root.left + self.subTreeSum(root.left) - (root.right + self.subTreeSum(root.right)))


    def findTilt(self, root):

        tile_dict = {}
        # tile_dict
        # 坡度总和为各个节点的坡度值综合,title_dict存各个节点的坡度
        # self.treetilt(root.left, tile_dict)
        left = root.left
        while left:
            self.treetilt(left, tile_dict)
            left = root.left
        # tile_dict[root] = abs(root.left + self.subTreeSum(root.left) - (root.right + self.subTreeSum(root.right)))

        right = root.right
        while right:
            self.treetilt(right, tile_dict)
            right = root.right


        tile_dict[root] = tile_dict[root.left] + tile_dict[root.right]
        # self.treetilt(root.right, tile_dict)



        print(tile_dict)

        return sum(tile_dict.values())


# 整个树的坡度是各个节点的坡度之和
# 各个节点的坡度是左子树的和 - 右子树的和

class Solution3:
    def subTreeSum(self, node):
        if not node:
            return 0

        return node.val + self.subTreeSum(node.left) + self.subTreeSum(node.right)

        # if not node.left and not node.right:
        #     return node.val
        # else:
        #     return self.subTreeSum(node.left) + self.subTreeSum(node.right)

    # 计算单个节点坡度
    def nodeTilt(self, node: TreeNode):
        if not node:
            return 0

        signal_tile = abs(self.subTreeSum(node.left) - self.subTreeSum(node.right))

        return signal_tile

    def findTilt(self, root: TreeNode):

        sum = 0

        left = root.left
        while left:
            sum += self.nodeTilt(left)
            left = left.left

        sum += self.nodeTilt(root)

        right = root.right
        while right:
            sum += self.nodeTilt(right)
            right = right.right


        return sum




tree_left = TreeNode(2)
tree_right = TreeNode(3)
tree = TreeNode(1, tree_left, tree_right)

# a = Solution2().findTilt(tree)
a = Solution3().findTilt(tree)
print(a)