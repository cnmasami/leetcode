# 假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
#
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。
#
from typing import List

# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["KFC", "Shogun", "Burger King"]


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        visited = {}

        min_index = float('inf')

        for idx, ele in enumerate(list1):
            visited[ele] = idx

        for idx, ele in enumerate(list2):
            # 如果当前索引超过最小索引和，就直接返回
            # 后面的索引和只会越来越大
            if idx > min_index:
                return ans

            if ele in visited:
                index = idx + visited[ele]
                if index < min_index:
                    ans.clear()
                    ans.append(ele)
                    min_index = index
                elif index == min_index:
                    ans.append(ele)

        return ans


a = Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])
print(a)

