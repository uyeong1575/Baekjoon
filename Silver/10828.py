n = int(input())

class Stack:

    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.ptr == 0:
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def size(self):
        return self.ptr

    def empty(self):
        if self.ptr == 0:
            return 1
        else:
            return 0
        
    def top(self):
        if self.ptr == 0:
            return -1
        else:
            return self.stk[self.ptr-1]
    
stack = Stack(n)


for _ in range(n):
    a = input().split()

    if a[0] == 'push':
        stack.push(int(a[1]))
    elif a[0] == 'pop':
        print(stack.pop())
    elif a[0] == 'size':
        print(stack.size())
    elif a[0] == 'empty':
        print(stack.empty())
    elif a[0] == 'top':
        print(stack.top())