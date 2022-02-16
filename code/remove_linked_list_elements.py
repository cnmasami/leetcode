# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = prev = ListNode()
        dummy.next = head
        prev.next = head

        while head:
            if head.val == val:
                prev.next = head.next
                # head = head.next
            else:
                prev = head

            head = head.next

        return dummy.next

    # 递归 先删除除了头节点以外的数据，然后根据头节点的值判断需不需要删除头节点
    # 递归实现
    def recursion(self, head: ListNode, val:int):
        if not head:
            return head

        head.next = self.recursion(head.next, val)

        if head.val == val:
            return head.next
        else:
            return head


    def other_method(self, head:ListNode, val:int):
        dummy = ListNode()
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next





node7 = ListNode(6)
node6 = ListNode(5)
node5 = ListNode(4)
node4 = ListNode(3)
node3 = ListNode(6)
node2 = ListNode(2)
node1 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

a = Solution().removeElements([], 6)
while a:
    print(a.val)
    a = a.next
