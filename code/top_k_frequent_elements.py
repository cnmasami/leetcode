# 前K个高频元素

# 给你一个整数数组 nums 和一个整数 k ，
# 请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
import collections
import heapq
import random
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = collections.Counter(nums)

        return [ele[0] for ele in num_counter.most_common(k)]

    # 快速排序
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = list(collections.Counter(nums).items())
        ans = []

        def change_quick(arr):
            random.shuffle(arr)
            n = arr[0]
            left_arr = []
            right_arr = []
            for i in range(1, len(arr)):
                # 左侧的出现频率比较大，优先需要输出
                if arr[i][1] > n[1]:
                    left_arr.append(arr[i])
                else:
                    right_arr.append(arr[i])
            # 左侧和ans以及n的长度刚好为k，ans加入对应元素
            if len(ans) + len(left_arr) + 1 == k:
                ans.extend(left_arr)
                ans.append(n)
            elif len(ans) + len(left_arr) + 1 > k:
                change_quick(left_arr)
            else:
                ans.extend(left_arr)
                ans.append(n)
                change_quick(right_arr)

        change_quick(count)

        return [ke for ke, va in ans[:k]]

    # 堆排序
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        # mn = collections.Counter(nums)
        # heap = [(-value, key) for key, value in mn.items()]
        # heapq.heapify(heap)
        # return [heapq.heappop(heap)[1] for _ in range(k)]
        # return [item[0] for item in heapq.nlargest(k, Counter(nums).items(), key=lambda a:a[1])]
        # 次数在前，元素在后
        count = [(v, k) for k, v in collections.Counter(nums).items()]
        # 初始化堆
        h = count[:k]
        heapq.heapify(h)

        for i in range(k, len(count)):
            heapq.heappushpop(h, count[i])

        return [b for a, b in h]

    # 找到位于k-1位置的元素，此位置之前的元素都大于该元素，将他们输出即可
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        def partition(nums, left, right):
            key = nums[right][1]
            while left < right:
                while left < right and nums[left][1] >= key:
                    left += 1
                nums[right], nums[left] = nums[left], nums[right]
                while left < right and nums[right][1] <= key:
                    right -= 1
                nums[right], nums[left] = nums[left], nums[right]

            return left

        count = list(collections.Counter(nums).items())
        left, right = 0, len(count) - 1
        while True:
            pos = partition(count, left, right)
            if pos == k - 1:
                return [key for key, _ in count[:k]]
            elif pos < k - 1:
                left = pos + 1
            else:
                right = pos - 1



a = Solution().topKFrequent(nums = [1, 5, 4, 3,2,5,4,1,2,2,3,5], k = 2)
print(a)