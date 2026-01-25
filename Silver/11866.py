from collections import deque
import sys

n ,k = map(int, sys.stdin.readline().strip().split())

c = []
r = []

for i in range(n):
    c.append(i+1)

cq = deque(c)

while len(cq) > 0:
    for _ in range(k-1):
        cq.append(cq.popleft())
    r.append(cq.popleft())

print("<" + ", ".join(map(str, r)) + ">")