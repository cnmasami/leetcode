# 省份数量

#有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
import collections
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = [-1] * len(isConnected)

        def find(root):
            son = root

            # 让root一直向上查找直到找到省会
            while provinces[root] >= 0:
                root = provinces[root]

            # 路径压缩，查找路径上的所有城市都直接连到省会
            while son != root:
                tmp = provinces[son]
                provinces[son] = root
                son = tmp

            return root

        # 按秩归并，pre数组存放的是下面连接的城市数量
        def union(root1, root2):
            if provinces[root2] < provinces[root1]:
                provinces[root2] += provinces[root1]
                provinces[root1] = root2
            else:
                provinces[root1] += provinces[root2]
                provinces[root2] = root1

        for idx, connected in enumerate(isConnected):
            for j in range(idx + 1, len(connected)):
                if isConnected[idx][j] == 1:
                    # 找到idx和j的省会
                    root1= find(idx)
                    root2 = find(j)
                    # 如果idx和j不在一个省但是彼此相连，将它们连到同一个省会
                    if root1 != root2:
                        union(root1, root2)

        cnt = 0
        for i in range(len(isConnected)):
            if provinces[i] < 0:
                cnt += 1

        return cnt

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent_2 = find(index2)
            parent_1 = find(index1)
            parent[parent_1] = parent_2
            # parent[find(index1)] = find(index2)

        cities = len(isConnected)
        parent = list(range(cities))

        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    union(i, j)

        # 如果parent==本身，说明它是省会
        provinces = sum(parent[i] == i for i in range(cities))
        return provinces

    # 深度优先，遍历所有城市，对于每一个城市，如果该城市尚未被访问，
    # 则从该城市开始深度优先搜索，通过矩阵isConnected得到与该城市直接相连的城市有哪些
    # 这些城市和该城市属于同一个连通分量，然后对这些城市继续深度优先搜索
    # 直到同一个连通分量的所有城市都被访问到，即可得到一个省份
    # 遍历完全部城市，即可得到连通分量的总数，即省份的总数
    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(i: int):
            for j in range(cities):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces

    def findCircleNum4(self, isConnected):
        citites = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(citites):
            if i not in visited:
                q = collections.deque([i])
                while q:
                    j = q.popleft()
                    visited.add(j)
                    for k in range(citites):
                        if isConnected[j][k] == 1 and k not in visited:
                            q.append(k)

                provinces += 1

        return provinces




a = Solution().findCircleNum2([[1,1,0],[1,1,0],[0,0,1]])
print(a)