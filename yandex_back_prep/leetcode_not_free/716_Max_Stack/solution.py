from typing import List


# MaxStack() Initializes the stack object.
# void push(int x) Pushes element x onto the stack.
# int pop() Removes the element on top of the stack and returns it.
# int top() Gets the element on the top of the stack without removing it.
# int peekMax() Retrieves the maximum element in the stack without removing it.
# int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
# You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        if len(self.stack) != 0:
            self.max_stack.pop(-1)
            return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        res = self.peekMax()
        buf = []
        while self.top() != res:
            buf.append(self.pop())

        self.pop()

        while buf:
            self.push(buf.pop(-1))

        return res
