# 数组中的第K个最大元素

# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(arr, left, right):
            key = arr[right]
            while left < right:
                while left < right and arr[left] > key:
                    left += 1
                arr[left], arr[right] = arr[right], arr[left]

                while left < right and arr[right] <= key:
                    right -= 1
                arr[left], arr[right] = arr[right], arr[left]

            return left

        left, right = 0, len(nums) - 1
        while True:
            pos = quick_sort(nums, left, right)
            if pos + 1 == k:
                return nums[k-1]
            elif pos + 1 < k:
                left = pos + 1
            else:
                right = pos -1


    def findKthLargest2(self, nums:List[int], k: int) -> int:
        def quickselect(mylist, k):
            random_index = random.randint(0, len(mylist) -1)
            pivot = mylist[random_index]
            left = []
            right = []
            mid = []
            for i in mylist:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                else:
                    mid.append(i)

            if len(right) >= k:
                pivot = quickselect(right, k)
            elif len(right) + len(mid) < k:
                pivot = quickselect(left, k - len(right) - len(mid))

            return pivot

        r = quickselect(nums, k)
        return r

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for x in nums:
            heapq.heappush(maxHeap, -x)
        for i in range(k-1):
            heapq.heappop(maxHeap)

        return -maxHeap[0]

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        # 大顶堆
        def maxHepify(arr, i, end):
            # j为i的左子结点(建堆时下标0表示堆顶)
            j = 2 * i + 1
            # 自上而下进行调整
            while j <= end:
                # i 的左右子节点分别为j和j+1
                if j + 1 <= end and arr[j+1] > arr[j]:
                    # 取两者之间的较大者
                    j += 1

                # 若i指示的元素小于其子节点中的较大者
                if arr[i] < arr[j]:
                    # 交换i和j的元素，并继续往下判断
                    arr[i], arr[j] = arr[j], arr[i]
                    # 往下走，i调整为其子节点j
                    i = j
                    # j调整为i的左子结点
                    j = 2 * i + 1
                else:
                    break

        n = len(nums)
        # 从第一个非叶子节点n//2-1开始依次往上进行建堆的调整
        for i in range(n // 2 - 1, -1, -1):
            maxHepify(nums, i, n-1)

        # 排序，依次将堆顶元素(当前最大值)放置到尾部，并调整堆
        # k-1次重建堆(堆顶元素)，或K次交换到尾部(倒数第K个元素)
        for j in range(n-1, n-k-1, -1):
            # 堆顶元素(当前最大值)放置到尾部j
            nums[0], nums[j] = nums[j], nums[0]
            # j-1 变成尾部，并从堆顶0开始调整堆
            maxHepify(nums, 0, j -1)

        return nums[-k]




a = Solution().findKthLargest([3,2,3,1,2,4,5,5,6,8,7,4,5,6,8], k = 4)
print(a)


