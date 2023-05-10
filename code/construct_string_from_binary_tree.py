# 根据二叉树创建字符串

# 给你二叉树的根节点 root ，请你采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。
#
# 空节点使用一对空括号对 "()" 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
#

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ''

        def dfs(root):
            nonlocal ans

            if not root:
                if ans[-1].isdigit():
                    ans += '()'
                elif ans.endswith('()'):
                    ans = ans[:-2]

                return

            # if not ans:
            #     ans = ans + str(root.val)
            # else:
            ans = ans + '(' + str(root.val)

            dfs(root.left)
            dfs(root.right)

            ans += ')'

        dfs(root)

        ans = ans[1:-1]

        return ans

node4 = TreeNode(4)
node2 = TreeNode(2, None, node4)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)

a = Solution().tree2str(node1)
print(a)

