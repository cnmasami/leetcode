# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous

# 基本上题解都是这个思路，但是别人的比我快，他们写的代码比较简洁
# p, rev = head, None
# while p:
#     rev, rev.next, p = p, rev, p.next
#
# return rev
