import sys

class que:

    def __init__(self, cap):
        self.cap = cap
        self.q = [None] * cap
        self.ptf = 0
        self.ptb = 0

    def push(self, value):
        self.q[self.ptb] = value
        self.ptb += 1

    def pop(self):
        if self.size() == 0:
            return -1
        tmp = self.q[self.ptf]
        self.ptf += 1
        return tmp

    def size(self):
        return self.ptb - self.ptf

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.empty() == 1:
            return -1
        return self.q[self.ptf]

    def back(self):
        if self.empty() == 1:
            return -1
        return self.q[self.ptb-1]


n = int(sys.stdin.readline().strip())
q = que(n)


for i in range(n):
    a = sys.stdin.readline().strip().split()
    if a[0] == 'push':
        q.push(a[1])
    elif a[0] == 'pop':
        print(q.pop())
    elif a[0] == 'size':
        print(q.size())
    elif a[0] == 'empty':
        print(q.empty())
    elif a[0] == 'front':
        print(q.front())
    elif a[0] == 'back':
        print(q.back())