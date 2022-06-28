# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 关键是找到链表的中心节点，使用快慢指针
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        elif not head.next:
            return TreeNode(head.val)
        elif head.next and not head.next.next:
            return TreeNode(head.next.val, TreeNode(head.val))
        else:
            prev = slow = fast = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None

            return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(slow.next))


