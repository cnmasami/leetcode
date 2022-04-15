# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 因为链表的头节点可能删除，需要dummpy指向头节点
    # cur指向dummy，如果cur.next与cur.next.next对应的元素相同，
    # 需要讲cur.next以及后面的拥有相同元素的链表全部删除，
    # 记下这个x，将链表中所有元素值为x的节点全部删除
    # 当cur.next与cur.next.next对应的元素不相同，说明链表中只有一个元素
    # 值为cur.next的系欸但，将cur指向cur.next
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 我做这种题就是总想着记录previous，但是官方就是一直是cur，然后比较cur.next与cur.next.next
        # 不向前看，只向后看
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


nod5 = ListNode(4)
nod4 = ListNode(3, nod5)
nod3 = ListNode(3, nod4)
nod2 = ListNode(2, nod3)
nod1 = ListNode(1, nod2)

a = Solution().deleteDuplicates(nod1)
while a:
    print(a.val)
    a = a.next


