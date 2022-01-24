# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dommy = res = ListNode()

        while list1 and list2:
            list1_val = list1.val
            list2_val = list2.val

            if list1_val <= list2_val:
                res.next = ListNode(list1_val)
                list1 = list1.next
            elif list1_val > list2_val:
                res.next = ListNode(list2_val)
                list2 = list2.next

            res = res.next

        if list1:
            res.next = list1

        if list2:
            res.next = list2

        return dommy.next

    # 官方题解，递归，判断两个链表的头节点，如果l1[0]< l2[0]那就是l1[1:]和l2做合并
    # 否则是l2[0]和l1做合并
    def offical(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


    # 官方迭代算法，同样是迭代，官方比我的迭代简洁的多,但其实我就是多写了赋值
    def offical_itera(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next




l14 = ListNode(4)
l12 = ListNode(2)
# l12.next=l14
l11 = ListNode(1)
l11.next = l12

l24 = ListNode(4)
l23 = ListNode(3)
l21 = ListNode(1)
l23.next = l24
l21.next = l23
l24.next = ListNode(5)


a = Solution().mergeTwoLists(l11, l21)

while a:
    print(a.val)
    a = a.next
