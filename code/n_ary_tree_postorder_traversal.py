# 给定一个 n叉树的根节点root，返回 其节点值的 后序遍历 。
#
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

""""""
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def helper(self, node, ans):
        for child in node.children:
            self.helper(child, ans)

        ans.append(node.val)

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        ans = []

        self.helper(root, ans)

        return ans

    def iter_postorder(self, root: Node) -> List[int]:
        stack = [(root, False)]
        ans = []

        while stack:
            node, poped = stack.pop()

            if node.children and not poped:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))
            else:
                ans.append(node.val)

        return ans


    def reverse_preorder(self, root: Node) -> List[int]:
        if not root:
            return []

        ans = []
        st = []

        while st:
            node = st.pop()
            ans.append(node.val)
            st.extend(node.children)

        ans.reverse()

        return ans

node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)
node1 = Node(1, [node3, node2, node4])

a = Solution().iter_postorder(node1)
print(a)

