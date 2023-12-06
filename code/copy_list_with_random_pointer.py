#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 随机链表的复制

# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
#
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
#
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
#
# 返回复制链表的头节点。
#
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    # 哈希表的方法，哈希表里存放原链表节点和对应的新链表节点
    # 相当于遍历了两边，第一遍就按照普通的顺序创建链表
    # 第二遍遍历创建random的指向
    def copyRandomList_hash(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        dic = {}
        # 复制各个节点，并建立 原节点 -> 新节点 的map映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        # 构建新节点的next和random指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 返回新链表的头结点
        return dic[head]

    # 构建一个交叉拼接链表，链表内容为 原节点1-> 新节点1 -> 原节点2 -> 新节点2 -> ......
    # 然后构建新链表各节点的random指向：当访问原节点cur的随机指向节点cur.random的时候，
    # 对应新节点cur.next的随机指向节点为cur.random.next
    # 拆分链表，设置pre/cur分别指向原/新链表头结点，遍历执行pre.next = pre.next.next
    # 和cur.next=cur.next.next 将两链表拆分开
    # 返回新链表的res
    def copyRandomList2(self, head: 'Optional[Node]'):
        if not head: return

        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = res = head.next
        pre = head
        # 3. 拆分两链表
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next

        pre.next = None # 单独处理原链表尾节点
        return res







