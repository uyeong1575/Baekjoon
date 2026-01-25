import sys
from collections import deque

N = int(input())
E = int(input())

adj = {}
for i in range(E):
    a, b = map(int, sys.stdin.readline().strip().split())
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)

visited = set()
dq = deque()
def BFS(start):
    visited.add(start)
    dq.append(start)
    while dq:
        node = dq.popleft()
        for i in adj.get(node, []):
            if i not in visited:
                visited.add(i)
                dq.append(i)

BFS(1)
print(len(visited)-1)


