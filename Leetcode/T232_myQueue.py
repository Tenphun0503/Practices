"""
Implement a first in first out (FIFO) queue using only two stacks.

The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Example:
    Input
        ["MyQueue", "push", "push", "peek", "pop", "empty"]
        [[], [1], [2], [], [], []]
    Output
        [null, null, null, 1, 1, false]

"""
class Solution:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    # Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)

    # Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()

    # Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    # Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk

class MyQueue:
    def __init__(self):
        self.stack1 = []

    def reverse(self, s):
        s_r = []
        while len(s) > 0:
            s_r.append(s.pop())
        return s_r

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        stack2 = self.reverse(self.stack1)
        res = stack2.pop()
        self.stack1 = self.reverse(stack2)
        return res

    def peek(self):
        stack2 = self.reverse(self.stack1)
        res = stack2[-1]
        self.stack1 = self.reverse(stack2)
        return res

    def empty(self):
        if len(self.stack1) > 0:
            return False
        else:
            return True

obj = MyQueue()
obj.push(1)
print(obj.stack1)
obj.push(2)
print(obj.stack1)
print(obj.peek())
print(obj.stack1)
print(obj.pop())
print(obj.stack1)
print(obj.empty())
