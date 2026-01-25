import sys
from collections import deque

n = int(sys.stdin.readline().strip())

c = []

for i in range(n):
    c.append(i+1)

cq = deque(c)

while len(cq) > 1:
    cq.popleft()
    cq.append(cq.popleft())

print(*cq)

