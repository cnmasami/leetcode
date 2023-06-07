# 打家劫舍 III
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为root。
#
# 除了root之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的root。返回在不触动警报的情况下，小偷能够盗取的最高金额。
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
    # 对于单个节点，两种方法，偷自己，或者偷自己的子节点
    # 用fo表示选择o节点的情况下，o节点的子树上被选择的节点的最大权值和
    # go表示不选择o节点的情况下，o节点的子树上被选择的节点的最大权值和
    # l和r代表o的左右孩子
    # 当o被选中时，o的左右孩子都不能被选中，所以fo=gl+gr
    # 当o不被选中时，o的左右孩子可以被选中，也可以不被选中
    # 对于o的某个具体孩子，它对o的贡献是x被选中和不被选中情况下权值和的较大值
    # 所以，go = max(fl , gl) + max(fr + gr)
    # 用哈希表来存f和g的函数值。用深度优先搜索的办法后续遍历二叉树
    # 就可以得到每一个节点的f和g，根节点的f和g的最大值就是我们要找的答案
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                # 没有节点，怎么选都是0
                return 0, 0

            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)

            rob = l_not_rob + r_not_rob + node.val
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return rob, not_rob

        return max(dfs(root))




# node3 = TreeNode(3)
# node1 = TreeNode(1)
# node2 = TreeNode(2, None, node3)
# node32 = TreeNode(3, None, node1)
# node33 = TreeNode(3, node2, node32)


node4 = TreeNode(4)
# node1 = TreeNode(1)
node2 = TreeNode(1, None, node4)
node32 = TreeNode(3)
node33 = TreeNode(2, node2, node32)



a = Solution().rob(node33)
print(a)


