# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。
# 返回 已排序的链表 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev = dummy = head

        head = head.next

        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head

            head = head.next


        return dummy


    # 官方题解代码更简洁
    def offical(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head

        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next


nod5 = ListNode(3)
nod4 = ListNode(3, nod5)
nod3 = ListNode(2, nod4)
nod2 = ListNode(2, nod3)
nod1 = ListNode(1, nod2)
nod0 = ListNode(1, nod1)

# 题解区看到还可以用快慢指针，不写了
a = Solution().deleteDuplicates(nod0)
while a:
    print(a.val)
    a = a.next
