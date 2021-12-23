# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # previous_node = None
        node_list = []

        while head:
            node_list.append(head.val)
            head = head.next

        left = 0
        right = len(node_list) -1
        while right > left:
            if node_list[left] == node_list[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

# node_list = ListNode(1)
#
# a = Solution().isPalindrome()
# print(a)
# 官方题解2 递归
class Solution2:
    def idPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def revurisively_check(current_node=head):
            if current_node is not None:
                if not revurisively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next

            return True

        return revurisively_check()

# def Solution4:
#     def isPalindrome(self, head:ListNode):
#         temp = head
#
#         def check(head: ListNode):
#             if head is None:
#                 return True
#
#             res = check(head.next) and (temp.val == head.val)
#             temp = head.next
#
#         return check(head)

# a = Solution2()
# print(a)

# 官方题解3 快慢指针
# 使用两个指针从头出发，第一个指针走一步，第二个指针走两步，
# 则第二个指针到达尾部的时候，第一个指针达到中间，然后反转后半部分的链表和前半部分的链表进行比较

class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False

            first_position = first_position.next
            second_position = second_position.next

        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def revers_list(self, head):
        previos = None
        currnet = head
        while currnet is not None:
            next_node = currnet.next
            currnet.next = previos
            previos = currnet
            currnet = next_node
        return previos