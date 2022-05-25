#给定一个 N 叉树，找到其最大深度。

# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
#



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # list格式
    def maxDepth(self, root: list) -> int:

        if not root:
            return 0

        if len(root) == 1:
            return 1

        root_node = root.pop(0)
        root.pop(0)
        depth = 1
        deq = [[root_node]]

        #
        while deq:
            node = deq.pop(0)
            depth += 1

            node_num = len(node)

            child_list = []
            count = 0
            while root:
                node = root.pop(0)
                if node:
                    child_list.append(node)
                else:
                    count +=1

                if count == node_num:
                    deq.append(child_list)
                    break

        return depth


    def max_depth(self, root:Node):
        if not root:
            return 0

        if root.children:
            return max([self.maxDepth(child) for child in root.children]) + 1
        else:
            return 1

    def bfs_maxDepth(self, root:Node):

        if root is None:
            return 0

        ans = 0
        queue = [root]

        # while queue:
        #     child_list = []
        #     for node in queue:
        #         for child in node.children:
        #             child_list.append(child)
        #             queue = child_list
        #     ans += 1

        while queue:
            queue = [child for node in queue for child in node.children]
            ans += 1

        return ans


# a = Solution().maxDepth([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
a = Solution().maxDepth([1])
print(a)








