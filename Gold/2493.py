import sys
from collections import deque

n = int(sys.stdin.readline().strip())

a = list(map(int, sys.stdin.readline().strip().split()))
b = []
c = []
stk = deque(c)

for i in range(len(a)):   
    h = a[i]

    while stk and a[stk[-1]] < h:
        stk.pop()

    if not stk:
        b.append(0)
    else:
        b.append(stk[-1] + 1)  

    stk.append(i)

print(*b)

# list.index()는 매 번 o(n)이다.