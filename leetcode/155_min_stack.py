class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        print('push :', val)
        if len(self._stack) == 0:  
            self._stack.append(val)
            self._min_stack.append(val)
        else:
            self._stack.append(val)
            if val < self._min_stack[-1]:
                self._min_stack.append(val)
            else:
                self._min_stack.append(self._min_stack[-1])
        print('self._stack :', self._stack)
        print('self._min_stack :', self._min_stack)
    def pop(self) -> None:
        if len(self._stack) == 0:
            return None
        else:
            self._min_stack.pop()
            return self._stack.pop()
 
    def top(self) -> int:
        return self._stack[-1]
    
    def getMin(self) -> int:
        return self._min_stack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(-3)
obj.push(5)

print(obj.pop())
print(obj.getMin())
