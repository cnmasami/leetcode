# 给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 还是要用dummpy node，因为如果left为1的话，他的previous总不能是None吧，总要有一套通用的方法
        dummy = still = ListNode(-1)
        still.next = head
        count = 0

        while True:
            previous = still
            still = still.next
            count += 1
            if count == left:
                revers_previous = previous
                revers_begin = still
            if count == right:
                revers_end = still
                break

        revers_next = revers_end.next
        sub_previous = None
        # revers_end.next = None
        # 这一步必须赋值给另一个变量，因为下面用到revers_begin.next，不赋值给另一个变量，就会改变revers_begin的值
        current = revers_begin

        # revers_end.next = None
        while left <= right:
            next_node = current.next
            current.next = sub_previous
            sub_previous = current
            current = next_node
            left += 1


        revers_previous.next = sub_previous
        revers_begin.next = revers_next

        return dummy.next

class Solution2:
    def reverseBetween(self, head:ListNode, left: int, right: int):
        def reverse_linked_list(head: ListNode):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        for _ in range(left -1):
            pre = pre.next

        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next

        left_node = pre.next
        curr = right_node.next

        pre.next = None
        right_node.next = None

        reverse_linked_list(left_node)

        pre.next = right_node
        left_node.next = curr
        return dummy_node.next

# 上面这两个方法都遍历了两次，下面我们遍历一次，每遇到一个节点就交换位置
# 这是我自己写的不对
class Solution3:
    def reverseBetween(self, head:ListNode, left: int, right: int):
        count = 0
        dummy = still = ListNode(-1)
        still.next = head

        while True:
            previous = still
            still = still.next
            count += 1
            if count == left:
                break

        current = still

        while left <= right:
            # 下一个节点
            next_node = current.next
            # 下下一个节点
            next_node_next = next_node.next
            # 当前节点的下一个节点是下下个节点
            current.next = next_node_next
            # 下一个节点的下一个节点是当前节点
            next_node.next = previous.next
            # 前一个节点的下一个节点是下一个节点
            previous.next = next_node
            # # 当前节点变为前一个节点
            # previous = current
            # #下下个节点是当前节点
            # current = next_node_next
            left += 1

        return dummy.next


class Solution4:
    def reverseBetween(self, head: ListNode, left:int, right:int):
        dummpy_node = ListNode(-1)
        dummpy_node.next = head
        pre = dummpy_node

        for _ in range(left, -1):
            pre = pre.next

        cur = pre.next

        for _ in range(right -  left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next

        return dummpy_node.next





node5 = ListNode(5, next= None)
node4 = ListNode(val=4, next=node5)
node3 = ListNode(val=3, next=node4)
node2 = ListNode(val=2, next=node3)
node1 = ListNode(val=1, next=node2)

a = Solution3().reverseBetween(node1, 2, 4)
while a:
    print(a.val)
    a = a.next