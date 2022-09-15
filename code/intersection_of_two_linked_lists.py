# 给两个单链表的头结点heada和headb，找出并返回两个单链表相交的起始结点，如果两个链表不存在相交结点，返回null
# 整个链式结构中不存在环
# 函数返回结果后，链表必须保持其原始结构

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 最简单的哈希
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = []

        while headA:
            visited.append(headA)
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            headB = headB.next

        return None

    # 如果两个链表相交，相交的部分肯定是在链表的后半程
    # 让a指针先走遍A链表，再走遍B链表
    # b指针先走遍B链表，再走遍A链表
    # 那么两个指针走过的路程长度是一样的
    # 如果两个链表最终相交，那么这两个指针最终一定会相遇并且共同走过这段相交的道路
    # 所以两个链表第一次指向的结点相同的时候就是相交的那个结点
    # 再直白一点，链表A从相交的部分起长度分为a+c
    # 链表B从相交的部分起长度分为b+c
    # 那么 a+c+b+c = b+c+a+c
    # 并且最后走的路一定是c，所以从c的开头两个指针开始相遇
    def twopointer_getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa


