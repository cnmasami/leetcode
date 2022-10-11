# 用队列实现栈
#
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，
# 并支持普通栈的全部四种操作（push、top、pop 和 empty）。
#
# 实现 MyStack 类：
#
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

#
# 注意：
#
# 你只能使用队列的基本操作 —— 也就是push to back、peek/pop from front、size 和is empty这些操作。
# 你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。
#
import collections


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return False if len(self.stack) else True



class MyStackTwoQueueV:
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


class MyStackQueueV:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) ->None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


#
# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()