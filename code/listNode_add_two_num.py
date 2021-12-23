# 给你两个非空 的链表，表示两个非负的整数。
# 它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。
# 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ret_ln = ListNode()
        hold = 0

        iter_ln = ret_ln

        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + hold
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + hold
                l1 = l1.next
            elif l2:
                val = l2.val + hold
                l2 = l2.next

            hold, val = divmod(val, 10)

            iter_ln.next = ListNode(val)
            iter_ln = iter_ln.next

        if hold != 0:
            iter_ln.next = ListNode(hold)

        return ret_ln.next